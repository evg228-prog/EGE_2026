ans = []
for N in range(1, 100_000):
    R = f'{N:b}'
    if N % 2 == 0:
        R = R + f'{R.count('1'):b}'
    else:
        R = '1' + R + '101'
    R = int(R, 2)
    if R > 350:
        ans.append(N)
print(min(ans))

# 17