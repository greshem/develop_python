
import codecs
from lxml import etree
#f=codecs.open("ceshi.html","r","utf-8")
f=codecs.open("sohu.html","r","gbk")
content=f.read()
f.close()
tree=etree.HTML(content)

print tree;

nodes=tree.xpath("//div/");


subnodes=nodes[0].xpath("//li/a")
for n in subnodes:
    print n.text
