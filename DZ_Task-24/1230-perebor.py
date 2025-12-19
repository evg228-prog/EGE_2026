with open(r'.\files\24_1230.txt') as file:
    data = file.readline()

ans = 0
cnt = 0
for i in range(len(data)):
    if data[i] not in 'WRQ':
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 0
ans = max(ans, cnt)
print(ans)

# 110