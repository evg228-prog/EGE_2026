from re import finditer

with open(r'.\files\24_1273 (1).txt') as file:
    data = file.readline()

pattern = r'(^|(?<=XYZ))).+?($|(?=(XYZ)))'

ans = 0
for match in finditer(pattern, data):
    cnt_XYZ = match.groups().count('XYZ')
    ans = max(ans, len(match.group()) + 4 if cnt_XYZ == 2 else 2)

Lengths = [len(match.group()) + 4 if match.groups().count('XYZ') == 2 else 2 for match in finditer(pattern, data)]
print(max(Lengths))

# 305