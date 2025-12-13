from re import *
with open(r'.\files\24_4642.txt') as file:
    data = file.readline()

pattern = '([AB][12])+'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)) // 2)