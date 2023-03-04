import random
tienames = ["Tie!", "Tie! I hope this doesn't happen again.", "Tie! Please, make sure this game moves on.", "Draw."]
wins = {
    "Rock":[["Scissors", "Lizard"], ["crushes", "crushes"]],
    "Paper":[["Rock", "Spock"], ["covers", "disproves"]],
    "Lizard":[["Paper", "Spock"], ["eats", "poisons"]],
    "Scissors":[["Paper", "Lizard"], ["cuts", "decapitates"]],
    "Spock":[["Rock", "Scissors"], ["vaporises", "smashes"]],
}
mode = input("PvE or PvP: ")
while mode != "PvP" and mode != "PvE":
    mode = input("PvE or PvP: ")
    if mode == "PvE":
        break
    elif mode == "PvP":
        break


def parse_int(inputs, forbid, msgtosend, max=100000):
    if inputs.upper() == "Q": return "Q"
    try: 
        int(inputs)
        if int(inputs) <= max:
            if int(inputs) != forbid:
                return inputs
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

def get_choice(name):
    for k in range(len(list(wins.keys()))):
        print(str(k + 1) + ". " + list(wins.keys())[k])
    print("_________________\n")
    choice = parse_int(input(f"{name} choice or [Q]uit: "), 0, f"{name} choice: ", len(list(wins.keys())))
    if choice == "Q":
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
end = False
listofchoose = []
p1score, p2score = 0, 0
print(f"First to {number_to_win} wins!")
while 1 > 0:
    if mode == "PvE":
        chosen = get_choice("Player 1")
        if chosen == "Q": break
        aichoose = bot_choice(listofchoose)
        listofchoose.append(chosen)
        p1score, p2score = calwin(chosen, aichoose, p1score, p2score)
        print(f"P:E\n{p1score}:{p2score}")
        if p1score == number_to_win or p2score == number_to_win:
            if p1score == number_to_win:
                print("Player wins in OVERALL!")
                break
            else:
                print("Computer wins in OVERALL!")
                break
        ptc()
    else:
        chosen1 = get_choice("Player 1")
        if chosen1 == "Q": break
        chosen2 = get_choice("Player 2")
        if chosen2 == "Q": break
        p1score, p2score = calwin(chosen1, chosen2, p1score, p2score)
        print(f"P1:P2\n{p1score}:{p2score}")
        if p1score == number_to_win or p2score == number_to_win:
            if p1score == number_to_win:
                print("Player 1 wins in OVERALL!")
                break
            else:
                print("Player 2 wins in OVERALL!")
                break
        ptc()
    print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nP:E\n{p1score}:{p2score}\nRock Paper Lizard Scissors Spock\n_________________\n")
if chosen == "Q" or chosen1 == "Q" or chosen2 == "Q":
    print("\n\n")
    raise KeyboardInterrupt("Quit")
else:
    print("\nExit")
    quit()