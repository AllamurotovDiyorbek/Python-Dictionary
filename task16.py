person = {"name": "Ali", "age": 25, "city": "Tashkent"}
ask=input("dict:")
if ask not in person:
    print("Bunday kalit yoq")
else:
    del person[ask]
print(person)