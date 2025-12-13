with open(r'.\files\24_5139.txt') as file:
    data = file.readline()

vowels = 'EUA'
consents = 'BCDF'

ans = 0
cnt = 0
i = 0
while i < len(data) - 2:
    if data[i] in consents and data[i + 1] in vowels and data[i + 2] in consents:
        cnt += 1
        i += 3
    else:
        ans = max(ans, cnt)
        cnt = 0
        i += 1
ans = max(ans, cnt)
print(ans)

# 6