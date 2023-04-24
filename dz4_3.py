def lcs(s):
    n = len(s) - 1
    ans = [0] * (n + 1)
    cur = [0] * (n + 1)
    p = []
    temp = []

    ans[0] = 1
    cur[0] = 1
    temp.append(s[0])
    p.append(s[0])
    for i in range(1, n + 1):
        if s[i] > s[i - 1]:
            temp.append(s[i])
            cur[i] = cur[i - 1] + 1
            if ans[i - 1] > cur[i]:
                ans[i] = ans[i - 1]
            else:
                ans[i] = cur[i]
        else:
            temp = []
            temp.append(s[i])
            cur[i] = 1
            ans[i] = ans[i - 1]

        if len(temp) > len(p):
            p = temp
    print(ans[n])
    return p
a = input('Введите числа через пробел ').split()
for i in range (len(a)):
    try:
        a[i] = int(a[i])
    except:
        print()
print('p:', lcs(a))
