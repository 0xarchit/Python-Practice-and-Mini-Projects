import random
def print_board(lst):
    st = '''
    {}|{}|{}
    -----
    {}|{}|{}
    -----
    {}|{}|{}
    '''.format(*lst)
    print(st)

choices = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
print("Welcome to Tic Tac Toe!")
print_board(choices)

turns = "X"
Flag = True
while Flag:
    while ' ' in choices:
        mv = eval(input(f"Enter your move {turns}, Your moves [0-8]: "))
        if mv not in range(9):
            print("Invalid move, try again.")
            continue
        if choices[mv] == ' ':
            choices[mv] = turns
        elif choices[mv] != ' ':
            print("Invalid move, try again.")
            continue
        print_board(choices)

        if choices[0] == choices[1] == choices[2] != ' ':
            print(f"Player {turns} wins!")
            break
        if choices[3] == choices[4] == choices[5] != ' ':
            print(f"Player {turns} wins!")
            break
        if choices[6] == choices[7] == choices[8] != ' ':
            print(f"Player {turns} wins!")
            break
        if choices[0] == choices[3] == choices[6] != ' ':
            print(f"Player {turns} wins!")
            break
        if choices[1] == choices[4] == choices[7] != ' ':
            print(f"Player {turns} wins!")
            break
        if choices[2] == choices[5] == choices[8] != ' ':
            print(f"Player {turns} wins!")
            break
        if choices[0] == choices[4] == choices[8] != ' ':
            print(f"Player {turns} wins!")
            break
        if choices[2] == choices[4] == choices[6] == '0':
            print(f"Player {turns} wins!")
            break
        turns = 'X' if turns == '0' else '0'
    else:
        print("It's a draw!")
    if input('Do you want to continue T/N? ') == 'Y':
        choices = [' ']*9
    else:
        Flag = False
else:
    print("Thanks for playing!")

    # computer vs human mode