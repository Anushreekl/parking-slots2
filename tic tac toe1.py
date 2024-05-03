def board(lst):
    count = 0
    for i in range(3):
        for j in range(3):
            if lst[count] == 0:
                print("__ |", end="")
            else:
                print(lst[count], " | ", end="")
            count += 1
        print()

def swap_users(user):
    if user == "X":
        return "O"
    else:
        return "X"

def win(lst):
    # Check rows
    for i in range(0, 9, 3):
        if lst[i] == lst[i+1] == lst[i+2] != 0:
            return lst[i] + " Wins"

    # Check columns
    for i in range(3):
        if lst[i] == lst[i+3] == lst[i+6] != 0:
            return lst[i] + " Wins"

    # Check diagonals
    if lst[0] == lst[4] == lst[8] != 0 or lst[2] == lst[4] == lst[6] != 0:
        return lst[4] + " Wins"

    # Check for draw
    if all(cell != 0 for cell in lst):
        return "It's a draw!"

    return None

lst = [0, 0, 0, 0, 0, 0, 0, 0, 0]
user = "X"
game = True

print("Welcome to Tic-Tac-Toe!")

while game:
    board(lst)
    n = int(input(f"Player {user}, enter your selection (1-9): "))

    if 1 <= n <= 9 and lst[n-1] == 0:
        lst[n-1] = user
        result = win(lst)
        if result:
            print(result)
            game = False
        else:
            user = swap_users(user)
    else:
        print("Invalid selection. Try again.")
