import random
import os



# draw a player in the grid

# move player, unless invalid move (past edges of grid)
# check for win/lose
# clear screen and random grid

# draw grid
CELLS = [
    (0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
    (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
    (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
    (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
    (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)
]


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# pick random location for the player, the monster, the exit door
def get_locations():
    return random.sample(CELLS, 3)


def move_player(player, move):
    x, y = player

    if move == "L":
        x -= 1
    if move == "R":
        x += 1
    if move == "U":
        y -= 1
    if move == "D":
        y += 1

    return x, y

# take input or movement
def get_move(player):
    moves = ["L", "R", "U", "D"]

    x, y = player

    if x == 0:
        moves.remove("L")
    if x == 4:
        moves.remove("R")
    if y == 0:
        moves.remove("U")
    if y == 4:
        moves.remove("D")

    return moves


def draw_map(player):
    print(" _" * 5)
    tile = "|{}"

    for cell in CELLS:
        x, y = cell
        if x < 4:
            line_end = ""
            if cell == player:
                output = tile.format("X")
            else:
                output = tile.format("_")
        else:
            line_end = "\n"
            if cell == player:
                output = tile.format("X|")
            else:
                output = tile.format("_|")
        print(output, end=line_end)


def game_loop():
    monster, door, player = get_locations()
    playing = True

    while playing:
        clear_screen()
        draw_map(player)
        valid_moves = get_move(player)
        print("you're currently in room {}".format(player))
        print("you can move {}".format(", ".join(valid_moves)))
        print("Enter `QUIT` to quit.")

        move = input("> ")
        move = move.upper()

        if move == 'QUIT':
            break

        if move in valid_moves:
            player = move_player(player, move)

            if player == monster:
                print("\n ** OH NO! The monster got you! Better luck next time! ** \n")
                playing = False
            if player == door:
                print("\n ** You scaped! Congratulation general ** \n")
                playing = False
        else:
            input("\n ** Walls are hard! Don't run into them! ** \n")
    else:
        if input('Play again? [Y/n] ').lower() != "n":
            game_loop()


clear_screen()
print("welcom to the dungeon!")
input("press `return` to start!")
clear_screen()
game_loop()
