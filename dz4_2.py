import random
import numpy as np
n = 15
p = []
for i in range(n):
    a = random.randint(2, 100)
    p.append(a)
p.append(random.randint(2, 100))
m = np.zeros((n, n))
def mult(i, j):
    global m
    global p
    if i != j:
        if m[i][j] == 0:
            for k in range(i, j):

                tek = mult(i,k) + mult(k+1,j) + p[i] * p[k+1] * p[j+1]
                if tek < m[i][j] or m[i][j] == 0:
                    m[i][j] = tek
    return m[i][j]
mult(0, n-1)
print('матрицы:', p)
print('минимальное количество операций для умножения входных матриц:', end=' ')
print(m[0][n-1])
