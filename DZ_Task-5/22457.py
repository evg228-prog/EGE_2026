ans = []
from string import printable
def convert(num, sys):
    res = ''
    while num != 0:
        res += printable[num % sys]
        num //= sys
    return res[::-1]
for N in range(1, 100000):
    R = convert(N,7)
    if (R.count('1') * 1 + R.count('2') * 2 + R.count('3') * 3 +
        R.count('4') * 4 + R.count('5') * 5 + R.count('6') * 6) % 2 == 0:
        R = R + '555'
    else:
        R = '33' + R + '6'
    R = int(R, 7)
    if R < 12717:
        ans.append(N)
print(max(ans))

# 47