with open(r'.\files\24_6636.txt') as file:
    data = file.readline()

digits_chet = '24'
digits_nechet = '135'
ans = 0
cnt = 0
i = 0
while i < len(data) - 1:
    if data[i] in digits_chet and data[i + 1] in digits_nechet:
        cnt += 1
        i += 2
    else:
        ans = max(ans, cnt)
        cnt = 0
        i += 1
ans = max(ans, cnt)
print(ans)

# 10