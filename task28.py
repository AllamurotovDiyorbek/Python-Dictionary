def group_by_length(words: list[str]) -> dict[int, list[str]]:
    dct={}
    for i in words:
        if len(i) not in dct:
            dct[len(i)]=[i]
        else:
            dct[len(i)].append(i)
    return dct
list_one=['Ali','Komil','Allayor','Malik']
result=group_by_length(words=list_one)
print(result)