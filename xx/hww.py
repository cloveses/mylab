
# res = {}
# lstA, lstB = input('integer list:'),input('integer list:')
# lstA = [int(i) for i in lstA.split(',')]
# lstB = [int(i) for i in lstB.split(',')]
# for k, v in zip(lstA, lstB):
#     res[k] = v
# print(res)

# pa, pb = input('integer list:'),input('integer list:')
# pa = [int(i) for i in pa.split(',')]
# pb = [int(i) for i in pb.split(',')]
# print(abs(pa[0]- pb[0]) + abs(pa[1]- pb[1]))

# from functools import reduce

# lstA = input('format: 1,2;3,4,5;2,4')
# lstA = lstA.split(';')
# lstA = [set(i.split(',')) for i in lstA]
# print(reduce(lambda x,y: x|y, lstA))

import lxml, os
from lxml import etree

d,u,p,mu = float(input()), float(input()), float(input()), float(input())
re = d * u * p / mu
if re < 2:
    fei = 24 / re
elif 2 < re < 500:
    fei = 18.5 / (re ** 0.6)
elif re == 500:
    fei = 8
elif re == 2:
    fei = 0.37
else:
    fei = 0.44
print('re=', re, 'fei=' ,fei)
if os.path.exists('res.xml'):
    file = etree.parse('res.xml')
    root = file.xpath('/results')[0]
    row = etree.SubElement(root, 'row')
    re_element = etree.SubElement(row, 're')
    re_element.text = str(re)
    fei_element = etree.SubElement(row, 'fei')
    fei_element.text = str(fei)
    tree = etree.ElementTree(root)
    tree.write('res.xml', pretty_print=True, xml_declaration=True, encoding='utf-8')
else:
    root = etree.Element('results')
    row = etree.SubElement(root, 'row')
    re_element = etree.SubElement(row, 're')
    re_element.text = str(re)
    fei_element = etree.SubElement(row, 'fei')
    fei_element.text = str(fei)
    tree = etree.ElementTree(root)
    tree.write('res.xml', pretty_print=True, xml_declaration=True, encoding='utf-8')



# a = float(input('Please input A:'))
# c = a / 5
# datas = []
# for i in range(1,6):
#     bj = a - (j - 1) * a / 5
#     datas.append(bj)
# d = a + sum(datas)
# print('c=', c, 'd=', d)
# print(datas)