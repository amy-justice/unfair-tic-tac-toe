import random

positions = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
winningCombos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]


def draw_board(positions):
    firstRow = '     |     |     \n  ' + positions[0] + '  |  '+ positions[1] + '  |  '+ positions[2] + '  \n_____|_____|_____'
    secondRow = '     |     |     \n  ' + positions[3] + '  |  '+ positions[4] +'  |  '+ positions[5] +'  \n_____|_____|_____'
    thirdRow = '     |     |     \n  '+ positions[6] + '  |  '+ positions[7] + '  |  '+ positions[8] + '  \n     |     |     '
    print(firstRow)
    print(secondRow)
    print(thirdRow)
    return

# who goes first? coin flip?
def first_move():
    coin = random.randint(1, 2)
    return coin

# get player move
def player_move(positions):
    print('Where do you want to go?')
    playerMove = input('Enter a number: ')
    if playerMove in positions:
        positions = ['X' if pos == playerMove else pos for pos in positions]
        draw_board(positions)
        nextMove = win_condition(positions)
        availableMoves = check_available(positions)
        if nextMove == True and availableMoves != None:
            computer_move(positions)
        elif availableMoves == None:
            print("Game over! Looks like it's a draw!")
    else:
        print('Pick another number!')
        player_move(positions)

# computer move
def computer_move(positions):
    print("\n My turn! \n")
    availableMoves = check_available(positions)
    compMove = move_logic(positions, availableMoves)
    positions = ['O' if pos == compMove else pos for pos in positions]
    draw_board(positions)
    nextMove = win_condition(positions)
    if nextMove == True and len(availableMoves) > 1:
        player_move(positions)
    elif len(availableMoves) == 1:
        print("Game over! Looks like it's a draw!")
   
# check win condition
def win_condition(positions):
    # winning combinations
    # 123, 456, 789, 147, 258, 369, 159, 357
    for i in winningCombos:
        if positions[i[0]] == positions[i[1]] and positions[i[1]] == positions[i[2]]:
            if positions[i[0]] == 'X':
                print('You beat me! Nice job!')
                return False
            else:
                print('I win! Loser.')
                return False
    return True

def check_available(positions):
    availableMoves = [pos for pos in positions if pos != 'X' and pos != 'O']
    if availableMoves != []:
        return availableMoves

def move_logic(positions, availableMoves):
    corners = ['1', '3', '7', '9']
    for i in winningCombos:
        combo = [positions[i[0]], positions[i[1]], positions[i[2]]]
        if combo.count('X') == 2 and combo.count('O') == 0:
            # check winning combos - if two are X, block
            move = [pos for pos in combo if pos != 'X']
            return move[0]
    for i in winningCombos:
        combo = [positions[i[0]], positions[i[1]], positions[i[2]]]
        if combo.count('O') == 2 and combo.count('X') == 0:
            # check winning combos - if two are O, try to win
            move = [pos for pos in combo if pos != 'O']
            return move[0]
    for i in winningCombos:
        combo = [positions[i[0]], positions[i[1]], positions[i[2]]]
        # needs to prefer going in combo including an O already
        if combo.count('O') == 1 and combo.count('X') == 0:
            move = [pos for pos in combo if pos != 'O']
            return random.choice(move)
    # if moving second, prefer to go for middle (5)
    if positions.count('5') == 1 and positions.count('X') == 1:
        return '5'
    # if moving first, prefer a corner (could be random? 1, 3, 7, 9)
    if positions.count('O') == 0 and positions.count('X') == 0:
        return random.choice(corners)
    return random.choice(availableMoves)

def game_start():
    #print board
    print('Let\'s play tic tac toe!')
    print("I'll flip a coin to see who goes first.")
    firstMove = first_move();
    if firstMove == 1:
        draw_board(positions)
        print("You go first!")
        player_move(positions)
    else: 
        print("I'll go first!")
        computer_move(positions)
    
game_start();



