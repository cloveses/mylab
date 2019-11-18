
a = float(input('Please input A:'))
c = a / 5
datas = []
for i in range(1,6):
    bj = a - (i - 1) * a / 5
    datas.append(bj)
d = a + sum(datas)
print('c=', c, 'd=', d)
print(datas)