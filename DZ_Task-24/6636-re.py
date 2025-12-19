from re import *
with open(r'.\files\24_6636.txt') as file:
    data = file.readline()

pattern = '([24][135])+'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)) // 2)

# 10