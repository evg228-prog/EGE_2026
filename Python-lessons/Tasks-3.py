# Задача №2
from random import randint

rand_num = randint(0, 100)

if rand_num % 3 == 0:
    print(rand_num // 3)
else:
    print(rand_num * 2)

# Задача №3
cell_1 = input('Введите стартовую клетку: ')
cell_2 = input('Введите конечную клетку: ')

move_horizontal = abs(int(cell_1[1])- int(cell_2[1]))
move_vertical = abs(int(cell_1[0]) - int(cell_2[0]))

cond_1 = move_horizontal == 2 and move_vertical == 1
cond_2 = move_horizontal == 1 and move_vertical == 2

if cond_1 or cond_2:
    print('YES!')
else:
    print('NO!')