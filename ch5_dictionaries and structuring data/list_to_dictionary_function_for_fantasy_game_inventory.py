'''
Write a function named addToInventory(inventory, addedItems), where
the inventory parameter is a dictionary representing the player’s inventory
(like in the previous project) and the addedItems parameter is a list like dragonLoot.
'''

from fantasy_game_inventory import displayInventory

def main():
    stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

    stuff = addToInventory(stuff,dragonLoot)
    displayInventory(stuff)


def addToInventory(inventory: dict, addedItems: list) -> dict:
    for item in addedItems:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory


if __name__ == "__main__":
    main()