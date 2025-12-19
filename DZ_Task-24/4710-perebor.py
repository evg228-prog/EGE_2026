with open(r'files/24_4710.txt') as file:
    data = file.readline()

vowels = 'AO'
consents = 'CDF'
ans = 0
cnt = 0
i = 0
while i < len(data) - 1:
    if data[i] in consents and data[i + 1] in vowels:
        cnt += 1
        i += 2
    else:
        ans = max(ans, cnt)
        cnt = 0
        i += 1
ans = max(ans, cnt)
print(ans)

# 95

