with open(r'.\files\24_5139.txt') as file:
    data = file.readline()

#          МОЁ РЕШЕНИЕ
for i in 'EUA': data = data.replace(i, '*')
for i in 'BCDF': data = data.replace(i, '+')
data = data.replace('+*+', '#')
for i in '*+':
    data = data.replace(i, ' ')
data = data.split()

#        ПЕРЕСТРАХОВКА
for i in 'EUA':
    data = data.replace(i, '*')
for i in 'BCDF':
    data = data.replace(i, '+')

while '+*+*+' in data:
    data = data.replace('+*+*+', '+*+ +*+')

data = data.replace('+*+', '#')
for i in '*+':
    data = data.replace(i, ' ')
data = data.split()

print(len(max(data, key=len)))

# 6

