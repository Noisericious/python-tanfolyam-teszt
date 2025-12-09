
from xml.dom import minidom
import xml.etree.ElementTree as xml_tree

xml_doc = minidom.parse("test_xml_file.xml")
print(xml_doc)

items = xml_doc.getElementsByTagName("items")
item = xml_doc.getElementsByTagName("item")

for i in item:
    print(i.attributes["name"].value) #írjuk ki a név értéket
    print(i.firstChild.data)

tree = xml_tree.parse("test_xml_file.xml")
root = tree.getroot()

for item in root:
    print(f"Root item: {item}")
    for i in item:
        print(i.attrib)
        print(i.text)

print("-" * 50)
print(root[0][0].text) #mátrix 0, 0 eleme, szövege
print("-" * 50)

for car in root[1]: #csak az auton megyek végig nem teljesen a root-on
    print(car.attrib)

data = xml_tree.Element("data")
items = xml_tree.SubElement(data, "items")
item1 = xml_tree.SubElement(items, "item")
item2 = xml_tree.SubElement(items, "item")
item1.set("name", "value1")
item2.set("name", "value2")
item1.text = "Data 1"
item2.text = "Data 2"

data_write = xml_tree.tostring(data, encoding="unicode")
with open("test.xml", "w", encoding="utf-8") as file:
    file.write(data_write)



