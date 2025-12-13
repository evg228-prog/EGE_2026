with open(r'.\files\24_4642.txt') as file:
    data = file.readline()

for i in ['A1', 'B1', 'A2', 'B2']: data = data.replace(i, '++')
for char in 'AB12': data = data.replace(char, ' ')
data = data.split()
print(len(max(data, key=len)) // 2)

# 34

