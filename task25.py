from typing import Union
def group_by_age(people: list[dict[str, int | str]]) -> dict[int, list[str]]:
    group={}
    for person in people:
        group.setdefault(person['age'],[]).append(person['name'])
    return group
people=[
    {
        "name":"ali",
        "age":13
    },
    {
        "name":"vali",
        "age":17
    },
    {
        "name":"sami",
        "age":15
    },
    {
        "name":"javohir",
        "age":15
    }
]
result=group_by_age(people)
print(result)