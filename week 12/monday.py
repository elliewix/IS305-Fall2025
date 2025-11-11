from lxml import etree

infile = open('hamlet-tei.xml', 'rb')
xml = infile.read()
infile.close()

tree = etree.fromstring(xml)
print(tree)

ns = {'tei': 'http://www.tei-c.org/ns/1.0'}

titles = tree.xpath('//tei:title/text()', namespaces = ns)
print(titles)
titles = tree.xpath('//tei:title//text()', namespaces = ns)
print(titles)
# I can use a boolean statement
titles = tree.xpath('//tei:title[@type = "statement"]/text()', namespaces = ns)
print(titles)

## looping over nodes
print(len(tree.xpath('//tei:stage', namespaces = ns)))
print(len(tree.xpath('//tei:stage/@type', namespaces = ns)))
print(len(tree.xpath('//tei:stage/text()', namespaces = ns)))
print(len(tree.xpath('//tei:stage//text()', namespaces = ns)))

stage_directions = tree.xpath('//tei:stage', namespaces = ns)

for stage in stage_directions:
    print(stage.xpath('@type'), stage.xpath('.//text()'))


