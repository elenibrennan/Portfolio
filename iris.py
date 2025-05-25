import torch
import torch.nn as nn
import torch.nn.functional as F

#create a model class that inherits nn.Module
class Model(nn.Module):
    #input layer (4 features of the flower) ->
    # Hidden Layer1 (neurons) ->
    # H2 (n) -> 
    # output (3 classes of iris flowers)
    def __init__(self, in_features = 4, h1 = 8, h2 = 8, out_features = 3):
        super().__init__() #instantiate nn.Module
        #fc1 = full connected 1 and 2
        #need to do for each layer
        self.fc1 = nn.Linear(in_features, h1)
        self.fc2 = nn.Linear(h1, h2)
        self.out = nn.Linear(h2, out_features)
    
    def forward(self, x):
        #relu says if the output is <0, call it 0, else use output
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.out(x)

        return x
    
#pick a manual seed for randomization
torch.manual_seed(33)
model = Model()

#import the data
import pandas as pd

url = "https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv"
df = pd.read_csv(url)

#change last column from strings to ints
df['species'] = df['species'].replace('setosa', 0.0)
df['species'] = df['species'].replace('versicolor', 1.0)
df['species'] = df['species'].replace('virginica', 2.0)

print(df)

#train, test, and split (set x,y)
#drop species because it is the y, not the features
X = df.drop('species', axis=1)
y = df['species']

#convert to numpy arrays
X = X.values
y = y.values

from sklearn.model_selection import train_test_split

#train test split
#test size is 20%, train size is 80%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=33)

#convert to tensors
#want it to be a float tensor because all data are floats
#convert X features to float tensors
X_train = torch.FloatTensor(X_train)
X_test = torch.FloatTensor(X_test)

#convert y labels to long tensors 
#long tensors are 64 bit integers
y_train = torch.LongTensor(y_train)
y_test = torch.LongTensor(y_test)

#set criterion of model to measure the error (how far off is the prediction from the data)
criterion = nn.CrossEntropyLoss()
#choose Adam optimizer, lr = learning rate
#lr is if error doesnt go down after a bunch of epochs (iterations), we want to lower learning rate
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

#TRAIN MODEL
#Epochs? (1 run thru all training data)
epochs = 100
losses = []

for i in range(epochs):
    #Go forward and get a prediction
    y_pred = model.forward(X_train) #get predicted results

    #measure the loss/error, will be high at first
    loss = criterion(y_pred, y_train) #predicted value vs y_train value

    #keep track of losses
    losses.append(loss.detach().numpy())

    #print every 10 epochs
    if i % 10 == 0:
        print(f'Epoch: {i} and Loss: {loss}')

    #Do back propogation (take error rate of forward prop and feed it back
    # through the network to fine tune the weights) 
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

#Evaluate model on test data set
with torch.no_grad(): #turn off back prop
    y_eval = model.forward(X_test) #X_test are features from test set, y_eval will be predictions
    loss = criterion(y_eval, y_test) #find error of y_eval vs y_test
    print(loss)

# ...existing code...

# Evaluate model on test data set
with torch.no_grad():
    y_eval = model.forward(X_test)
    predicted = torch.argmax(y_eval, dim=1)
    correct = []
    wrong = []
    for idx in range(len(y_test)):
        if predicted[idx] == y_test[idx]:
            correct.append(idx)
        else:
            wrong.append(idx)
    print(f"Correctly classified indices: {correct}")
    print(f"Incorrectly classified indices: {wrong}")
# Optionally, print the actual predictions and true labels for inspection
    print("Predicted:", predicted.tolist())
    print("Actual:   ", y_test.tolist())