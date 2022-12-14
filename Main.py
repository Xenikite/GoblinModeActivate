# Imports

from storage.Game import Game
from storage.entity.Player import Player
from storage.menu.MainMenu import generateMainMenu

# Defining Variables
debugMode = True  # will be implemented later

# Defining Lists
equipmentTypes = ("weapon", "headgear", "chest", "arm", "ring", "leg", "shield", "shoes")

if __name__ == "__main__":
    player = Player(health=5,)
    instance = Game(player)
    instance.load()
    currentMenu = generateMainMenu()
    # Main Loop
    while True:
        print("Test Menu Here, disregard")
        currentMenu.print()
        option = input(">>> ")
        currentMenu.option(option, instance)
