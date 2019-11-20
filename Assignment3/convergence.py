import math
from matplotlib import pyplot as plt

def taylor_sum(k, n):
    # k值超出范围则引发错误
    if not -1 < k <= 1:
        raise ValueError('−1 < k ≤ 1')
    s = 0
    #求和
    for i in range(1, n+1):
        factor = (-1) ** (n + 1)
        num = k ** n
        den = n
        s += (num / den) * factor
    return s

# 收集用于制作图例的数据
legend_hdls = []
legend_labels = []
# 添加标题
plt.title('Taylor sum vs ln(x+1)', fontsize='large', fontweight='bold')
#循环绘制四条曲线
ns = (1, 3, 5, 9) #
for n in ns:
    x = -0.9
    x_datas = []
    y_datas = []
    while x <= 1:
        x_datas.append(x)
        y_datas.append(taylor_sum(x, n))
        x += 0.1
    hdl, = plt.plot(x_datas, y_datas)
    legend_hdls.append(hdl)
    legend_labels.append('n=%d' % n)

# 绘制对比曲线
x = -0.9
x_datas = []
y_datas = []
while x <= 1:
    x_datas.append(x)
    y_datas.append(math.log(x+1))
    x += 0.1
hdl, plt.plot(x_datas, y_datas, color='black')
legend_hdls.append(hdl)
legend_labels.append('ln(x+1)')
#添加图例
plt.legend(handles=legend_hdls, labels=legend_labels)
#保存图片
plt.savefig("taylorsum.png")
plt.show()
