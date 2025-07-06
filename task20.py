permissions = {"read": True, "write": False, "delete": True}
# chiqishi: read, delete
result=0
for i in permissions:
    if permissions[i]==True:
        print(i)
 