ans = []
from string import printable
def convert(num, sys):
    res = ''
    while num != 0:
        res += printable[num % sys]
        num //= sys
    return res[::-1]
for N in range(1, 100000):
    R = convert(N, 8)
    if (R.count('2') + R.count('4') + R.count('6')) % 2 != 0:
        R = R[-3:] + '46'
    else:
        R = convert(N % 8 * 5, 8) + R
    R = int(R, 8)
    if N >= 80:
        ans.append(R)
print(min(ans))

# 38

