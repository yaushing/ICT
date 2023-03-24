"""
    Basic
    _____

    Metal
    Gems
    Wood


"""

### IMPORTS ###

from time import *
from math import *
try: from devkey import *
except: print("No DevKey Found")

#################
### VARIABLES ###
#################

resources = {
    "M":"Metal",
    "G": "Gems",
    "W":"Wood"
}

idle_resource = {
    "Metal":[[10, "Metal"], [5, "Wood"]],
    "Gems":[[10, "Metal"], [15, "Gems"]],
    "Wood":[[10, "Metal"], [10, "Wood"]],
}

#################
### FUNCTIONS ###
#################

def clean_file(lines):
    cleaned_lines = []
    for line in lines:
        clean_line = line.strip("\n")
        cleaned_lines.append(int(clean_line, base=2))
    return cleaned_lines

def update_game_stats(current_game_stats):
    new_game_stats = {}
    for resource, amount in current_game_stats.items():
        new_game_stats[resource] = [amount[0], int(amount[1]) + int(amount[0])]
    return new_game_stats

def parse_move(msg):
    n = input(msg).upper()
    if n == "B":
        return "buy"
    elif n == "G":
        return "research"
    elif n == "A":
        return "go"
    elif n == "S":
        return "save"
    else: return parse_move(msg)

def convert_all_int(game_stats):
    new_game_stats = game_stats.copy()
    for k, v in game_stats.items():
        new_game_stats[k] = [int(v[0]), int(v[1])]
    return new_game_stats
def parse_int(input_given, msg, Max = 10000000, Min = 0, forbid = 0, exceptions = []):
    try:
        if input_given in exceptions:
            return input_given
        int(input_given)
        if int(input_given) > Max or int(input_given) < Min:
            raise ValueError()
        if int(input_given) == forbid:
            raise ValueError()
        return int(input_given)
    except:
        return parse_int(input(msg), msg, Max, Min, forbid, exceptions)

def parse_buy(msg, things_to_buy=["M", "G", "W"]):
    n = input(msg).upper()
    if n in things_to_buy: return resources[n]
    else: return parse_buy(msg)

def check_can_buy(game_stats, costs):
    amt = []
    for cost in costs:
        if game_stats[cost[1]][1] < cost[0]: return (False, None, (cost[0] - game_stats[cost[1]][1], cost[1]))
        amt.append(floor(game_stats[cost[1]][1] / cost[0]))
    return (True, min(amt))


def buy(game_stats):
    new_game_stats = game_stats.copy()
    for k, v in game_stats.items():
        print(f"Cost of idle {k}: ", end = "")
        for cost in idle_resource[k]:
            print(cost[0],  cost[1], end=" ")
        print()
    buy = parse_buy("Buy idle [M]etal, [G]em, or [W]ood: ")
    print("Buy "+ buy)
    print(f"Cost of one idle {buy}: ", end="")
    for cost in idle_resource[buy]:
        print(f"{cost[0]} {cost[1]}, ", end="")
    print()
    can_buy = check_can_buy(game_stats, idle_resource[buy])
    if can_buy[0]:
        print(f"You can buy {can_buy[1]} idle {buy}")
    else:
        print(f"You can't buy any more idle {buy}. You need {can_buy[2][0]} more {can_buy[2][1]}")
        return game_stats
    amt_to_buy = parse_int(input(f"How many idle {buy} would you like to buy? "), f"How many idle {buy} would you like to buy? ", can_buy[1], 0)
    new_game_stats[buy][0] += amt_to_buy
    return new_game_stats

def generate_lines(game_stats):
    lines = []
    for k, v in game_stats.items():
        lines.append(str(bin(v[0])) + "\n")
        lines.append(str(bin(v[1])) + "\n")
    lines.append(str(bin(floor(time()))))
    return lines

######################
### LOAD GAME DATA ###
######################

name = input(f"Player name: ")
try:
    with open("IDLE_Space_Savefile.txt", "r") as f:
        file_lines = f.readlines()
        cleaned_files = clean_file(file_lines)
        game_stats = {
            "Metal": [cleaned_files[0], cleaned_files[1]],
            "Gems": [cleaned_files[2], cleaned_files[3]],
            "Wood": [cleaned_files[4], cleaned_files[5]],
        }
        saved = True
except:
    print("Save not found.")
    game_stats = {
        "Metal": [1, 0],
        "Gems": [1, 0],
        "Wood": [1, 0],
    }
    saved = False

try:
    if name in list(decrypt_keystore().keys()):
        dev = True
    else:
        dev = False
except:
    dev = False

#################
### Game Loop ###
#################
start_time = floor(time())
new = True
if saved:
    past_time = cleaned_files[-1]
    for _ in range(start_time-past_time):
        game_stats = update_game_stats(game_stats)
    print("IDLE resources added.")
while 1 > 0:
    game_stats = convert_all_int(game_stats)
    if new:
        game_stats = update_game_stats(game_stats)
        for k, v in game_stats.items():
            print("_______\n")
            print(f"{k}")
            print(f"{v[0]} {k} per turn")
            print(f"{v[1]} {k} currently")
    move = parse_move("[B]uy something, [G]o to research page, [A]dvance to next turn or [S]ave and quit: ")
    if move == "buy":
        game_stats = buy(game_stats)
        new = False
    elif move == "research":
        # research
        new = False
    elif move == "save":
        with open("IDLE_Space_Savefile.txt", "w") as f:
            f.writelines(generate_lines(game_stats))
        quit()
    else: new = True