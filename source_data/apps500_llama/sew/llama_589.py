import  sys
import  xml.etree.ElementTree as  etree

def get_attr_number(node):
    """Returns the total score of the given XML document"""
    # Initialize the score with 0
    score=0
    
    # If the node is an element, increment the score by the number of its attributes
    if  node.attrib:
        score += len(node.attrib)
    
    # Recursively add the scores of all child elements
    for child in node:
        score = score + get_attr_number(child)
    
    return score

if __name__ == '__main__':
    sys.stdin.readline()  # Ignore the first line (N)
    xml=sys.stdin.read()
    tree=etree.ElementTree(etree.fromstring(xml))
    root=tree.getroot()
    print(get_attr_number(root))