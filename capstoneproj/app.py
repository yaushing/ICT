import random, time

weapons = {
    "hard fist":[1,5, ["hit", "punch"], "hard fist"],
    "hard kick":[1,5, ["kick", "540 kick"], "hard kick"],
    "hammer":[1, 10, ["smash", "whack"], "hammer"],
    "lightsaber":[0, 20, ["slice", "cut through"], "lightsaber"],
    "God Sword":[0, 50, ["eviscerate", "absolutely CRUSH"], "God Sword"]
}
def startround():
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
            self.weapon = weapons[random.choice(list(weapons.keys()))][-1]
            time.sleep(0.01)
            print(f"{self.name} chose {self.weapon}!")
    class Player(object):
        def __init__(self, name):
            self.name = input(f"{name} name: ")
            self.health = 100
            self.weapon = weapons[list(weapons.keys())[int(input("Choose your weapon (number): ")) - 1]][-1]
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
    def call_attack(player, weapon):
        dmg = random.randint(weapons[weapon][0], weapons[weapon][1]) 
        player.health -= dmg
        return player.health, dmg
    def printgame(whoattack, whodef):
        dmg = call_attack(whodef, whoattack.weapon)[1]
        print(f"{whoattack.name} used a {whoattack.weapon} to {random.choice(weapons[whoattack.weapon][2])} {whodef.name} for {dmg} Damage! ", end = "")
        if whodef.health > 0:
            print(f"{whodef.name} has {whodef.health}HP remaining.")
        else:
            print(f"{whoattack.name} has beaten {whodef.name} to the ground!!!")
            return whodef
        return
    for i in range(3):
        print(3 - i)
        time.sleep(1)
    print("Fight!")
    totalplayers = hplayers + cplayers
    while len(totalplayers) > 1:
        attacker = random.choice(totalplayers)
        defender = random.choice(totalplayers)
        while defender == attacker:
            defender = random.choice(totalplayers) 
        loser = printgame(attacker, defender)
        totalplayers.pop(totalplayers.index(loser)) if loser else print("", end="")
        time.sleep(0.1)
    print(f"{totalplayers[0].name} is the GRAND WINNERRRRRR!!!!!!!")
    playagain = input("Would you like to play again? (Y/N)")
    while playagain == "Y":
        startround()
startround()

