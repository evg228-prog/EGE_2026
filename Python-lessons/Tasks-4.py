# Задача №1
num = int(input())

num_1 = num
num_2 = num

while num_1:
    print(num_1 % 10)
    num_1 //= 10

print('###############################')
num_2 = str(num)
print(num_2[::-1])

print('###############################')
num_3 = str(num)
for i in range(len(num_3)):
    print(i, num_3[i])

print('###############################')
num = int(input())

num_1 = num
while num_1:
    print(num_1 % 10)
    num_1 //= 10
