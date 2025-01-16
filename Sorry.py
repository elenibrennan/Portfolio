import random

# data
players = ('Red', 'Blue', 'Green', 'Yellow')
start_names = ('Sr', 'Sb', 'Sg', 'Sy')
start_positions = (0, 10, 20, 30)
end_names = ('Gr', 'Gb', 'Gg', 'Gy')
end_positions = (39, 9, 19, 29)

# initialize starting variables
pawns = [-1, -1, -1, -1]
pawns_name = ['Sr', 'Sb', 'Sg', 'Sy']
winner = ""
turn = 0

print ("New Game!")
# beginning of outer loop
# keep going until a winner
while winner == "":
    turn += 1
    print ("\nPlaying turn:",turn)
    # take each player's turn
    for player in range(4):
        # skip next player (continue) if there is already a winner
        if winner != "":
            continue
        player_name = players[player]
        # prepare a flag for when a player's turn is over (rules are that they keep going if they roll 6s)
        turn_over = False
        # as long as the player turn is not over, they continue
        while not turn_over:
            old_pawn = pawns[player]
            old_pawns_name = pawns_name[player]
            roll = random.choice(range(1, 7))
            print (player_name,"is playing and rolled a",roll,"...  ")
            
            # test if player is stuck in start
            if old_pawn == -1:
                # then if a 6 is rolled you jump to the start 
                if roll == 6:
                    pawns[player] = start_positions[player]
                    pawns_name[player] = str(pawns[player])
            # if not stuck in start, move your rolled amount
            else:
                pawns[player] += roll
                pawns_name[player] = str(pawns[player])
                
            # test if player is in range of finishing: between end_position and end_position-6
            # This is really critical.  For example, Blue finishes when they get to 9+1, but they start at 10 which is also 9+1. 
            # So you cant just test for 9+1 all the time. You only test if they are currently within 5 spaces from finishing
            if end_positions[player] - 6 < old_pawn <= end_positions[player]:
                # test if player overshot the end_position and if so, no move
                if pawns[player] > end_positions[player] + 1:
                    pawns[player] = old_pawn
                    pawns_name[player] = str(pawns[player])
                # test did they finish?
                if pawns[player] == end_positions[player] + 1:
                    pawns_name[player] = end_names[player]
                    winner = players[player]
                    turn_over=True

            # if not in range of finishing, then we allow the roll and have to jump from 39 to 0 whenever that line is crossed
            else:
                if pawns[player] > 39:
                    pawns[player] -= 40
                    pawns_name[player] = str(pawns[player])

            # If you dont roll 6, your turn is over so we just set the flag
            if roll < 6:
                turn_over = True
            print ("moving from",old_pawns_name,"to",pawns_name[player])
            
            # now look for hits/collisions with other players to send them back to start
            # First, confirm you are out of start position. This is critical as all pieces start at the same time -1 position
            if pawns[player] > -1:
                for hit in range(4):
                    # don't hit yourself
                    if hit == player:
                        continue
                      
                    # if you hit another piece, they go back to their start.  Sorry!
                    if pawns[player] == pawns[hit]:
                        pawns[hit] = -1
                        pawns_name[hit] = start_names[hit]
                        print ("Player", players[hit], "was hit and sent back to", pawns_name[hit], "Sorry!!")


print ("Winner is", winner, "!!!")

