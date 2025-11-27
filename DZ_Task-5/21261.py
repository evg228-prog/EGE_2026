from string import printable as olo


def convert(num, sys):
    res = ''
    while num:
        res += olo[num % sys]
        num //= sys
    return res[::-1]

ans1 = []
ans = []
for N in range(1, 100_000):
    R = convert(N, 4)
    if sum(map(int, R)) % 3 == 0:
        new_R = ''
        for i in R:
            if i == '0':
                new_R += '2'
            elif i == '2':
                new_R += '0'
            else:
                new_R += i
            R = '32' + new_R
    else:
        R = R[0] + '10' + R[3:] + '33'
    R = int(R, 4)
    if R > 320:
        ans.append([R, N])
ans_R = min(ans)[0]
ans_N = 0
for i in ans:
    if i[0] == ans_R:
        if i[1] > ans_N:
            ans_N = i[1]
print(ans_N)



