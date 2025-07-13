def count_letters(text: str) -> dict[str, int]:
    dct={}
    for i in text:
        if i in dct:
            continue
        elif i!=" ":
            dct[i]=text.count(i)
    return dct
t="Assaka bank"
print(count_letters(t))