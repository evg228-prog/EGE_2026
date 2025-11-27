from string import printable
def convert(num, sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1]
ans = []
for x in range(1, 2400):
    num_10 = 7*9**210 + 6*9**110 - x
    num_9 = convert(num_10, 9)
    if num_9.count('0') == 100:
        ans.append(x)
print(max(ans))

# 2394

