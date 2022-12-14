from storage.CombatInstance import CombatInstance
from storage.Item.Box import Box
from storage.Game import Game
from storage.Variant import BoxTypeVariant
from storage.entity import Entity
from storage.menu import MenuItem, Menu


def buildBox(instance: Game, boxType, rarity=1, keys=1):
    contents = instance.getBoxType(boxType).getItem()
    newBox = Box(boxType, contents)
    return newBox

def __mm_FuckOff(instance: Game):
    import sys
    instance.save()
    sys.exit(0)

def __mm_Pull(instance: Game):
    highest = 0
    avg = []
    failCount = 0
    for x in range(100):
        i = instance.player.pull(BoxTypeVariant.COPPER.value)
        if i.rarity > 0.95:
            if highest < failCount:
                highest = failCount
            avg.append(failCount)
            failCount = 0
        else:
            failCount+=1
    print("highest " + str(highest))
    average = 0
    freq: dict[int, int] = {}
    for x in avg:
        average += x
        if x not in freq.keys():
            freq[x] = 1
        else:
            freq[x] += 1
    print("average " + str(average/len(avg)))
    print("inventory size " + str(len(instance.player.inventory)))
    instance.save()

def __mm_TestAttack(instance: Game):
    health = instance.player.attack(Entity("Goblin", 5, 5, 0))
    print(health)

def __mm_Hit(instance: Game):
    instance.player.hit(10)
    print(instance.player.health)
    instance.save()

def __mm_Save(instance: Game): #Created so I can understand how menu generation works
    try:
        instance.save()
        print("Instance Saved")
    except:
        return
    return

def __mm_Combat(instance: Game):
    CombatInstance(instance, Entity("Goblin", 5, 1, 0)).loop()

def generateMainMenu():
    pull = MenuItem("pull", "Pull some random items", __mm_Pull)
    hit = MenuItem("hit", "Smack a Bitch", __mm_Hit)
    fuckOff = MenuItem("fuck off", "Furry Sex Time", __mm_FuckOff)
    saveGame = MenuItem("save", "Save the damn game", __mm_Save)
    atk = MenuItem("atk", "Combat go Brrr", __mm_TestAttack)
    combat = MenuItem("combat", "More Combat", __mm_Combat)
    menu = Menu()
    menu.add(pull)
    menu.add(hit)
    menu.add(fuckOff)
    menu.add(saveGame)
    menu.add(atk)
    menu.add(combat)
    return menu
