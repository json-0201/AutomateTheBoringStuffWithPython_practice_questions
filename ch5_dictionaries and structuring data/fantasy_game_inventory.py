'''
Write a function named displayInventory() that would take any possible “inventory”
and display it like the following:

Inventory:
12 arrow
42 gold coin
1 rope
6 torch
1 dagger
Total number of items: 62
'''

def main():
    stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    displayInventory(stuff)


def displayInventory(inventory: dict) -> None:
    print("Inventory:")
    sum = 0
    for k, v in inventory.items():
        print(v, k)
        sum += v
    print(f"Total number of items: {sum}")


if __name__ == "__main__":
    main()