def addToInventory(inventory, addedItems):
    for i in addedItems:
        inventory.setdefault(i, 0)    
        inventory[i] +=1
    print(inventory)
inv = {'gold coin': 24, 'rope' : 1}
dragonloot = ['gold coin', 'gold coin', 'dragger', 'gold coin', 'ruby']
addToInventory(inv, dragonloot)
