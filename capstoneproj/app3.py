################################
##### MUD CAPSTONE PROJECT #####
################################
'''
COMMENT FORMAT:

NOTE: 

###################################
#### THIS IS A LEVEL 4 COMMENT ####
###################################

#################################
### THIS IS A LEVEL 3 COMMENT ###
#################################

###############################
## THIS IS A LEVEL 2 COMMENT ##
###############################

#############################
# THIS IS A LEVEL 1 COMMENT #
#############################

# THIS IS A REGULAR COMMENT FOR REFERENCES


You can split the code into a list based on this.

e.g

Level 4 comment
    Level 3 comment
        Level 2 comment
            Level 1 comment
            Level 1 comment
    Level 3 comment
        Level 2 comment
        Level 2 comment
Level 4 comment
    Level 3 comment
        Level 2 comment
'''



##################
#### IMPORTS #####
##################
try: from devkey import *
except: print("Devkey not installed.")
import random, time
###################
#### CONSTANTS ####
###################

################
###  WEAPONS ###
################
# WEAPONS ( For Player )
# Key: [mindmg, maxdmg, [Phrases for basic attack], {special ablity:[[mindmg, maxdmg], cooldown, desc]}, name]
pweapons = {
    "hard fist":[6,10, ["hit", "punch"], {"Iron Punch":[[20,50], 2, "A literal punch of iron"]}, 0.1,"hard fist"],
    "hard kick":[6,10, ["kick", "540 kick"], {"Tornado Kick":[[0, 75], 3, "A powerful kick that is completedly based on luck"]}, 0.3, "hard kick"],
    "hammer":[10, 20, ["smash", "whack"], {"Hammer Smash":[[9,10], 2, "A perfectly balanced strike"]}, 0.5,"hammer"],
    "lightsword":[6, 30, ["slice", "cut through"], {"Lightsword Throw":[[0,75], 2, "If it lands it can deal HEAVY damage"]}, 1, "Lightsword"],
    "god sword":[6, 50, ["eviscerate", "absolutely CRUSH"], {"Godly Slice":[[9,10], 2, "I had to nerf this weapon somehow"]}, 1.3, "God Sword"],
    "katana": [5, 15, ["slash", "quick strike"], {"Razor Edge":[[15, 30], 2, "A swift, precise strike with the sharpest edge of the blade"]}, 0.5, "Katana"],
    "spear": [6, 10, ["thrust", "impale"], {"Javelin Throw":[[10, 20], 3, "A long-range attack that deals heavy damage"]}, 0.3, "Spear"],
    "dagger":[6, 12, ["stab", "sneak attack"], {"Assassin's Strike":[[7, 15], 2, "A quick and deadly strike from the shadows"]}, 0.2, "Dagger"],
    "axe": [6, 12, ["chop", "cleave"], {"Warrior's Fury":[[12, 20], 3, "A devastating blow that unleashes the warrior's rage"]}, 0.2, "Axe"],
    "blunt weapon": [6, 8, ["bash", "smash"], {"Head-Cracker":[[10, 15], 2, "A powerful blow that stuns the opponent"]}, 0.2, "Blunt Weapon"],
    "scythe": [8, 16, ["reap", "mow down"], {"Harvest Time":[[18, 25], 3, "A sweeping attack that cuts down multiple enemies"]}, 0.2, "Scythe"],
    "crossbow": [4, 10, ["fire", "bolt"], {"Sniper Shot":[[12, 20], 4, "A precise shot that deals heavy damage from a distance"]}, 0.2, "Crossbow"],
    "staff": [2, 6, ["smack", "whack"], {"Arcane Blast":[[10, 15], 3, "A blast of magical energy that deals moderate damage"]}, 0.2, "Staff"],
    "mace": [7, 14, ["crush", "smash"], {"Bone-Breaker":[[18, 25], 2, "A heavy blow that shatters the opponent's bones"]}, 0.2, "Mace"],
    "whip": [3, 7, ["lash", "whip"], {"Crack of Doom":[[10, 15], 2, "A loud crack that stuns the opponent"]}, 0.2, "Whip"],
    "halberd": [9, 18, ["chop", "impale"], {"Sky Piercer":[[20, 30], 3, "A powerful upward strike that impales the enemy"]}, 0.2, "Halberd"],
    "club": [5, 6, ["smack", "bash"], {"Stun":[[10, 15], 3, "Stuns the target, interrupting their actions"]}, 0.2, "Club"],
    "bow": [6, 7, ["shoot"], {"Arrow Volley":[[7, 8], 4, ""]}, 0.2, "Bow"],
    }
# WEAPONS ( Including creatures )
# Key: [mindmg, maxdmg, [Phrases for basic attack], {special ablity:[[mindmg, maxdmg], cooldown, desc]}, name]
weapons = {
    "hard fist":[6,10, ["hit", "punch"], {"Iron Punch":[[20,50], 2, "A literal punch of iron"]}, 0.1,"hard fist"],
    "hard kick":[6,10, ["kick", "540 kick"], {"Tornado Kick":[[0, 75], 3, "A powerful kick that is completedly based on luck"]}, 0.3, "hard kick"],
    "hammer":[10, 20, ["smash", "whack"], {"Hammer Smash":[[9,10], 2, "A perfectly balanced strike"]}, 0.5,"hammer"],
    "lightsword":[6, 30, ["slice", "cut through"], {"Lightsword Throw":[[0,75], 2, "If it lands it can deal HEAVY damage"]}, 1, "Lightsword"],
    "god sword":[6, 50, ["eviscerate", "absolutely CRUSH"], {"Godly Slice":[[9,10], 2, "I had to nerf this weapon somehow"]}, 1.3, "God Sword"],
    "katana": [5, 15, ["slash", "quick strike"], {"Razor Edge":[[15, 30], 2, "A swift, precise strike with the sharpest edge of the blade"]}, 0.5, "Katana"],
    "spear": [6, 10, ["thrust", "impale"], {"Javelin Throw":[[10, 20], 3, "A long-range attack that deals heavy damage"]}, 0.3, "Spear"],
    "dagger":[6, 12, ["stab", "sneak attack"], {"Assassin's Strike":[[7, 15], 2, "A quick and deadly strike from the shadows"]}, 0.2, "Dagger"],
    "axe": [6, 12, ["chop", "cleave"], {"Warrior's Fury":[[12, 20], 3, "A devastating blow that unleashes the warrior's rage"]}, 0.2, "Axe"],
    "blunt weapon": [6, 8, ["bash", "smash"], {"Head-Cracker":[[10, 15], 2, "A powerful blow that stuns the opponent"]}, 0.2, "Blunt Weapon"],
    "scythe": [8, 16, ["reap", "mow down"], {"Harvest Time":[[18, 25], 3, "A sweeping attack that cuts down multiple enemies"]}, 0.2, "Scythe"],
    "crossbow": [4, 10, ["fire", "bolt"], {"Sniper Shot":[[12, 20], 4, "A precise shot that deals heavy damage from a distance"]}, 0.2, "Crossbow"],
    "staff": [2, 6, ["smack", "whack"], {"Arcane Blast":[[10, 15], 3, "A blast of magical energy that deals moderate damage"]}, 0.2, "Staff"],
    "mace": [7, 14, ["crush", "smash"], {"Bone-Breaker":[[18, 25], 2, "A heavy blow that shatters the opponent's bones"]}, 0.2, "Mace"],
    "whip": [3, 7, ["lash", "whip"], {"Crack of Doom":[[10, 15], 2, "A loud crack that stuns the opponent"]}, 0.2, "Whip"],
    "halberd": [9, 18, ["chop", "impale"], {"Sky Piercer":[[20, 30], 3, "A powerful upward strike that impales the enemy"]}, 0.2, "Halberd"],
    "club": [5, 6, ["smack", "bash"], {"Stun":[[10, 15], 3, "Stuns the target, interrupting their actions"]}, 0.2, "Club"],
    "bow": [6, 7, ["shoot"], {"Arrow Volley":[[7, 8], 4, ""]}, 0.2, "Bow"],
    "poisonous fangs":[5, 2, ["bite"], {"Poison":[[2, 5], 2, "Injects a deadly poison"]}, 0.2, "Poisonous Fangs"],
    "poisonous bite":[5, 2, ["bite"], {"Poison":[[2, 5], 2, "Injects a deadly poison"]}, 0.2, "Poisonous Bite"],
    "maul": [8, 10, ["smash"], {"Crush":[[15, 25], 5, "A powerful blow that crushes the target"]}, 0.2, "Maul"],
    "claws":[1, 3, ["scratch", "peel at"], {"Deep Cut":[[5, 10], 2, "Causes a pretty deep cut"]}, 0.2, "Claws"], 
    "giant claws":[10, 20, ["shred", "cut through"], {"Disembowel":[[10, 20], 4, "Well this is the only way to kill a Skull Crawler"]}, 0.3, "Giant Claws"],
}

###############
### ENEMIES ###
###############

# CONTAINS INFORMATION ABOUT THE ENEMIES

# Format:
# "ENEMY NAME":["ENEMY WEAPON", "ENEMY HEALTH"]
enemies = {
    "bat": ["claws", 100],
    "giant bat": ["giant claws", 150],
    "cave bear": ["giant claws", 200],
    "spider": ["poisonous fangs", 75],
    "snake": ["poisonous bite", 50],
    "orc": ["maul", 150],
    "troll": ["club", 200],
    "goblin": ["dagger", 75],
    "wizard": ["staff", 150],
    "wizard mirrors":["staff", 20],
    "guardian of the treasure":["staff", 1000]
}

#############
### WAVES ###
#############

# FORMAT:
# [[QUANTITY OF TYPE 1 ENEMY, "TYPE 1 ENEMY NAME"], [QUANTITY OF TYPE 2 ENEMY, "TYPE 2 ENEMY NAME]], .ETC
waves = [
    [[2, "bat"]],
    [[3, "bat"]],
    [[1, "giant bat"]],
    [[3, "bat"], [1, "cave bear"]],
    [[1, "giant bat"], [2, "cave bear"], [3, "bat"]],
    [[1, "goblin"]],
    [[3, "orc"], [4, "troll"]],
    [[1, "wizard"]],
    [[3, "wizard"]],
    [[1, "wizard"]],
    [[10, "wizard mirrors"]],
    [[1, "guardian of the treasure"]],
]
# DESCRIPTION OF WAVES
wavesdesc = [
    "You approach the cave with apprehension. As you enter it, 2 bats suddenly jump at you!",
    "You make quick work of the bats and move further in. Suddenly, the bats behind you came at you again. Confused, you spun around, to find out that they came back to life, and felt another bat come charging at you from behind!",
    "Just as you think you've defeated the bats, the ground beneath you begins to shake, and a massive bat, twice the size of any you've seen before, emerges from the shadows.",
    "The battle with the giant bat is intense, but you eventually defeat it with a well-placed strike. Panting and covered in bat blood, you lean against a wall to catch your breath. That's when you notice a narrow passage leading deeper into the cave. Curiosity getting the better of you, you decide to explore the passage. It leads you to a large chamber, filled with glittering treasure! As you reach out to grab a golden amulet, you hear a low growl. You spin around to find yourself face to face with a fierce cave bear and some bats, guarding the treasure.",
    "Finally, with a fierce roar, the bear and bats collapse. You take a moment to catch your breath and then turn your attention back to the treasure. As you begin to gather up the gold and gems, you hear a shuffling noise behind you. You spin around to find the giant bat, a few more cave bears, and some bats, reanimated by the power of the treasure, lunging towards you.",
    """You fight your way through the them, using your and strength to outmaneuver them. Finally, you reach the far wall of the chamber, where you find a mysterious door. You push the door open, and as the light from the treasure chamber spills in, you see a figure waiting for you on the other side. It's the guardian of the treasure, a powerful wizard who has been watching your progress with interest. "Welcome, brave adventurer," the wizard says with a smile. 'You have proven yourself worthy of the treasure. But the true test is yet to come.' Suddenly he disappeares, and in his place, a goblin appears""",
    "Dispatching the goblin, you move through a tunnel illuminated my glittering crystals, eventually entering an arena. Betrayed, you spin around, to see that the tunnel had closen up. Spinning back to the front, you see some orcs and trolls brawling if each other. Sighing, you charge at them.",
    "With all of them defeated, you charge up to the stands, where you see the wizard watching. He treis to run, but you quickly catch up to him and tackle him to the ground.",
    "You kick the wizard to the floor and look up. As it turned out, dozens of wizards were there, cowering. A few brave wizards stepped forward to avenge their fallen comrade.",
    "'YOU FOOL!' A thunderous voice said. Looking up, it was the original wizard who you saw. He charged at you.",
    "He was panting on the ground. But when you moved closer to him, he suddenly duplicated himself into several mirrors.",
    "Defeating all of his mirrors, you look at him, with him floating in his full power. 'I ... will ... avenge ... MY BROTHERS!!!' He yelling, flying at you." 
]

########################
### PLAYER VARIABLES ###
########################

# STARTING VALUES
stre, inte, life = 5, 5, 5

###################
#### FUNCTIONS ####
###################

##############################
### MODIFY STARTING VALUES ###
##############################

def modify_start_vals(streintelife, streintelifevals, minvals):
    modvals = streintelifevals.copy()
    tempmodvals = modvals.copy()
    while True:
        print("\n_________________\n\n")
        for value in range(len(streintelife)):
            print(f"{value + 1}: {streintelife[value]} = {modvals[value]}")
        print("Strength affects the damage of the basic attack (lower minimum and higher maximum damage of basic attack)\n")
        print("Intelligence affects the damage of the secondary attack and the special ability (lower minimum and higher maximum damage of secondary attack)")
        print("Life affects the amount healed every time you heal, and increases the chance for higher damage (increases minimum damage)\n\n")
        print("Type the value to change in the following format:\n{value to change}{space}{amount to change}{space}{value to bring the point to}")
        print("E.g. If you want to bring 1 point from Strength to Intelligence, enter {1 1 2}")
        print("E.g. If you want to bring 3 points from Strength to Life, enter {1 3 3}")
        values = input("Enter values or [C]ontinue to game: ")
        if values.upper() == "C":
            break
        while True:
            try:
                amount_to_change_from, amount_to_change, amount_to_change_to = list(map(int, values.split()))
                tempmodvals[amount_to_change_from - 1] -= amount_to_change
                tempmodvals[amount_to_change_to - 1] += amount_to_change
                for modval in tempmodvals:
                    if modval < minvals:
                        print(modval, minvals)
                        print(f"Value cannot be less than {minvals}")
                        raise ValueError()
            except:
                values = input("Enter values or [C]ontinue to game: ")
            else:
                break
            if values.upper() == "C":
                break
        modvals = tempmodvals
        
    

########################
### INPUT VALIDATION ###
########################

def parse_int(sentin, maxint=2000000000, forbid=0):
        try:
            if sentin.upper() == "Q": raise KeyboardInterrupt()
            int(sentin)
            if int(sentin) <= maxint:
                if int(sentin) != forbid:
                    return True
                else:
                    return False
            else:
                return False
        except:
            return False

################################
### LEVEL UP INCREASE VALUES ###
################################

def lvlup(str, inte, life):
    stats = [str, inte, life]
    print("Level up!")
    print("1. Current strength: ", str)
    print("2. Current intelligence ", inte)
    print("3. Current life: ", life)
    print("Strength affects power of regular attacks.\nIntelligence affects power of special abilities.\nLife increases amount of health you get back every time you heal.")
    chosenincr = input("Choose 1 stat to level up (number): ")
    while not parse_int(chosenincr, 3):
        chosenincr = input("Choose 1 stat to level up (number): ")
    incr = int(chosenincr)
    stats[incr-1] += 1
    return tuple(stats)

###############################
### PRESS ENTER TO CONTINUE ###
###############################
def ptc():
    input("Press Enter to Continue")
    print()

##########################
### SENDING GAME WAVES ###
##########################

def sendwave(wave, name, str, inte, life, weapon):
    currenttime = 0
    hplayers = []
    hplayers.append(Player(name, str, inte, life, weapon))
    print(f"Wave: {wave}")
    print("\n" + wavesdesc[wave-1])
    ptc()
    creatures = []
    wavecreatures = waves[wave-1]
    for wavecreature in wavecreatures:
        for i in range(wavecreature[0]):
            creatures.append([f"{wavecreature[1].title()} {i + 1}", wavecreature[1]])
    cplayers = []
    for cplayer in creatures:
        cplayers.append(Computer(cplayer[0], enemies[cplayer[1]][0], enemies[cplayer[1]][1]))

    totalplayers = hplayers + cplayers
    totalorderedplayers = hplayers + cplayers
    random.shuffle(totalplayers)

    ####################
    ## DEALING DAMAGE ##
    ####################

    def dealdmg(whoatk, target, player_type):
        abilityname = list(target[0].abilities.values())[target[2]-1][-1]
        damage_reduced = False
        dmgtaken = max(1, random.randint(target[1][0], target[1][1]))
        for buff in target[0].buffs:
            if "def up" in buff:
                dmgtaken = int(dmgtaken * buff[1])
                damage_reduced = True
                target[0].buffs.pop(target[0].buffs.index(buff))
        if abilityname == "Tank up":
            ans = f"{whoatk.name} used {abilityname} on {target[0].name}!!!"
            print(ans)
            whoatk.buffs.append(["def up", 0.5])
            return
        if abilityname == "Basic Attack (based on Strength)" or abilityname == "Secondary attack (based on Intelligence)":
            target[0].health -= dmgtaken
            ans = f"{whoatk.name} used {whoatk.weapon.title()} to {random.choice(weapons[whoatk.weapon][2])} {target[0].name}, dealing {dmgtaken} damage!"
            print(ans)
            print("")
        else:
            ans = f"{whoatk.name} used {abilityname} on {target[0].name}!!!"
            print(ans)
            if dmgtaken < 0:
                ans = f"{whoatk.name}'s {abilityname} healed {dmgtaken * -1}HP!"
                print(ans)
            else:
                ans = f"{whoatk.name}'s {abilityname} dealt {dmgtaken} Damage!"
                print(ans)
            print("")
            target[0].health -= dmgtaken
        if damage_reduced:
            print(f"Because of Defence up, damage was reduced from {dmgtaken * 2} to {dmgtaken}")
        if target[0].health <= 0:
            totalorderedplayers.pop(totalorderedplayers.index(target[0]))
            totalplayers.pop(totalplayers.index(target[0]))
            print(target[0].name, "has died!")
            print("")

    ##################
    ## AI FUNCTIONS ##
    ##################

    ############################
    # AI DECIDE ABILITY TO USE #
    ############################
        
    def AIdecide(player, canspec=False):
        if player.health <= 35:
            return (player, player.abilities["heal"][2], 4)
        elif player.health > 35 and len(player.buffs) < 1:
            return (player, player.abilities["defup"][2], 5)
        elif canspec and player.health > 35:
            return (AIdecidetarget(player, player.abilities["sabi"], 3))
        else:
            return random.choice((AIdecidetarget(player, player.abilities["batk"], 1)), (AIdecidetarget(player, player.abilities["batk2"], 2)))

    ############################
    # AI DECIDE ABILITY TARGET #
    ############################

    def AIdecidetarget(player, ability, abilityno):
        if len(totalorderedplayers) > 2:
            target = random.choice(totalorderedplayers)
            while target == player:
                target = random.choice(totalorderedplayers)
            return (target, ability[2], abilityno)
        else:
            if totalorderedplayers[0] == player:
                return (totalorderedplayers[1], ability[2], abilityno)
            else:
                return (totalorderedplayers[0], ability[2], abilityno)

    ##########################
    # PRINT PLAYER ABILITIES #
    ##########################

    def printabilities(player):
        for ability in range(len(list(player.abilities.keys()))):
            if ability != 2:
                print(f"{ability + 1}. {player.abilities[list(player.abilities.keys())[ability]][-1]}. {player.abilities[list(player.abilities.keys())[ability]][0]}")
            else:
                if player.canspec:
                    print(f"{ability + 1}. {player.abilities[list(player.abilities.keys())[ability]][-1]}. {player.abilities[list(player.abilities.keys())[ability]][0]}")
                else:
                    print(f"{ability + 1}. {player.abilities[list(player.abilities.keys())[ability]][-1]}. {player.abilities[list(player.abilities.keys())[ability]][0]}. Ability on cooldown! {player.turns % weapons[player.weapon][3][list(weapons[player.weapon][3].keys())[0]][1] + 1} turn(s) left!")
    
    ################################################
    # TESTS WEATHER SPECIAL ABILITY IS ON COOLDOWN #
    ################################################

    def testforspec(current, playerturn, playercooldown):
        if current:
            return True, 0
        else:
            if (playerturn) % playercooldown == 0:
                return True, 0
            else:
                return False, 1

    ####################
    # ACTUAL WAVE LOOP #
    ####################

    while len(totalplayers) > 1:
        for player in totalplayers:
                # IF CURRENT HEALTH IS MORE THAN ALLOWED MAXIMUM HEALTH
                if player.health > player.maxhealth:
                        player.health = player.maxhealth
                print(f"It is {player.name}'s Turn!!!") # PRINT PLAYER TURN
                print(f"{player.name} has {player.health}HP left!") # PRINT PLAYER REMAINING HEALTH
                print("") # NEW LINE
                if player.type == "human": # IF PLAYER IS CONTROLLED BY HUMAN
                    canspecresults = testforspec(player.canspec, player.turns, weapons[player.weapon][3][list(weapons[player.weapon][3].keys())[0]][1]) # GET WHETHER SPECIAL ABILITY IS ON COOLDOWN
                    player.canspec = canspecresults[0] # GET WHETHER SPECIAL ABILITY IS ON COOLDOWN
                    player.turns += canspecresults[1] # ADD TURNS
                    printabilities(player) # PRINT ABILITIES
                    chosenability = input("Choose your ability (number) or [Q]uit: ") # CHOOSE ABILITY
                    if player.canspec: # IF SPECIAL ABILITY IS AVAILABLE
                        while not parse_int(chosenability, 5): # INPUT VALIDATION -- OLD VERSION -- CHECK INPUT VALIDATION.PY FOR NEW ONE
                            chosenability = input("Choose your ability (number) or [Q]uit: ") # IF INPUT IS INVALID
                    else: # IF SPECIAL ABILITY IS NOT AVAILABLE
                        while not parse_int(chosenability, 5, 3): # INPUT VALIDATION -- OLD VERSION -- CHECK INPUT VALIDATION.PY FOR NEW ONE
                            chosenability = input("Choose your ability (number) or [Q]uit: ") # IF INPUT IS INVALID
                    ability = int(chosenability) # GET ABILITY INTEGER 
                    if ability != 4 and ability != 5: # IF ABILITY IS "OTHER" TARGET
                        for players in totalorderedplayers: # PRINT OUT POSSIBEL TARGETS
                            print(f"{totalorderedplayers.index(players) + 1}. {players.name} {'-' * (50 - len(player.name))} {players.health}HP")
                        
                        chosentarget = input("Choose who to attack (number): ") # CHOOSE TARGET
                        while not parse_int(chosentarget, len(totalplayers), totalorderedplayers.index(player) + 1): # INPUT VALIDATION -- OLD VERSION -- CHECK INPUT VALIDATION.PY FOR NEW ONE
                            chosentarget = input("Choose who to attack (number): ") # IF INPUT IS INVALID
                        chosentarget = totalorderedplayers[int(chosentarget) - 1] # GET TARGET <OBJECT> FROM PLAYER LIST
                    else: # TARGET IS SELF TYPE
                        chosentarget = player # SET TARGET TO PLAYER <OBJECT>
                    if ability == 3: # USING SPECIAL ABILITY
                        player.canspec = False
                        player.turns += 1
                    # TARGET FORMAT:
                    # (<OBJECT>, ABILITY NAME, ABILITY NUMBER)
                    target = (chosentarget, player.abilities[list(player.abilities.keys())[ability-1]][2], ability) #TUPLE FOR THE TARGET
                    dealdmg(player, target, player.type) # DEAL DAMAGE, OR HEAL, ETC.
                    ptc() # PRESS ENTER TO CONTINUE
                    if player.health > player.maxhealth: 
                        player.health = player.maxhealth # SET PLAYER HEALTH TO MAXHEALTH IF HEALTH IS GREATER THAN MAXHEALTH
                else: # IF PLAYER TYPE IS AI
                    print(f"{player.name} is choosing ... ") # PRINT CHOOSING
                    time.sleep(0.5) # SLOW DOWN TO INCREASE SURREALISM
                    canspecresults = testforspec(player.canspec, player.turns, weapons[player.weapon][3][list(weapons[player.weapon][3].keys())[0]][1]) # GET WHETHER SPECIAL ABILITY IS ON COOLDOWN
                    player.canspec = canspecresults[0] # GET WHETHER SPECIAL ABILITY IS ON COOLDOWN
                    player.turns += canspecresults[1] # ADD TURNS
                    target = AIdecide(player, player.canspec) # CHOOSE TARGET AND ABILITY
                    if target[-1] == 2: # IF ABILITY IS SPECIAL 
                        player.canspec = False # SET COOLDOWN TO TRUE
                        player.turns += 1 # ADD TURNS
                    dealdmg(player, target, player.type) # DEAL DAMAGE
                    ptc() # PRESS ENTER TO CONTINUE
        if hplayers[0] not in totalplayers: # IF PLAYER IS DEAD
            break # END GAME LOOP, TO CONTINUE TO LINE 360
    if hplayers[0] in totalplayers: # IF GAME ENDED WITH PLAYER STILL ALIVE
        return 1 # END WAVE, WITH WIN
    else: # IF GAME ENDED WITHOUT PLAYER STILL ALIVE
        print(f"You made it until wave {wave}") # PRINT WAVE NUMBER
        print("The story so far ...") # PRINT THE STORY
        for i in range(wave): # FOR EVERY WAVE SURVIVED
            print(wavesdesc[i]) # PRINT WAVE DESCRPTION
            print("\n") # NEW LINE
        return "no" # END WAVE, AS LOSS

########################
#### PLAYER CLASSES ####
########################

######################
### COMPUTER CLASS ###
######################

class Computer(object):
        def __init__(self, name, weapon, health):
            self.name = name
            self.speed = 0.5 + weapons[weapon][-2]
            self.maxhealth = health
            self.health = health
            self.weapon = weapon
            self.type = "AI"
            self.turns = 1
            self.canspec = False
            self.buffs = []
            self.specialabilities = weapons[self.weapon][3]["".join(weapons[self.weapon][3].keys())]
            self.abilities = {
            "batk":["A basic attack", "other", [weapons[self.weapon][0], weapons[self.weapon][1]], "Basic Attack (based on Strength)"],
            "batk2":["Secondary attack", "other", [weapons[self.weapon][0] - 5, weapons[self.weapon][1] + 5], "Secondary attack (based on Intelligence)"],
            "sabi":[self.specialabilities[-1], "other", [self.specialabilities[0][0], self.specialabilities[0][1]], "".join(weapons[self.weapon][3].keys())],
            "heal":["Healing, based on random", self, [-10, -5], "Breath of Life"],
            "defup":["Reduces damage taken the next turn by half", self, [1, 5], "Tank up"]
        }
            time.sleep(0.01)
            self.turns = 0

#################
## HUMAN CLASS ##
#################

class Player(object):
    def __init__(self, name, str, inte, life, weapon):
        self.name = name
        self.speed = 0.5 + weapons[weapon][-2]
        self.maxhealth = 1
        self.health = 1
        self.weapon = weapon
        self.type = "human"
        self.turns = 1
        self.canspec = False
        self.str = str
        self.life = life
        self.inte = inte
        self.buffs = []
        self.specialabilities = weapons[self.weapon][3]["".join(weapons[self.weapon][3].keys())]
        self.abilities = {
            "batk":["A basic attack", "other", [weapons[self.weapon][0] - int((self.str * max(0.25, (10 - self.life)/10))), weapons[self.weapon][1] + int(self.str * max(1, ((self.life)/10) + 1))], "Basic Attack (based on Strength)"],
            "batk2":["Secondary attack", "other", [weapons[self.weapon][0] + int((self.inte * max(0.25, (10 - self.life)/10))), weapons[self.weapon][1] + int(self.inte * max(1, ((self.life)/10) + 1))], "Secondary attack (based on Intelligence)"],
            "sabi":[self.specialabilities[-1], "other", [self.specialabilities[0][0] + self.inte, self.specialabilities[0][1] + self.inte], "".join(weapons[self.weapon][3].keys())],
            "heal":["Healing, based on random", self, [-10 - self.life, -5 - self.life], "Breath of Life"],
            "defup":["Reduces damage taken the next turn by half", self, [1, 5], "Tank up"]
        }

#######################
#### INTIALIZATION ####
#######################

###############
### PLAYERS ###
###############

#######################
## HUMAN PLAYER INIT ##
#######################

players = []
players.append(f"Player 1")
name = input(f"Player name: ")

#############################
# UNLOCK DEV WEAPONS IF DEV #
#############################

################################
# GRANT PLAYER THE DEV WEAPONS #
################################

print(list(decrypt_keystore().keys())[0])
try:
    if name in list(decrypt_keystore().keys()):
        # Sets name to dev name
        name = decrypt_keystore()[name][0] if int(input()) == 1 else decrypt_keystore()[name][1]
        # Grants dev weapons as a choice of weapon
        weapons["dev sword"] = [100, 200, ["kill"], {"SHREDDER":[[500, 1000], 2, "Instant kill"]}, -0.4, "Dev Sword"]
        weapons["dev bow"] = [300, 400, ["shoot", "pierce"], {"Rapid Fire":[[10000, 100000], 2, "You thought the dev sword's isntant kill wasn't enough? It is NOW!"]}, -0.4, "Dev Bow"]
        weapons["test weapon - no damage (special ability heals) - prolong game"] = [0, 0, ["agressively sit next to"], {"Touch of Life":[[-100, -50], 2, "Heals"]}, -0.4, "test weapon - no damage (special ability heals) - prolong game"]
        pweapons["dev sword"] = [100, 200, ["kill"], {"SHREDDER":[[500, 1000], 2, "Instant kill"]}, -0.4, "Dev Sword"]
        pweapons["dev bow"] = [300, 400, ["shoot", "pierce"], {"Rapid Fire":[[10000, 100000], 2, "You thought the dev sword's isntant kill wasn't enough? It is NOW!"]}, -0.4, "Dev Bow"]
        pweapons["test weapon - no damage (special ability heals) - prolong game"] = [0, 0, ["agressively sit next to"], {"Touch of Life":[[-100, -50], 2, "Heals"]}, -0.4, "test weapon - no damage (special ability heals) - prolong game"]
        print("Welcome, Dev")
except:
    pass

############################
# PRINTS WEAPONS TO CHOOSE #
############################

if len(players) > 0:
        for pweapon in range(len(list(pweapons.keys()))):
                print(pweapon + 1, end=" ")
                print(pweapons[list(pweapons.keys())[pweapon]][-1].title())

#################
# SELECT WEAPON #
#################
weaponint = input("Choose your weapon (number): ")
while not parse_int(weaponint, len(pweapons)):
    weaponint = input("Choose your weapon (number): ")
weapon = weapons[list(pweapons.keys())[int(weaponint) - 1]][-1].lower()
print(f"{name} chose {weapon}!")


############################
## MODIFY STARTING VALUES ##
############################

modify_start_vals(["Strength", "Intelligence", "Life"], [stre, inte, life], 3)

#################
## SENDS WAVES ##
#################

for wave in range(len(waves)):
    print()
    contyn = sendwave(wave+1, name, stre, inte, life, weapon)
    if contyn == "no":
        ErrorMessage = "Health less than 0.\n_______________________________________________________________\n\nPlayer is dead.\n_______________________________________________________________\n\nEnd Simulation\n________________________________________________________________\n"
        raise ValueError(ErrorMessage)
    else:
        newvals = lvlup(str, inte, life)
        str = newvals[0]
        inte = newvals[1]
        life = newvals[2]
        print("1. New strength: ", stre)
        print("2. New intelligence ", inte)
        print("3. New life: ", life)
        ptc()

print(f"You made it to the end!")
print("The story:")
for i in range(len(wavesdesc)):
    print(wavesdesc[i])
    print("\n")