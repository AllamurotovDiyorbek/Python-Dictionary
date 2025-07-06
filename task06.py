diction= {"brand": "Chevrolet", "model": "Cobalt", "color": "white"}
ask=input("keyni kiriting? ")
if ask in diction:
    print(diction[ask])
else:
    print("Topilmadi")