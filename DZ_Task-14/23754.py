from string import printable as olo
def convert(num, sys):
    res = ''
    while num:
        res += olo[num % sys]
        num //= sys
    return res[::-1]
ans = []
for x in range(1, 3000):
    num1 = convert(9*11**210 + 8*11**150 - x, 11)
    if num1.count('0') == 60:
        ans.append(x)
print(max(ans))

# 2992