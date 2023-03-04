import random
from time import *
tienames = ["Tie!", "Tie! I hope this doesn't happen again.", "Tie! Please, make sure this game moves on.", "Draw."]
wins = {
    "Human":[["Tree", "Wolf", "Sponge", "Paper", "Air", "Water", "Dragon"], ["cuts down", "hunts", "breaks apart", "cuts", "breaths", "drinks", "kills"]],
    "Tree":[["Wolf", "Sponge", "Paper", "Air", "Water", "Dragon", "Devil"], ["falls and kills", "breaks apart", "cuts", "breaths", "drinks", "kills", "disproves"]],
    "Wolf":[["Sponge", "Paper", "Air", "Water", "Dragon", "Devil", "Lightning"], ["breaks apart", "cuts", "breaths", "drinks", "kills", "disproves", "lives through"]],
    "Sponge":[["Paper", "Air", "Water", "Dragon", "Devil", "Lightning", "Gun"], ["hates", "dries in", "absorbs", "absorbs", "softens", "absorbs", "muffles"]],
    "Paper":[["Air", "Water", "Dragon", "Devil", "Lightning", "Gun", "Rock"], ["dries in", "absorbs", "absorbs", "softens", "absorbs", "muffles", "covers"]],
    "Air":[["Water", "Dragon", "Devil", "Lightning", "Gun", "Rock", "Fire"], ["oxygenates", "destroys", "disintegrates", "stops", "muffles", "makes moss grow on", "puts out"]],
    "Water":[["Dragon", "Devil", "Lightning", "Gun", "Rock", "Fire", "Scissors"], ["drowns", "drowns", "dissipates", "jams", "puts out", "rusts"]],
    "Dragon":[["Devil", "Lightning", "Gun", "Rock", "Fire", "Scissors", "Snake"], ["sets fire to", "sets fire to", "sets fire to", "sets fire to", "sets fire to", "sets fire to""sets fire to"]],
    "Devil":[["Lightning", "Gun", "Rock", "Fire", "Scissors", "Snake", "Human"], ["ends", "removes", "vaporises", "cancels", "explodes", "kills", "kills"]],
    "Lightning":[["Gun", "Rock", "Fire", "Scissors", "Snake", "Human", "Tree"], ["electrocutes", "vaporises", "is", "cancels", "electrocutes", "electrocutes", "electrocutes"]],
    "Gun":[["Rock", "Fire", "Scissors", "Snake", "Human", "Tree", "Wolf"], ["shoots", "shoots", "shoots", "shoots", "shoots", "shoots", "shoots"]],
    "Rock":[["Fire", "Scissors", "Snake", "Human", "Tree", "Wolf", "Sponge"], ["crushes", "crushes", "crushes", "crushes", "crushes", "crushes", "crushes"]],
    "Fire":[["Scissors", "Snake", "Human", "Tree", "Wolf", "Sponge", "Paper"], ["sets fire to", "burns", "burns", "burns", "burns", "burns", "sets fire to"]],
    "Scissors":[["Snake", "Human", "Tree", "Wolf", "Sponge", "Paper", "Air"], ["cuts", "cuts", "cuts", "cuts", "cuts", "cuts", "cuts"]],
    "Snake":[["Human", "Tree", "Wolf", "Sponge", "Paper", "Air", "Water"], ["poisons", "poisons", "poisons", "poisons", "poisons", "poisons", "poisons"]],
}

def what_beats_what():
    keys = list(wins.keys())
    print("_________________\n")
    for n in range(len(wins[keys[0]][0])):
        for i in range(len(list(wins.keys()))):
            print(f"{keys[i]} {wins[keys[i]][1][n]} {wins[keys[i]][0][n]}")
    print("_________________\n")
mode = input("PvE or PvP: ")
while mode != "PvP" and mode != "PvE":
    mode = input("PvE or PvP: ")
    if mode == "PvE":
        break
    elif mode == "PvP":
        break


def parse_int(inputs, forbid, msgtosend, max=100000):
    if inputs.upper() == "Q": return "Q"
    if inputs.upper() == "L": return "L"
    try: 
        int(inputs)
        if int(inputs) <= max:
            if int(inputs) != forbid:
                return int(inputs)
            return parse_int(input(msgtosend), forbid, msgtosend, max)
        return parse_int(input(msgtosend), forbid, msgtosend, max)
    except: return parse_int(input(msgtosend), forbid, msgtosend, max)

def most_frequent(List, forbid):
    counter = 0
    num = List[0]
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency > counter):
            if i != forbid:
                counter = curr_frequency
                num = i
    return num

def bot_choice(list_of_choiced):
    if len(list_of_choiced) > 0: 
        modal = most_frequent(list_of_choiced, "")
        secondmost = most_frequent(list_of_choiced, modal)
        chosen = []
        for key in wins.keys():
            if modal in wins[key][0]:
                chosen.append(key)
        chosen1 = []
        for chose in chosen:
            if chose not in wins[secondmost][0]:
                chosen1.append(chose)
        if len(chosen1) > 0:
            return random.choice(chosen1)
        else:
            return random.choice(list(wins.keys()))
    else:
        return random.choice(list(wins.keys()))

def get_choice(name, hide=False):
    if not hide:
        for k in range(len(list(wins.keys()))):
            print(str(k + 1) + ". " + list(wins.keys())[k])
        print("_________________\n")
    choice = parse_int(input(f"{name} choice or [Q]uit. [L]ist moves to see what beats what: "), 0, f"{name} choice: ", len(list(wins.keys())))
    if str(choice).isalpha():
        return choice
    return list(wins.keys())[int(choice) - 1]
def calwin(p1, p2, p1score, p2score):
    if p2 in wins[p1][0]:
        print(f"{p1} {wins[p1][1][wins[p1][0].index(p2)]} {p2}")
        print("Player 1 wins!")
        return p1score + 1, p2score
    elif p1 in wins[p2][0]:
        print(f"{p2} {wins[p2][1][wins[p2][0].index(p1)]} {p1}")
        if mode == "PvP": print("Player 2 wins")
        else: print("Computer wins!")
        return p1score, p2score + 1
    elif p1 == p2:
        print(random.choice(tienames))
        return p1score, p2score

def ptc():
    input("Press Enter to continue") 

number_to_win = parse_int(input("Points to win: "), 0, "Points to win: ", 100000)
print(number_to_win)
end = False
listofchoose = []
p1score, p2score = 0, 0
chosen, chosen1, chosen2 = 0, 0, 0
print(f"First to {number_to_win} wins!")
while 1 > 0:
    if mode == "PvE":
        chosen = get_choice("Player 1")
        if chosen == "Q": break
        if chosen == "L": 
            what_beats_what()
            chosen = get_choice("Player 1", True)
        aichoose = bot_choice(listofchoose)
        listofchoose.append(chosen)
        p1score, p2score = calwin(chosen, aichoose, p1score, p2score)
        print(f"P:E\n{p1score}:{p2score}")
        if p1score >= number_to_win or p2score >= number_to_win:
            if p1score >= number_to_win:
                print("Player wins in OVERALL!")
                break
            else:
                print("Computer wins in OVERALL!")
                break
        ptc()
    else:
        chosen1 = get_choice("Player 1")
        if chosen1 == "Q": break
        if chosen1 == "L": 
            what_beats_what()
            chosen1 = get_choice("Player 1", True)
        chosen2 = get_choice("Player 2")
        if chosen2 == "Q": break
        if chosen2 == "L": 
            what_beats_what()
            chosen2 = get_choice("Player 2", True)
        p1score, p2score = calwin(chosen1, chosen2, p1score, p2score)
        print(f"P1:P2\n{p1score}:{p2score}")
        if p1score >= number_to_win or p2score >= number_to_win:
            if p1score >= number_to_win:
                print("Player 1 wins in OVERALL!")
                break
            else:
                print("Player 2 wins in OVERALL!")
                break
        ptc()
    print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nP:E\n{p1score}:{p2score}\nRock Paper Lizard Scissors Spock\n_________________\n")
if chosen == "Q" or chosen1 == "Q" or chosen2 == "Q":
    print("\n\n_________________\n")
    ErrorReason = "Choice, Player Quit. \n_________________\n\nEnd of Player, End Simulation.\nStart Sembiance, Begin new round. Locating players ... Please hold"
    raise KeyboardInterrupt("Quit: " + ErrorReason)
    print("hi")
else:
    print("\nExit, END")
    quit()