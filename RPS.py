import itertools
import os
import platform
import random


if platform.system() == "Windows":
    os.system('cls')
else:
    os.system('clear')

last_moves_count = {}
num_last_moves = 4



def create_last_moves_count(length):
    global last_moves_count

    if length <= 0: return {}
    keys = [''.join(combo) for combo in itertools.product("RPS", repeat=length)]
    return {key: 0 for key in keys}
    

def player(prev_play, opponent_history=[]):
    global last_moves_count, num_last_moves

    if prev_play == "":
        opponent_history.clear()
        last_moves_count = {}
        return random.choice(['R', 'P', 'S'])

    if len(last_moves_count) == 0:
        last_moves_count = create_last_moves_count(num_last_moves)

    opponent_history.append(prev_play)

    if len(opponent_history) < num_last_moves:
        return random.choice(['R', 'P', 'S'])

    last_moves = "".join(opponent_history[-num_last_moves:])

    if last_moves not in last_moves_count:
        last_moves_count[last_moves] = 0
    last_moves_count[last_moves] += 1

    potential_next_moves = [
        last_moves[1:] + "R",
        last_moves[1:] + "P",
        last_moves[1:] + "S",
    ]

    sub_last_moves_count = {
        key: last_moves_count[key]
        for key in potential_next_moves
    }

    predicted_next_move = max(sub_last_moves_count, key=sub_last_moves_count.get)[-1]

    counter_moves = {'R': 'P', 'P': 'S', 'S': 'R'}
    return counter_moves[predicted_next_move]


   