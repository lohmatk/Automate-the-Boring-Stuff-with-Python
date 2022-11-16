# “Fantasy Game InventoryYou are creating a fantasy video game. T
# he data structure to model the player’s inventory will be a dictionary
# where the keys are string values describing the item in the inventory and the
# value is an integer value detailing how many of that item the player has. For
# example, the dictionary value {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
# means the player has 1 rope, 6 torches, 42 gold coins, and so on.”
#
# “Write a function named displayInventory() that would take
# any possible “inventory” and display it like the following:Inventory:
# 12 arrow
# 42 gold coin
# 1 rope
# 6 torch
# 1 dagger
#
# Total number of items: 63”



itemsAll = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(someBasicDict):
    print('Inventory:')
    total = 0
    for k, v in someBasicDict.items():
        print(v, k)
        total = total + v
    print('Total items:', total, '\n')

displayInventory(itemsAll)


# “List to Dictionary Function for Fantasy Game InventoryImagine that a vanquished dragon’s
# loot is represented as a list of strings like this:dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
# Write a function named addToInventory(inventory, addedItems), where the inventory parameter is a dictionary representing
# the player’s inventory (like in the previous project) and the addedItems parameter is a list like dragonLoot.
# The addToInventory() function should return a dictionary that represents the updated inventory. Note that the
# addedItems list can contain multiples of the same item. Your code could look something like
# this:def addToInventory(inventory, addedItems):
#     # your code goes here
#
# inv = {'gold coin': 42, 'rope': 1}
# dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
# inv = addToInventory(inv, dragonLoot)
# displayInventory(inv)The previous program (with your displayInventory() function from the
# previous project) would output the following:Inventory:
# 45 gold coin
# 1 rope
# 1 ruby
# 1 dagger
#
# Total number of items: 48”



dragonLoot = ['gold coin', 'oya', 'dagger', 'gold coin', 'gold coin', 'ruby', 'oya']

def addToInventory(basicDict, addedItems):
    for i in addedItems:
        if basicDict.setdefault(i) != None:
            basicDict[i] = basicDict.setdefault(i) + 1
        else:
            basicDict[i] = 1
    print('New dict: ', basicDict, '\n')

addToInventory(itemsAll, dragonLoot)
displayInventory(itemsAll)

