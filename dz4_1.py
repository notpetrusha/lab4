import numpy as np
import random
n = int(input('количество экспонатов'))
w = int(input('вес экспанатов за один заход'))
m = int(input('количестов заходов '))
exp_w = [random.randint(1, 10) for _ in range(n)]  # вес каждого экспоната
exp_p = [random.randint(1, 10) for _ in range(n)]  # стоимость каждого экспоната
ans = 0
def func(n, w):
    a = np.zeros((n, w))
    global exp_w
    global exp_p
    for k in range(n):
        for s in range(w):
            if s >= exp_w[k]:
                a[k][s] = max(a[k - 1][s], a[k - 1][s - exp_w[k]] + exp_p[k])
            else:
                a[k][s] = a[k - 1][s]
    ans = a[n - 1][w - 1]
    sum = a[n - 1][w - 1]
    j = w - 1
    for i in range(n - 1, 0, -1):

        if sum == 0:
            break
        if a[i - 1][j] != sum:
            sum -= exp_p[i]
            j -= exp_p[i]
            n -= 1
            exp_w.remove(exp_w[i])
            exp_p.remove(exp_p[i])
    return ans, n
for i in range(m):
    tek, n = func(n, w)
    ans += tek
print(ans)

