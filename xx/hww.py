import lxml, os
from lxml import etree

d,u,p,mu = float(input()), float(input()), float(input()), float(input())
re = d * u * p / mu
if re == 2:
    fei = 0.37
elif re == 500:
    fei = 8
elif re < 2:
    fei = 24 / re
elif 2 < re < 500:
    fei = 18.5 / (re ** 0.6)
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
