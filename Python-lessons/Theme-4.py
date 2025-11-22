# Цикл while
num = int(input('Введите число: '))

sum_digits = 0
while num:
    sum_digits += num % 10
    num //= 10

# Цикл for
# Итерируемый объект - объект, который состоит из других элементов.
# str - состоят из символов.
# list, tuple, set, dict - содержат в себе любые типы данных.

# range(N) - последовательность целых чисел [0, N)
# range(M, N) - последовательность целых чисел [M, N)
# range(M, N, S) - последовательность целых чисел [M, N) с шагом S

# Операторы
# break - остановка цикла
for i in range(10):
    #print(i)
    if i ==5:
        break

# continue - переход к следующему шагу цикла
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# else - позволяет выполнить блок кода, если цикл завершился без break
for i in range(10):
    print(i)
    if i == 10:
        break
else:
    print('Цикл завершился добровольно')