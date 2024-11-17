import random
# function to display the game field
def display_board(board):
    
    print("Here is the current game board: ")
    
    print('       ',board[0],'|',board[1],'|',board[2])
    print('       ',board[3],'|',board[4],'|',board[5])
    print('       ',board[6],'|',board[7],'|',board[8])

#fucntion to choose the player character(X or O)
def player_character(first, second):
    player1 = 'WRONG'
    # print("Welcome to the game! \n\nAnytime you want the exit the game type 'exit' ")
    while player1 not in ['X', 'O']:
        player1 = input(f"Player {first}, please choose your game character (X or O): ").upper()
        if player1 == 'EXIT':
            exit_game()
            continue
        if player1 not in ['X', 'O']:
            print(f"Player {first}, you entered invalid input, please try again.")
    if player1 == 'X':
        player2 = 'O'
        print(f"Player {first} has - 'X' and Player {second} has - 'O'")
    else:
        player2 = 'X'
        print(f"Player {first} has - 'O' and Player {second} has - 'X'")
    return player1, player2
        
# function to take player1 choice
def player1_choice(board, first):
    choice = 'wrong'
    
    while choice not in board and (choice != 'x' or 'o'):
        choice = input(f'PLayer {first}, please select your index: ')
        if choice == 'exit':
            exit_game()
            #setting the choice back to 'wrong' so that the loop can continue working 
            choice = 'wrong'
            continue
        if choice not in board and (choice != 'x' or 'o'):
            print("Sorry, you entered invalid or already taken index! ")

    return int(choice)

# function to take player2 choice
def player2_choice(board, second):
    choice = 'wrong'
    
    while choice not in board and (choice != 'x' or 'o'):
        choice = input(f'PLayer {second}, please select your index: ')
        if choice == 'exit':
            exit_game()
            #setting the choice back to 'wrong' so that the loop can continue working 
            choice = 'wrong'
            continue
        if choice not in board and (choice != 'x' or 'o'):
            print("Sorry, you entered invalid or already taken index! ")

    return int(choice)

#function to replace the field with players' choice
def replace_field(board, index, player):
    board[index] = player
    return board

#fucntion to check winner
def check_winner(board, player1, player2):
    #check first row and first column
    if board[0] == board[1] == board[2] or board[0] == board[3] == board[6] :
        if board[0] == player1:
            print("PLayer 1 won")
            return player1
        else:
            print('Player 2 won')
            return player2
    #check second row and second column 
    if board[3] == board[4] == board[5] or board[1] == board[4] == board[7]:
        if board[4] == player1:
            print("PLayer 1 won")
            return player1
        else:
            print('Player 2 won')
            return player2
    #check third row and rhird column 
    if board[6] == board[7] == board[8] or board[2] == board[5] == board[8]:
        if board[8] == player1:
            print("PLayer 1 won")
            return player1
        else:
            print('Player 2 won')
            return player2
    #check diagonals
    if board[0] == board[4] == board[8] or board[2] == board[4] == board[6]:
        if board[4] == player1:
            print("PLayer 1 won")
            return player1
        else:
            print('Player 2 won')
            return player2
    return False

#function to check a draw 
def check_draw(board):
    check_for_unique =  list(set(board))
    check_for_unique.sort()
    if check_for_unique == ['O', 'X', 'exit']:
        print("Draw this time! Play again to choose the best!")
        return True
    else: 
        return False
    
#fucntion to ask for a one more game
def play_again():
    choice = 'wrong'
    
    while choice not in ['YES', 'NO']:
        choice = input("Do you want to play again? ('Yes' or 'No') ").upper()
        
        if choice not in ['YES', 'NO']:
            print('Sorry, you input is invalid, try again. ')
    if choice == 'YES':
        return True
    else:
        return False

#fucntion to exit the game
def exit_game ():
    if play_again() == False:
        print("Thanks you for the game!")
        exit()
    else:
        pass

#function to randomly choose a player for first move 
def random_choice():
    first = random.randint(1,2)
    second = 0
    if first == 1:
        second = 2
    else:
        second = 1
    return first, second

#EXECUTION     
    
# #creating variable to check how long we will play
play_more = True
print("Welcome to the game! \n\nAnytime you want the exit the game type 'exit' ")
while play_more:
    #creating a new boards
    board = ['0','1','2','3','4','5','6','7','8', 'exit']
    #assigning the player id to the first and second moves
    first, second = random_choice()
    print(f"\nPlayer {first} will go first")
    #calling function to determine players' characters
    player1, player2 = player_character(first, second)
    
    #displaying the new board to the players 
    display_board(board)
    #the loop will work until the win of player
    while check_winner(board, player1, player2) == False:
        board = replace_field(board, player1_choice(board, first), player1)
       # print('\n'*100)
        display_board(board)
        #checking if we already have a winner
        if check_winner(board, player1, player2) != False:
            break
        #checking after first player move for a draw because 9 % 2 = 1
        if check_draw(board) == True:
            break
        board = replace_field(board, player2_choice(board, second), player2)
       # print('\n'*100)
        display_board(board)
    play_more = play_again()
print('Thank you for the game!')