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
    if (R.count('1') + R.count('2')) % 2 == 0:
        R = '12' + R[2:] + '0'
    else:
        R = '10' + R[2:] + '2'
    R = int(R, 3)
    if R > 105:
        ans.append(N)
print(min(ans))

# 28