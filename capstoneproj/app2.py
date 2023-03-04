import random, time

#WEAPONS
# Key: [mindmg, maxdmg, [Phrases for basic attack], {special ablity:[[mindmg, maxdmg], cooldown, desc]}, name]
weapons = {
    "hard fist":[1,5, ["hit", "punch"], {"Iron Punch":[[20,50], 2, "A literal punch of iron"]},"hard fist"],
    "hard kick":[1,5, ["kick", "540 kick"], {"Tornado Kick":[[0, 75], 3, "A powerful kick that is completedly based on luck"]}, "hard kick"],
    "hammer":[1, 10, ["smash", "whack"], {"Hammer Smash":[[9,10], 2, "A perfectly balanced strike"]},"hammer"],
    "lightsword":[0, 20, ["slice", "cut through"], {"Lightsword Throw":[[0,75], 2, "If it lands it can deal HEAVY damage"]}, "Lightsword"],
    "god sword":[0, 50, ["eviscerate", "absolutely CRUSH"], {"Godly Slice":[[9,10], 2, "I had to nerf this weapon somehow"]}, "God Sword"],
    "fat":[10, 20, ["smack", "suffocate"], {"Heavy Smash":[[20, 30], 2, "Not really very strong"]}, "Fat"]
}



number_of_players = int(input("Number of human-controlled players: "))
number_of_computer = int(input("Number of computer-controlled players: "))
while number_of_players + number_of_computer < 2:
    print("Total number of players must be greater than 1.")
    number_of_computer = int(input("Number of computer-controlled players: "))
computers = []
for computer in range(number_of_computer):
    computers.append(f"A.I. {computer + 1}")
players = []
for player in range(number_of_players):
    players.append(f"Player {player + 1}")
class Computer(object):
        def __init__(self, name):
            self.name = name
            self.health = 100
            self.weapon = weapons[random.choice(list(weapons.keys()))][-1].lower()
            self.type = "AI"
            self.specialabilities = weapons[self.weapon][3]["".join(weapons[self.weapon][3].keys())]
            self.abilities = {
            "batk":["A basic attack", "other", [weapons[self.weapon][0], weapons[self.weapon][1]], "Basic Attack"],
            "sabi":[self.specialabilities[-1], "other", self.specialabilities[0], "".join(weapons[self.weapon][3].keys())],
            "heal":["Healing, based on random", self, [-10, -5], "Kiss of Nature"]
        }
            time.sleep(0.01)
            self.turns = 0
            print(f"{self.name} chose {self.weapon}!")
class Player(object):
    def __init__(self, name):
        self.name = input(f"{name} name: ")
        self.health = 100
        self.weapon = weapons[list(weapons.keys())[int(input("Choose your weapon (number): ")) - 1]][-1].lower()
        self.type = "human"
        self.turns = 0
        # ABILITIES
        # Key: [desc, target, -health, name]
        self.specialabilities = weapons[self.weapon][3]["".join(weapons[self.weapon][3].keys())]
        self.abilities = {
            "batk":["A basic attack", "other", [weapons[self.weapon][0], weapons[self.weapon][1]], "Basic Attack"],
            "batk2":["Secondary attack", "other", [weapons[self.weapon][0] + self.inte, weapons[self.weapon][1] + self.inte], "Secondary attack (based on Intelligence)"],
            "sabi":[self.specialabilities[-1], "other", self.specialabilities[0], "".join(weapons[self.weapon][3].keys())],
            "heal":["Healing, based on random", self, [-10, -5], "Kiss of Nature"],
        }
        print(f"{self.name} chose {self.weapon}!")
hplayers = []
cplayers = []
if len(players) > 0:
    for weapon in range(len(list(weapons.keys()))):
            print(weapon + 1, end=" ")
            print(weapons[list(weapons.keys())[weapon]][-1].title())
for player in players:
    hplayers.append(Player(player))
for cplayer in computers:
    cplayers.append(Computer(cplayer))
totalplayers = hplayers + cplayers
totalorderedplayers = hplayers + cplayers
random.shuffle(totalplayers)

def dealdmg(whoatk, abilityname, target):
    dmgtaken = random.randint(target[1][0], target[1][1])
    print(abilityname)
    if abilityname == "Basic Attack":
        target[0].health -= dmgtaken
        print(f"{whoatk.name} used {whoatk.weapon.title()} to {random.choice(weapons[whoatk.weapon][2])} {target[0].name} for {dmgtaken} damage!")
    else:
        print(f"{whoatk.name} used {abilityname}!")
        target[0].health -= dmgtaken
    if target[0].health <= 0:
        totalorderedplayers.pop(totalorderedplayers.index(target[0]))
        totalplayers.pop(totalplayers.index(target[0]))
        print(target[0].name, "has died!")

def AIdecide(player):
    if player.health <= 35:
        return (player, player.abilities["heal"][2])
    elif player.turns % player.specialabilities[1] == 0 and player.health > 35:
        return AIdecidetarget(player, player.abilities["sabi"])
    else:
        return AIdecidetarget(player, player.abilities["batk"])

def AIdecidetarget(player, ability):
    if len(totalorderedplayers) > 2:
        target = random.choice(totalorderedplayers)
        while target == player:
            target = random.choice(totalorderedplayers)
        return (target, ability[2])
    else:
        if totalorderedplayers[0] == player:
            return (totalorderedplayers[1], ability[2])
        else:
            return (totalorderedplayers[0], ability[2])

while len(totalorderedplayers) > 1:
    for player in totalorderedplayers:
        print(f"It is {player.name}'s Turn!")
        print(f"{player.name} has {player.health}HP left!")
        abilities = list(player.abilities.values())
        player.turns += 1
        if player.type == "human":
            print("Abilities: ")
            for i in range(len(abilities)):
                print(f"{i+1}. {abilities[i][-1]}", end=": ")
                if player.turns % player.specialabilities[1] != 0 and i == 1:
                    print(f"{abilities[i][0]}", end="")
                    print(f". Ability on Cooldown. {player.turns % player.specialabilities[1]} more turn(s) left")
                else:
                    print(f"{abilities[i][0]}")
            chosenability = input("\nChoose ability (number): ")
            while not chosenability.isnumeric():
                chosenability = input("Choose ability (number): ")
            chosenability = int(chosenability)
            while player.turns % player.specialabilities[1] != 0 and chosenability == 2:
                print("Ability on cooldown!")
                chosenability = input("Choose ability (number): ")
                while not chosenability.isnumeric():
                    chosenability = input("Choose ability (number): ")
                chosenability = int(chosenability)
            if list(player.abilities.values())[chosenability-1][1] == "other":
                if len(totalorderedplayers) > 2:
                    for i in range(len(totalorderedplayers)):
                        print(f"{i+1}. {totalorderedplayers[i].name}")
                    target1 = input("Who would you like to attack (number)? ")
                    if (target1.isnumeric() and int(target1) > len(totalorderedplayers)) or (not target1.isnumeric) or (target1.isnumeric() and totalorderedplayers[int(target1)-1] == player):
                        while (target1.isnumeric() and int(target1) > len(totalorderedplayers)) or (not target1.isnumeric) or (target1.isnumeric() and totalorderedplayers[int(target1)-1] == player):
                            target = input("Who would you like to attack (number)? ")
                    target = (totalorderedplayers[int(target1)-1], list(player.abilities.values())[chosenability-1][2])
                else:
                        if totalorderedplayers[0].name == player.name:
                            target = (totalorderedplayers[1], list(player.abilities.values())[chosenability-1][2])
                        else:
                            target = (totalorderedplayers[0], list(player.abilities.values())[chosenability-1][2])
            else:
                target = (player, list(player.abilities.values())[chosenability-1][2])
        else:
            print(f"{player.name} is choosing ... ")
            target = AIdecide(player)
        print(chosenability)
        dealdmg(player, list(player.abilities.values())[chosenability-1][-1], target)
        