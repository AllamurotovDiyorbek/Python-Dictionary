def group_indices(numbers: list[int]) -> dict[int, list[int]]:
    group=dict()
    for i,number in enumerate(numbers):
         if number not in group:
            group[number] = []
         group[number].append(i)
    return group
nums=[1,2,3,4,1,2,1,3,1,3,9,8,4,3]
result=group_indices(nums)
print(result)