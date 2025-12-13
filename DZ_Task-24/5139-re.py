from re import *
with open(r'.\files\24_5139.txt') as file:
    data = file.readline()

pattern = r'([BCDF][EUA][BCDF])+'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)) // 3)

# 6