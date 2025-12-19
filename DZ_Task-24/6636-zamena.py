with open(r'.\files\24_6636.txt') as file:
    data = file.readline()

for i in '24': data = data.replace(i, '*')
for i in '135': data = data.replace(i, '+')
data = data.replace('*+', '#')
for i in '+*': data = data.replace(i, ' ')
data = data.split()
print(len(max(data, key=len)))

# 10