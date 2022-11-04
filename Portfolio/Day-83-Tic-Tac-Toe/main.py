board = {
                '1': ' ' , '2': ' ' , '3': ' ' ,
                '4': ' ' , '5': ' ' , '6': ' ' ,
                '7': ' ' , '8': ' ' , '9': ' ' ,
                }

values = [' ' for x in range(9)]

player_position = {'X':[], 'O':[] }

win_combinations = [[1,2,3],[4,5,6],[7,8,9],[1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
 
    # Loop to check if any winning combination is satisfied
    for x in soln:
        if all(y in player_pos[cur_player] for y in x):
 
            # Return True if any winning combination satisfies
            return True
    # Return False if no combination is satisfied       
    return False       
 
# Function to check if the game is drawn
def check_draw(player_pos):
    if len(player_pos['X']) + len(player_pos['O']) == 9:
        return True
    return False   


def print_board():
    # print( + '|' + board['2'] + '|' + board['3'])
    # print('-+-+-')
    # print(board['4'] + '|' + board['5'] + '|' + board['6'])
    # print('-+-+-')
    # print(board['7'] + '|' + board['8'] + '|' + board['9'])
    
    print(f"""{board['1']}|{board['2']}|{board['3']}
-+-+-
{board['4']}|{board['5']}|{board['6']}
-+-+-
{board['7']}|{board['8']}|{board['9']}
""")
   
    
def check_if_winner():

    
def game():
    turn = 'X'
    count = 0
    
    # There can only be 9 turns per game
    for i in range (10):
        print_board()
        print(f"{turn}'s turn. Please select your move: ")
        move = input()
        
        # If the spot is empty
        if board[move] == ' ':
            # Set the X or O to the spot
            board[move] = turn
            # Increase the turn count
            count += 1
        else:
            print("That option is invalid, please try again.")
            continue
        
    if count >=5:
        check_if_winner()
    
    
    
    