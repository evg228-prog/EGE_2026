from string import printable as olo

for x in olo[:29]:
    num1 = int(f'923{x}874', 29)
    num2 = int(f'524{x}6152', 29)
    num3 = num1 + num2
    if num3 % 28 == 0:
        print(x, num3 // 28)

# 3319197720