import re
import sys
from anytree import Node, AnyNode, RenderTree
from anytree.exporter import DotExporter
from anytree.util import rightsibling

input = "ModifiedContent<ModifiedContent<ScrollView<VStack<Optional<ModifiedContent<ForEach<Array<Chart>, String, ChartView>, _FocusSectionModifier>>>>, _SafeAreaRegionsIgnoringLayout>, _SafeAreaRegionsIgnoringLayout>"
leading = "[\w+\, ]+<"
x = re.findall(leading, input)
ending = "([\w, .]+>)|[>]"
y = re.findall(ending, input)
print(x)
print(y)
rootNode = Node('Root')
parentNode = rootNode
for index, item in enumerate(x):
    # print(str(index) + " " + item)
    value = item
    child = Node("")
    if item.find(',') >= 0:
        child = Node(str(index) + '\n' + value, parent=parentNode.parent)
        # parentNode = child
        print()
        sys.stdout.write("\t"*index + item)
    else:
        child = Node(str(index) + '\n' + value, parent=parentNode)
        parentNode = child
        print()
        sys.stdout.write("\t"*index + item)



DotExporter(rootNode).to_picture("udo.png")

parentNode1 = parentNode

for index, item in enumerate(y):
    print()
    att = len(y) - index
    sys.stdout.write("\t"*att + item)
    sideNode = item.split(',')
    for aNode in sideNode:
        if aNode == "":
            continue
        value = item
        child = Node(str(len(y) - index) + '\n' + aNode, parent=parentNode1)
    if item == "":
            newNode = parentNode1.parent
            if newNode == None:
                continue
            parentNode1 = parentNode1.parent
            continue
    # child = Node(str(len(y) - index) + '\n' + value, parent=parentNode1)
    if len(parentNode1.children) > 1:
        nextNode = rightsibling(parentNode1)
        if nextNode != None:
            parentNode1 = nextNode
            continue
    newNode = parentNode1.parent
    if newNode == None:
        print('Null here ' + parentNode1.name)
    else:
        parentNode1 = newNode


DotExporter(rootNode).to_picture("output.png")
