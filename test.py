import copy

li1 = [1, 2, 3, 4, 5]
li2 = copy.deepcopy(li1)
li1[2] = 0
print(f'li1: {li1}')
print(f'li2: {li2}')