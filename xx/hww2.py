from lxml import etree


a = float(input('Please input A:'))
c = a / 5
datas = []
for i in range(1,6):
    bj = a - (i - 1) * a / 5
    datas.append(bj)
d = a + sum(datas)
print('c=', c, 'd=', d)
print(datas)
root = etree.Element('root')
data = etree.SubElement(root, 'values')
data.set('a', str(a))
cs = etree.SubElement(data, 'c')
cs.text = str(c)
ds = etree.SubElement(data, 'd')
ds.text = str(d)
tree = etree.ElementTree(root)
tree.write('res.xml', pretty_print=True, xml_declaration=True, encoding='utf-8')
