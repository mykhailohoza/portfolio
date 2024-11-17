def replace_field(board, index, player):
    board[index] = player
    print(board)

board = ['0','1','2','3','4','5','6','7','8']
ind = 4
player = 'X'
replace_field(board, ind, player )

