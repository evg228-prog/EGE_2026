from string import printable
def convert(num, sys):
    res = ''
    while num != 0:
        res += printable[num % sys]
        num //= sys
    return res[::-1]
ans = []
for N in range(1, 10000):
    R = convert(N, 3)
    if N % 3 == 0:
        R = R + R[-2:]
    else:
        new_R = R.count('1') + R.count('2')
        new_R_2 = convert(new_R, 3)
        R = R + new_R_2
    R = int(R, 3)
    if R > 220 and R % 2 == 0:
        ans.append(R)
print(min(ans))

# 222

