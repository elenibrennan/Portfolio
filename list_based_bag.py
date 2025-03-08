#Eleni Brennan, pledged 
import random

def clear_bag(the_bag):
    for i in range(len(the_bag)):
        the_bag[i]="<empty>"


def is_bag_empty(the_bag):
    for i in range(len(the_bag)):
        if(the_bag[i]!="<empty>") :
            return False
    ##All bag locations checked, all are empty.
    return True


def print_bag(the_bag):
    #prints the bag
    print(the_bag)

def add_item_to_bag(item, the_bag, position=None):
    #iterates through every position in the length of the bag
    for i in range(len(the_bag)):
        #if the position of the bag is empty, insert item
        if(the_bag[i] == '<empty>'):
            the_bag[i]=item
            return 
        else:
            print(f'Could not add item {item} because bag is full')
        

def remove_item_from_bag(position_or_item, the_bag):
    #by position
    #checks if it is a position entered
    if isinstance(position_or_item, int):
        pos=position_or_item
        if the_bag[pos] == '<empty>':
            print(f'Could not remove item at position {pos} because position {pos} is empty')
            return '<empty>'
        else:
            removed_item = the_bag[pos]
            the_bag[pos] = '<empty>'
            return removed_item
    
    #by item
    #checks if it is an item entered
    if isinstance(position_or_item, str):
        item=position_or_item
        if item not in the_bag:
            return None
        else:
            remove_item=the_bag.index(item)
            the_bag[remove_item]='<empty>'
            return item
        ###TODO
        

def get_number_of_items_in_bag(the_bag):
    #subtracts the number of empty slots from total slots to get item count
    return len(the_bag) - the_bag.count('<empty>')
    
    #previous code, also works but longer

    #count=0
    #for i in range(len(the_bag)):
         #if the_bag[i] != '<empty>':
             #count += 1
    #return count


def shuffle_bag(the_bag):
    #uses random shuffle to shuffle items in place 
    random.shuffle(the_bag)


def sort_bag(the_bag):
    the_bag.sort()


def merge_bags(bag1, bag2):
    #merges two bags, then uses the clear_bag function 
    merged_bag= bag1 + bag2
    
    clear_bag(bag1)
    clear_bag(bag2)
    
    
    return merged_bag


def main():

    print("MY BACKPACK")
    my_backpack=[None]*8
    print_bag(my_backpack)
    clear_bag(my_backpack)
    print("The claim that the bag is empty is", is_bag_empty(my_backpack))
    print_bag(my_backpack)
    add_item_to_bag("sword",my_backpack)
    add_item_to_bag("torch",my_backpack)
    add_item_to_bag("sword",my_backpack)
    add_item_to_bag("apple",my_backpack,6) ##place apple in position 6.
    add_item_to_bag("wallet",my_backpack,7) ##place wallet in position 7
    print_bag(my_backpack)
    print("The claim that the bag is empty is", is_bag_empty(my_backpack))
    print("Number of items in bag:", get_number_of_items_in_bag(my_backpack))
    position_of_removed_sword=remove_item_from_bag("sword",my_backpack)
    print("Removed from backpack the sword at position:", 
           position_of_removed_sword)
    ##The following fails, no orange in bag.
    position_of_removed_orange=remove_item_from_bag("orange",my_backpack)
    print("Removed from backpack the orange at position:",
           position_of_removed_orange)
    print_bag(my_backpack)
    print("Number of items in bag:", get_number_of_items_in_bag(my_backpack))

    print("MY HANDBAG")
    my_handbag=[None]*4
    clear_bag(my_handbag)
    print("The claim that the bag is empty is", is_bag_empty(my_handbag))
    add_item_to_bag("comb",my_handbag)
    add_item_to_bag("sunscreen",my_handbag)
    add_item_to_bag("lipstick",my_handbag,1)##fails, already occupied
    add_item_to_bag("mirror",my_handbag,2)
    add_item_to_bag("clippers",my_handbag)
    add_item_to_bag("phone",my_handbag)##fails, bag is full
    print("The claim that the bag is empty is", is_bag_empty(my_handbag))
    print_bag(my_handbag);
    print("Number of items in bag:", get_number_of_items_in_bag(my_handbag))
    print("Now sort the items in the bag...")
    sort_bag(my_handbag)
    print_bag(my_handbag)
    print("Number of items in bag:", get_number_of_items_in_bag(my_handbag))

    print("MY SUITCASE")
    suitcase=merge_bags(my_backpack,my_handbag)
    print("After the merger: ");
    print("The claim that the backpack is empty is", is_bag_empty(my_backpack))
    print("The claim that the handbag is empty is", is_bag_empty(my_handbag))
    print("The claim that the suitcase is empty is", is_bag_empty(suitcase))
    print_bag(suitcase)
    add_item_to_bag("shirt",suitcase)
    add_item_to_bag("towel",suitcase)
    print_bag(suitcase)
    print("Number of items in suitcase:",
           get_number_of_items_in_bag(suitcase))
    item4_from_suitcase=remove_item_from_bag(4,suitcase)##empty location
    print("Unsuccessful removal attempt at pos. 4:",item4_from_suitcase)
    item2_from_suitcase=remove_item_from_bag(2,suitcase)
    print("Removed from suitcase at pos. 2 the item:",item2_from_suitcase)
    print_bag(suitcase)
    print("Number of items in suitcase:",
           get_number_of_items_in_bag(suitcase))
    print("Now randomly shuffle the suitcase...")
    shuffle_bag(suitcase)
    print_bag(suitcase)
    print("Number of items in suitcase:",
           get_number_of_items_in_bag(suitcase))

##end of main()


if __name__ == '__main__':
    main() #initiate execution

