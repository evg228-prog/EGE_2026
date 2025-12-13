from re import *
with open(r'.\files\24_2426.txt') as file:
    data = file.readline()

pattern = r'[123]+'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))

# 20
