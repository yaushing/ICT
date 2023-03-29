################################
##### MUD CAPSTONE PROJECT #####
################################
'''
COMMENT FORMAT:

NOTE: `

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
    "mirror staff": [1, 3, ["smack", "whack"], {"Arcane Blast":[[5, 7.5], 3, "A blast of magical energy that deals moderate damage"]}, 0.2, "Mirror Staff"],
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
    "bat": ["claws", 25],
    "giant bat": ["giant claws", 50],
    "cave bear": ["giant claws", 100],
    "spider": ["poisonous fangs", 50],
    "snake": ["poisonous bite", 50],
    "orc": ["maul", 150],
    "troll": ["club", 50],
    "goblin": ["dagger", 75],
    "wizard": ["staff", 150],
    "wizard mirrors":["mirror staff", 10],
    "guardian of the treasure":["staff", 1000],
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
    [[1, "giant bat"], [1, "cave bear"], [1, "bat"]],
    [[1, "goblin"]],
    [[1, "orc"], [1, "troll"]],
    [[1, "wizard"]],
    [[3, "wizard"]],
    [[1, "wizard"]],
    [[1, "wizard mirrors"]],
    [[1, "guardian of the treasure"]],
]
# DESCRIPTION OF WAVES
wavesdesc = [
    "You approach the cave with apprehension. As you enter it, 2 bats suddenly jump at you!",
    "You make quick work of the bats and move further in. Suddenly, the bats behind you came at you again. Confused, you spin around, to find out that they came back to life, and felt another bat come charging at you from behind!",
    "Just as you think you've defeated the bats, the ground beneath you begins to shake, and a massive bat, twice the size of any you've seen before, emerges from the shadows.",
    "The battle with the giant bat is intense, but you eventually defeat it with a well-placed strike. Panting and covered in bat blood, you lean against a wall to catch your breath. That's when you notice a narrow passage leading deeper into the cave. Curiosity getting the better of you, you decide to explore the passage. It leads you to a large chamber, filled with glittering treasure! As you reach out to grab a golden amulet, you hear a low growl. You spin around to find yourself face to face with a fierce cave bear and some bats, guarding the treasure.",
    "Finally, with a fierce roar, the bear and bats collapse. You take a moment to catch your breath and then turn your attention back to the treasure. As you begin to gather up the gold and gems, you hear a shuffling noise behind you. You spin around to find the giant bat, a few more cave bears, and some bats, reanimated by the power of the treasure, lunging towards you.",
    """You fight your way through the them, using your and strength to outmaneuver them. Finally, you reach the far wall of the chamber, where you find a mysterious door. You push the door open, and as the light from the treasure chamber spills in, you see a figure waiting for you on the other side. It's the guardian of the treasure, a powerful wizard who has been watching your progress with interest. "Welcome, brave adventurer," the wizard says with a smile. 'You have proven yourself worthy of the treasure. But the true test is yet to come.' Suddenly he disappeares, and in his place, a goblin appears""",
    "Dispatching the goblin, you move through a tunnel illuminated my glittering crystals, eventually entering an arena. Betrayed, you spin around, to see that the tunnel had closen up. Spinning back to the front, you see some orcs and trolls brawling if each other. Sighing, you charge at them.",
    "With all of them defeated, you charge up to the stands, where you see the wizard watching. He tries to run, but you quickly catch up to him and tackle him to the ground.",
    "You kick the wizard to the floor and look up. As it turned out, dozens of wizards were there, cowering. A few brave wizards stepped forward to avenge their fallen comrade.",
    "'YOU FOOL!' A thunderous voice said. Looking up, it was the original wizard who you saw. He charged at you.",
    "He was panting on the ground. But when you moved closer to him, he suddenly duplicated himself into several mirrors.",
    "Defeating all of his mirrors, you look at him, with him floating in his full power. 'I ... will ... avenge ... MY BROTHERS!!!' He yelling, flying at you." ,
]

########################
### PLAYER VARIABLES ###
########################

# STARTING VALUES
stre, inte, life = 5, 5, 5

###################
#### FUNCTIONS ####
###################

#################################
### MODIFY START OF ABILITIES ###
#################################
def get_abilities(new_abilities):
    new_modified_abilities = new_abilities.copy()
    possible_new_abilities = ["clearall", "accdown", "defdown", "offdown", "offup", "critchanceup", "critchancedown", "critdmgup", "critdmgdown"]
    possible_new_abilities_dict = {
        "clearall":["Clear head", r"Remove all buffs and debuffs from self, then gain 10% offense for each buff or debuff cleared."],
        "defdown":["Blur", r"Reduce defense of target enemy by 10%."],
        "offup":["Sweeping Strikes", r"Increase damage of self by 50% with a 10% chance to increase it by 100%"],
        "offdown":["Blur", r"Decrease damage of enemy by 50% with a 10% chance to decrease it by 75%"],
        "critchanceup":["Focus Strikes", r"Increase critical chance of self by 10%"],
        "critchancedown":["<Create Name>", r"Decrease critical chance of enemy by 5%"],
        "critdmgup":["<Create Name>", r"Increase critical damage of self by 10% with a 10% chance to increase it by 20%"],
        "critdmgdown":["<Create Name>", r"Decrease critical damage of enemty by 5% with a 10% chance to decrease it by 10%"],
        "accdown":["<Create Name>", r"Decrease accuracy of enemy by 25%, i.e. the enemy has a 25% chance to miss it's next attack"]
    }
    for ability in new_abilities:
        if ability in possible_new_abilities:
            possible_new_abilities.pop(possible_new_abilities.index(ability))
    printed_abilities = random.sample(possible_new_abilities, 3)
    for i in range(3):
        print(f"{i+1}. {possible_new_abilities_dict[printed_abilities[i]][0]}: {possible_new_abilities_dict[printed_abilities[i]][1]}")
    offensive_ability_no = 3
    defensive_ability_no = 2
    for ability in new_modified_abilities:
        offensive_ability_no += 1
    #for abi
    new_ability_int = parse_int(f"Choose a new ability (number). You currently have {offensive_ability_no} offensive and {defensive_ability_no} defensive abilities: ", 3)
    new_modified_abilities.append(printed_abilities[new_ability_int - 1])
    possible_new_abilities.pop(possible_new_abilities.index(printed_abilities[new_ability_int - 1]))
    return new_modified_abilities

##################
### LIST STATS ###
##################

def list_stats(player):
    for buff in player.buffs:
        print(buff)

##############################
### MODIFY STARTING VALUES ###
##############################

def modify_start_vals(streintelife, streintelifevals, minvals):
    modvals = streintelifevals.copy()
    tempmodvals = modvals.copy()
    flag_break = False
    while True:
        if flag_break:
            break
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
                flag_break = True
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
                        tempmodvals[amount_to_change_from - 1] += amount_to_change
                        tempmodvals[amount_to_change_to - 1] -= amount_to_change
                        raise ValueError()
            except:
                values = input("Enter values or [C]ontinue to game: ")
                
            else:
                break
            if values.upper() == "C":
                flag_break = True
                break 
        modvals = tempmodvals
        
    

########################
### INPUT VALIDATION ###
########################

def parse_int(msg, Max = 10000000, Min = 0, forbid = 0, exceptions = []):
    input_amt = input(msg)
    try:
        if input_amt in exceptions:
            return input_amt
        int(input_amt)
        if int(input_amt) > Max or int(input_amt) < Min:
            raise ValueError()
        if int(input_amt) == forbid:
            raise ValueError()
        return int(input_amt)
    except:
        return parse_int(msg, Max, Min, forbid, exceptions)


################################
### LEVEL UP INCREASE VALUES ###
################################

def lvlup(stre, inte, life):
    stats = [stre, inte, life]
    print("Level up!")
    print("1. Current strength: ", stre)
    print("2. Current intelligence ", inte)
    print("3. Current life: ", life)
    print("Strength affects power of regular attacks.\nIntelligence affects power of special abilities.\nLife increases amount of health you get back every time you heal.")
    incr = parse_int("Choose 1 stat to level up (number): ", 3)
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

def sendwave(wave, name, str, inte, life, weapon, abilities):
    hplayers = []
    hplayers.append(Player(name, str, inte, life, weapon, abilities))
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

    def dealdmg(whoatk, target):
        abilityname = list(whoatk.abilities.values())[target[2]-1][-1]
        msg = ""
        if abilityname != "Breath of Life":
            dmgtaken = max(1, random.randint(target[1][0], target[1][1]))  
        else: dmgtaken = random.randint(target[1][0], target[1][1])
        whoatk.stats["critchance"] = max(1, whoatk.stats["critchance"])
        whoatk.stats["critdmg"] = max(1, whoatk.stats["critdmg"])
        whoatk.stats["off"] = max(0.1, whoatk.stats["off"])
        if random.randint(0, 100) > whoatk.stats["acc"]:
            msg += "Accuracy down made the attack MISS!"
            whoatk.stats["acc"] = 100
            print(msg)
            return
        ability = list(whoatk.abilities.values())[target[2]-1]
        if ability[-3] == "Buff" and "up" in list(whoatk.abilities.keys())[list(whoatk.abilities.values()).index(ability)]:
            crit = random.randint(1, 10)
            whoatk.buffs.append([ability[-4][0], ability[-4][1][0]]) if crit < 10 else whoatk.buffs.append([ability[-4][0], ability[-4][1][1]])
            whoatk.stats[ability[-4][0]] += ability[-4][1][0] if crit < 10 else ability[-4][1][1]
            whoatk.stats["def"] = min(1, whoatk.stats["def"])
        elif ability[-3] == "Buff" and "down" in list(whoatk.abilities.keys())[list(whoatk.abilities.values()).index(ability)]:
            crit = random.randint(1, 10)
            target[0].buffs.append([ability[-4][0], ability[-4][1][0]]) if crit < 10 else whoatk.buffs.append([ability[-4][0], ability[-4][1][1]])
            target[0].stats[ability[-4][0]] += ability[-4][1][0] if crit < 10 else ability[-4][1][1]
            print(target[0].stats, target[0].buffs)
        elif ability[-3] == "Buff" and "clear" in  list(whoatk.abilities.keys())[list(whoatk.abilities.values()).index(ability)]:
            cleared_buffs = 0
            for _ in range(len(whoatk.buffs)):
                cleared_buffs += 1
            whoatk.stats["off"] = 1
            whoatk.stats["def"] = 0
            whoatk.stats["critchance"] = 10
            whoatk.stats["acc"] = 100
            whoatk.stats["critdmg"] = 1.5
            off_up_percent = 0.1 * cleared_buffs
            whoatk.stats["off"] += off_up_percent
            whoatk.buffs.append([["off"], 1 + off_up_percent])
        else:
            if random.randint(1, 100) < whoatk.stats["critchance"]:
                msg += "Critical Hit!\n"
                whoatk.stats["critchance"] = 10
                dmgtaken = dmgtaken * whoatk.stats["critdmg"]
                whoatk.stats["critdmg"] = 1.5
            dmgtaken = dmgtaken * whoatk.stats["off"]
            dmgtaken = dmgtaken * (1 - target[0].stats["def"])
            if whoatk.stats["off"] > 1:
                msg += "Offense up increased damage!\n"
                whoatk.stats["off"] = 1
            elif whoatk.stats["off"] < 1:
                msg += "Offense down decreased damage!\n"
                whoatk.stats["off"] = 1
            if target[0].stats["def"] > 0: 
                target[0].stats["def"] = 0
                msg += "Defense up reduced damage!\n"
            elif target[0].stats["def"] < 0:
                target[0].stats["def"] = 0
                msg += "Defense down increased damage!\n"
            if abilityname != "Breath of Life":
                dmgtaken = max(0.1, dmgtaken) 
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
                    target[0].health -= dmgtaken
                    print(ans)
                    return
                else:
                    ans = f"{whoatk.name}'s {abilityname} dealt {dmgtaken} Damage!"
                    print(ans)
                print("")
                target[0].health -= dmgtaken
        print(msg)
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
        buff_abilities = ["heal", "sabi", "defup", "clearall", "defdown", "offup", "offdown", "critchanceup", "critchancedown", "critdmgup", "critdmgdown", "accdown"]
        for ability in buff_abilities:
            if player.health <= (0.35 * player.maxhealth) and ability == "heal":
                return (player, player.abilities[ability][2], 3)
            elif canspec and ability == "sabi" and player.health > 0.35 * player.maxhealth:
                return AIdecidetarget(player, player.abilities[ability], 2)
            elif ability != "heal" and ability != "sabi" and random.randint(0, 100) <= 5:
                return AIdecidetarget(player, player.abilities[ability], list(player.abilities.keys()).index(ability))
        return AIdecidetarget(player, player.abilities["batk"], 1)

    ############################
    # AI DECIDE ABILITY TARGET #
    ############################

    def AIdecidetarget(player, ability, ability_number):
        if len(totalorderedplayers) > 2:
            target = random.choice(totalorderedplayers)
            while target == player:
                target = random.choice(totalorderedplayers)
            return (target, ability[2], ability_number)
        else:
            if totalorderedplayers[0] == player:
                return (totalorderedplayers[1], ability[2], ability_number)
            else:
                return (totalorderedplayers[0], ability[2], ability_number)

    ##########################
    # PRINT PLAYER ABILITIES #
    ##########################

    def list_buffs(player):
        for i in range(len(player.buffs)):
            print(f"{i+1}. {player.buffs[i]}")

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
    # TESTS WHETHER SPECIAL ABILITY IS ON COOLDOWN #
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
                player.buffs = []
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
                    while True:
                        if player.canspec: # IF SPECIAL ABILITY IS AVAILABLE
                            chosenability = parse_int("Choose your ability (number), [Q]uit or [L]ist buffs: ", 10000000, 0, 0, ["Q", "L"]) # CHOOSE ABILITY
                        else: # IF SPECIAL ABILITY IS NOT AVAILABLE
                            chosenability = parse_int("Choose your ability (number), [Q]uit or [L]ist buffs: ", 10000000, 0, 3, ["Q", "L"]) # CHOOSE ABILITY
                        if chosenability == "Q":
                            raise KeyboardInterrupt()
                        if chosenability == "L":
                            list_buffs(player)
                        else: break
                    ability = chosenability # GET ABILITY INTEGER 
                    if player.abilities[list(player.abilities.keys())[ability - 1]][1] == "other": # IF ABILITY IS "OTHER" TARGET
                        for players in totalorderedplayers: # PRINT OUT POSSIBLE TARGETS
                            print(f"{totalorderedplayers.index(players) + 1}. {players.name} {'-' * (50 - len(player.name))} {players.health}HP")
                        
                        chosentarget = parse_int("Choose who to attack (number): ", len(totalplayers), 0, 1) # CHOOSE TARGET
                        chosentarget = totalorderedplayers[chosentarget - 1] # GET TARGET <OBJECT> FROM PLAYER LIST
                    else: # TARGET IS SELF TYPE
                        chosentarget = player # SET TARGET TO PLAYER <OBJECT>
                    if ability == 3: # USING SPECIAL ABILITY
                        player.canspec = False
                        player.turns += 1
                    # TARGET FORMAT:
                    # (<OBJECT>, ABILITY NAME, ABILITY NUMBER)
                    target = (chosentarget, player.abilities[list(player.abilities.keys())[ability-1]][2], ability) #TUPLE FOR THE TARGET
                    dealdmg(player, target) # DEAL DAMAGE, OR HEAL, ETC.
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
                    dealdmg(player, target) # DEAL DAMAGE
                    ptc() # PRESS ENTER TO CONTINUE
        if hplayers[0] not in totalplayers: # IF PLAYER IS DEAD
            break # END GAME LOOP
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
            self.stats = {
                "def":0,
                "off":1,
                "acc":100,
                "critchance":10,
                "critdmg": 1.5,
            }
            self.specialabilities = weapons[self.weapon][3]["".join(weapons[self.weapon][3].keys())]
            self.abilities = {
            "batk":["A basic attack", "other", [weapons[self.weapon][0], weapons[self.weapon][1]], "Basic Attack (based on Strength)"],
            "sabi":[self.specialabilities[-1], "other", [self.specialabilities[0][0], self.specialabilities[0][1]], "".join(weapons[self.weapon][3].keys())],
            "heal":["Healing, based on random", self, [-10, -5], "Breath of Life"],
            "defup":[r"Damage taken next reduced by 50% with a 10% chance to take 0.1 damage", self, [1, 5], ["def", [0.5, 1]], "Buff", "Defensive", "Motivation"],
            "clearall":[r"Remove all buffs and debuffs from self, then gain 10% offense for each buff or debuff cleared.", self, [1, 5], ["CLEAR"], "Buff", "Offensive", "Clear head"],
            "defdown":[r"Reduce defense of target enemy by 10%.", "other", [1, 5], ["def", [-0.1, -0.1]], "Buff", "Offensive", "Blur"],
            "offup":[r"Increase damage of self by 50% with a 10% chance to increase it by 100%", self, [1, 5], ["off", [0.5, 1]], "Buff", "Offensive", "Sweeping Strikes"],
            "offdown":[r"Decrease damage of enemy by 50% with a 10% chance to decrease it by 75%", "other", [1, 5], ["off", [-0.5, -0.75]], "Buff", "Offensive", "Daze"],
            "critchanceup":[r"Increase critical chance of self by 10%", self, [1, 5], ["critchance", [10, 10]], "Buff", "Offensive", "Focus Strikes"],
            "critchancedown":[r"Decrease critical chance of enemy by 5%", "other", [1, 5], ["critchance", [-5, -5]], "Buff", "Offensive", "<Create Name>"],
            "critdmgup":[r"Increase critical damage of self by 10% with a 10% chance to increase it by 20%", self, [1, 5], ["critdmg", [0.1, 0.2]], "Buff", "Offensive", "<Create Name>"],
            "critdmgdown":[r"Decrease critical damage of enemty by 5% with a 10% chance to decrease it by 10%", self, [1, 5], ["critdmg", [-0.05, -0.1]], "Buff", "Offensive", "<Create Name>"],
            "accdown":[r"Decrease accuracy of enemy by 25%, i.e. the enemy has a 25% chance to miss it's next attack", self, [1, 5], ["acc", [-25, -25]], "Buff", "Offensive", "<Create Name>"],
        }
            time.sleep(0.01)
            self.turns = 0

#################
## HUMAN CLASS ##
#################

class Player(object):
    def __init__(self, name, str, inte, life, weapon, new_abilities):
        self.name = name
        self.speed = 0.5 + weapons[weapon][-2]
        self.maxhealth = 100
        self.health = 100
        self.weapon = weapon
        self.type = "human"
        self.turns = 1
        self.canspec = False
        self.str = str
        self.life = life
        self.inte = inte
        self.buffs = []
        self.stats = {
            "def":0,
            "off":1,
            "acc":100,
            "critchance":10,
            "critdmg": 1.5,
        }
        self.specialabilities = weapons[self.weapon][3]["".join(weapons[self.weapon][3].keys())]
        self.abilities = {
            "batk":["A basic attack", "other", [weapons[self.weapon][0] - int((self.str * max(0.25, (10 - self.life)/10))), weapons[self.weapon][1] + int(self.str * max(1, ((self.life)/10) + 1))], "Offensive", "Basic Attack (based on Strength)"],
            "batk2":["Secondary attack", "other", [weapons[self.weapon][0] + int((self.inte * max(0.25, (10 - self.life)/10))), weapons[self.weapon][1] + int(self.inte * max(1, ((self.life)/10) + 1))], "Offensive", "Secondary attack (based on Intelligence)"],
            "sabi":[self.specialabilities[-1], "other", [self.specialabilities[0][0] + self.inte, self.specialabilities[0][1] + self.inte], "Offensive", "".join(weapons[self.weapon][3].keys())],
            "heal":["Healing, based on random", self, [-10 - self.life, -5 - self.life], "Defensive", "Breath of Life"],
            "defup":[r"Damage taken next reduced by 50% with a 10% chance to take 0.1 damage", self, [1, 5], ["def", [0.5, 1]], "Buff", "Defensive", "Motivation"],
        }
        self.possible_abilities = {
            "clearall":[r"Remove all buffs and debuffs from self, then gain 10% offense for each buff or debuff cleared.", self, [1, 5], ["CLEAR"], "Buff", "Offensive", "Clear head"],
            "defdown":[r"Reduce defense of target enemy by 10%.", "other", [1, 5], ["def", [-0.1, -0.1]], "Buff", "Offensive", "Blur"],
            "offup":[r"Increase damage of self by 50% with a 10% chance to increase it by 100%", self, [1, 5], ["off", [0.5, 1]], "Buff", "Offensive", "Sweeping Strikes"],
            "offdown":[r"Decrease damage of enemy by 50% with a 10% chance to decrease it by 75%", "other", [1, 5], ["off", [-0.5, -0.75]], "Buff", "Offensive", "Daze"],
            "critchanceup":[r"Increase critical chance of self by 10%", self, [1, 5], ["critchance", [10, 10]], "Buff", "Offensive", "Focus Strikes"],
            "critchancedown":[r"Decrease critical chance of enemy by 5%", "other", [1, 5], ["critchance", [-5, -5]], "Buff", "Offensive", "<Create Name>"],
            "critdmgup":[r"Increase critical damage of self by 10% with a 10% chance to increase it by 20%", self, [1, 5], ["critdmg", [0.1, 0.2]], "Buff", "Offensive", "<Create Name>"],
            "critdmgdown":[r"Decrease critical damage of enemty by 5% with a 10% chance to decrease it by 10%", self, [1, 5], ["critdmg", [-0.05, -0.1]], "Buff", "Offensive", "<Create Name>"],
            "accdown":[r"Decrease accuracy of enemy by 25%, i.e. the enemy has a 25% chance to miss it's next attack", self, [1, 5], ["acc", [-25, -25]], "Buff", "Offensive", "<Create Name>"],
        }
        if len(new_abilities) > 0:
            for newability in new_abilities:
                self.abilities[newability] = self.possible_abilities[newability]

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

# Try-Except Block to check if name exists, and grant weapons to dev.
try:
    if name in list(decrypt_keystore().keys()):
        # Prompt user to select name
        name = decrypt_keystore()[name][0] if int(input("Name 1 or Name 2 (1/2)")) == 1 else decrypt_keystore()[name][1]
        # Add Dev Weapons to the dictionary
        weapons["dev sword"] = [100, 200, ["kill"], {"SHREDDER":[[500, 1000], 2, "Instant kill"]}, -0.4, "Dev Sword"]
        weapons["dev bow"] = [300, 400, ["shoot", "pierce"], {"Rapid Fire":[[10000, 100000], 2, "You thought the dev sword's instant kill wasn't enough? It is NOW!"]}, -0.4, "Dev Bow"]
        weapons["test weapon - no damage (special ability heals) - prolong game"] = [0, 0, ["aggressively sit next to"], {"Touch of Life":[[-100, -50], 2, "Heals"]}, -0.4, "test weapon - no damage (special ability heals) - prolong game"]
        # Add Dev Weapons to the player's weapon dictionary
        pweapons["dev sword"] = [100, 200, ["kill"], {"SHREDDER":[[500, 1000], 2, "Instant kill"]}, -0.4, "Dev Sword"]
        pweapons["dev bow"] = [300, 400, ["shoot", "pierce"], {"Rapid Fire":[[10000, 100000], 2, "You thought the dev sword's instant kill wasn't enough? It is NOW!"]}, -0.4, "Dev Bow"]
        pweapons["test weapon - no damage (special ability heals) - prolong game"] = [0, 0, ["aggressively sit next to"], {"Touch of Life":[[-100, -50], 2, "Heals"]}, -0.4, "test weapon - no damage (special ability heals) - prolong game"]
        # Greet the dev
        print("Welcome, Dev")
        wave_to_start = int(input("Wave: "))
except:
    wave=0
    pass

# Print weapons to choose from for players who exist in the game
if len(players) > 0:
        for pweapon in range(len(list(pweapons.keys()))):
                print(pweapon + 1, end=" ")
                print(pweapons[list(pweapons.keys())[pweapon]][-1].title())

# Allow players to select the weapon they want,
# using parse_int() function to validate user input
weaponint = parse_int("Choose your weapon (number): ", len(pweapons))
# Use user's selected weapon to display on screen
weapon = weapons[list(pweapons.keys())[int(weaponint) - 1]][-1].lower()
print(f"{name} chose {weapon}!")


############################
## MODIFY STARTING VALUES ##
############################

modify_start_vals(["Strength", "Intelligence", "Life"], [stre, inte, life], 3)

#################
## SENDS WAVES ##
#################
new_abilities = []# Comment Section –– Python Code

# Modify starting values based on the user's selection
modify_start_vals(["Strength", "Intelligence", "Life"], [stre, inte, life], 3)

# Send waves to fight against enemies and upgrade level if the player continues playing
new_abilities = []
new_ability_waves = [2, 3, 5, 11]
for wave in range(wave_to_start, len(waves)):
    print(f"Computiong: {wave}")
    print()
    # If current wave number is in new_ability_waves, add new abilities accordingly
    if (wave + 1) in new_ability_waves:
        new_abilities = get_abilities(new_abilities)
    # Send wave and get response back for simulation continuation
    contyn = sendwave(wave+1, name, stre, inte, life, weapon, new_abilities)
    # If player lose all their health during the battle,
    # raise a ValueError exception with error message
    if contyn == "no":
        ErrorMessage = "Health less than 0.\n_______________________________________________________________\n\nPlayer is dead.\n_______________________________________________________________\n\nEnd Simulation\n________________________________________________________________\n"
        raise ValueError(ErrorMessage)
    else:
        # Upgrade values for strength, intelligence, and life based on player's performance
        newvals = lvlup(stre, inte, life)
        stre = newvals[0]
        inte = newvals[1]
        life = newvals[2]
        # Display updated levels on screen
        print("1. New strength: ", stre)
        print("2. New intelligence ", inte)
        print("3. New life: ", life)
        ptc()

# Congratulate the player for completing the game and print a summary of the story on screen.
print(f"You made it to the end!")
print("The story:")
for i in range(len(wavesdesc)):
    print(wavesdesc[i])

