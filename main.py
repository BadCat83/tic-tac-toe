import random
import re


class Player:
    """"Player represented class"""

    def __init__(self, name, first_move=False):
        self.player_turns = set()
        self.name = name
        self.first_move = first_move

    def write_progress(self, turn):
        self.player_turns.add(turn)


def print_board(players=None):
    numbers = [str(_) for _ in range(1, 10)]
    print('-' * 13)
    for i in range(1, 10, 3):
        for val in reversed(numbers[-i:-i - 3:-1]):
            if players:
                if val in players[0].player_turns:
                    val = 'X'
                elif val in players[1].player_turns:
                    val = '0'
                else:
                    val = ' '
            print(f"| {val} ", end='')
        print(f"|\n{'-' * 13}")


def print_help():
    print("Use numpad for make a move, every cell matches to the certain number")
    print_board()
    print("If you want to exit, print '0', for help print 'h'")


def introduce(player=None):
    player_name = input("Player, please, introduce yourself: ")

    if not player and input("Would you like to go first? y/n: ").lower() == 'y':
        pass
    elif player and not player.first_move:
        print("Sorry, you haven't got a choice.")
    else:
        print("You go second.")
        return Player(player_name)
    print("You go first.")
    return Player(player_name, True)


def check_player_turn(move, players):
    if move % 2 == players[0].first_move:
        return players[0]
    else:
        return players[1]


def check_input(input_str):
    return re.match(r'[0-9h]', input_str)


def check_winner(player):
    win_combination = ({7, 8, 9}, {4, 5, 6},
                       {1, 2, 3}, {1, 4, 7},
                       {2, 5, 8}, {3, 6, 9},
                       {3, 5, 7}, {1, 5, 9},)
    win_phrase = ("Take the cake!",
                  "Cookie for you!",
                  "Winner winner, chicken dinner!",
                  "Take a pie from the shelf!",
                  "Well, zippity-doo for you.",)
    for win_set in win_combination:
        if len(player.player_turns.intersection(map(str, win_set))) == 3:
            print(f"Congratulation to you, {player.name}! "
                  f"{random.choice(win_phrase)}")
            return True
    return False


def start_game():
    print_help()
    first_player = introduce()
    second_player = introduce(first_player)
    move = 1
    while move < 10:
        current_player = check_player_turn(move, (first_player, second_player))
        if player_input := check_input(input(f"{move} round: {current_player.name}"
                                             f" makes a move: ")):
            player_input = player_input.group()
            if player_input == '0':

                break
            elif player_input == 'h':
                print_help()
            else:
                if player_input not in first_player.player_turns | second_player.player_turns:
                    current_player.write_progress(player_input)
                    move += 1
                    print_board((first_player, second_player))
                else:
                    print("The cell is already occupied")
                    continue
        else:
            print('Incorrect input, try one more time.')
            continue
        if len(current_player.player_turns) > 2:
            if check_winner(current_player):
                break
    print("Game over. Thank you for playing")


if __name__ == '__main__':
    print("Welcome to the game!")
    try:
        start_game()
    except Exception as e:
        print(e)
    finally:
        print("Bye, have a nice day!")
