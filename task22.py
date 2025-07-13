def group_students(students: list[dict[str, str]]) -> dict[str, list[str]]:
    group=dict() 
    for student in students:
        group_name=student['group']
        if group_name not in group.keys():
            group[group_name]=[]
        group[group_name].append(student['name'])
    return group
students=[
    {
        'name':'Ali',
        'group':'A'
    },
    {
        'name':'Yasin', 
        'group':'B'
    },
    {
        'name':'Jamol',
        'group':'C'
    },
    {
        'name':'Laylo',
        'group':'A'
    },
    {
        'name':'Komil',
        'group':'B'
    },
    {
        'name':'Abror',
        'group':'C'
    }
]
p=group_students(students)
print(p)