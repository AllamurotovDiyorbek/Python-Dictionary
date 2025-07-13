def filter_non_zero(d: dict[str, int]) -> dict[str, int]:
    result={}
    for key in d:
        value=d[key]
        if value!=0:
            result[key]=value
    return result
data={
    'a':1,
    'b':2,
    'c':3,
    'd':0,
    'e':5,
    'f':0
}
print(filter_non_zero(data) )