inventory={"olma":1,"dinay":100,"qatiq":2,"tarvuz":20,"behi":10}
ask=input("")
if ask in inventory:
    pass
else:
    inventory[ask]=0
print(inventory)