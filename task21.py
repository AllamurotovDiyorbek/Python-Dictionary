def count_names(names: list[str]) -> dict[str, int]:
    ol={}
    for i in names:
        ol[i]=names.count(i)
    return ol   
names = ['olma','olma', 'olma','behi', 'nok', 'gilos']
p=count_names(names)
print(p)