import math
from matplotlib import pyplot as plt

def taylor_sum(k, n):
    if not -1 < k <= 1:
        raise ValueError('−1 < k ≤ 1')
    s = 0
    for i in range(n):
        s += ((-1) ** n) * ((k ** (n + 1)) / (n + 1))
    return s


ns = (1,3,5,9)
for n in ns:
    x_datas = []
    y_datas = []
    x = -0.9
    while x <= 1:
        x_datas.append(x)
        y_datas.append(taylor_sum(x, n))
        x += 0.1
    plt.plot(x_datas, y_datas)
plt.show()
