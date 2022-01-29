n = input()

sum = 0
memo = []
while True:
    for i in map(int, n):
        tmp = pow(i, 2)
        sum = sum + tmp

    if sum == 1:
        print(True)
        break
    try:
        if memo.index(n) >= 0:
            print(False)
            break
    except ValueError:
        memo.append(n)
        n = str(sum)
        sum = 0
        continue
