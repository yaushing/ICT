
MUD Capstone Project


1. Details
This project is a multiplayer text-based adventure game, where players can create their characters, interact with non-player characters (NPCs), and fight against monsters and other players.

The project is composed of several modules, which are briefly explained below.
Modules
client.py: This module is responsible for handling the client-side of the game. It provides an interface for players to connect to the server, create their characters, and interact with the game world.

server.py: This module is responsible for handling the server-side of the game. It receives requests from clients and sends responses back, handles game logic, and manages the game world.

utils.py: This module contains utility functions used by both the client and server modules, such as functions to parse user input, handle messages, and manage game state.

game_data.py: This module contains data used by the game, such as information about monsters, items, and weapons.

2. Imports

Imports the devkey module, which contains the Keys of the developers, to allow for Developers to gain developer weapons, to test specific parts of the game.

Imports the random and time module, to run key functions of the game.
The random module is used to calculate the next move of the A.I. (Honestly I would have preferred it if this was Machine Learning but I don't code much so anyways) ~Tess

The time module used in the background to calculate the speed of the game and check speed of game functions.

3. Constants
3.1. Weapons
3.1.1. Player Weapons
The <pweapons> dictionary contains a list of 18 weapons that the player is allowed to choose from. It is important not to confuse this with the <weapons> dictionary (See 3.1.2).

Each weapon in the <pweapons> dictionary has its own set of attributes. These attributes include:

Damage Range: This is a range of damage that the weapon can deal, which is affected by strength, intelligence, life, (See 3.2) and buffs (See 3.3).
Attack Types: This is a list of attack types that the weapon can perform, such as "hit", "punch", "slice", "stab", and more.
Special Abilities: This is a dictionary of special abilities that the weapon possesses. Each special ability has a name, a damage range, a number of uses, and a description.
Weight: This is the weight of the weapon.
Name: This is the name of the weapon.

3.1.2. Weapons
<weapons> is a dictionary which contains the data for all weapons, whether player or enemy, containing damage, phrases for attacking, special abilities, etc. (Be. More. Specific.) ~Nova

3.2. Variables for the player.
There are four variable for the player. Should you make it more detailed, this can be extended much more.
1. Health
2. Strength
3. Intelligence
4. Life

Extended variables:
1. Health
2. Strength
3. Intelligence
4. Life
5. Accuracy (Default 100%, i.e. The attacks will ALWAYS hit.)
6. Offense (Default 100%, i.e. The attacks will not be modified.)
7. Defense (Default 100%, i.e. The damage taken will not be modified.)
8. Critical Chance (Default 10%, i.e. There is a 10% chance of scoring a critical hit.)
9. Critical Damage (Default 150%, i.e. A critical hit will deal 150% damage)

3.3. Game Modifiers
There are some Modifiers. They are:
1. Offense up
2. Defense up
3. Critical Chance up
4. Critical Damage up
5. Accuracy down

3.4 Enemies
This contains the list of the types of enemies. The list contains the types of enemies, the weapon it uses and the health it has.

3.5 Waves.
3.5.1 Wave Description.
This contains the description for each wave in the game.

3.5.2 Wave enemies
Contains the list of enemies for each wave.


