from re import *
with open(r'.\files\24_1230.txt') as file:
    data = file.readline()

pattern = r'[^WRQ]+'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))

# 110