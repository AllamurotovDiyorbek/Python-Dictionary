def get_active_users(users: dict[str, dict[str, bool | str]]) -> list[str]:
    lst=[]
    for i in users:
        if users[i]["is_active"]==True:
            lst.append(i)
            pass
    return lst
users_data = {
    "Ali": {"is_active": True},
    "Vali": {"is_active": False},
    "Sami": {"is_active": True}
}
print(get_active_users(users_data))