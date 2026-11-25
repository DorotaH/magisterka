import sys
import xml.etree.ElementTree as etree


def get_attr_number(node):
    """Calculate the score of the XML document by summing the number of attributes of each element."""
    score = 0
    # For each child element in the current node
    for child in node:
        # Recursively call get_attr_number to add the score of the child
        score += get_attr_number(child)
    # Add the number of attributes of the current node to the score
    score += len(node.attrib)
    # If the node is not an element (i.e., it's a text), return 0
    if node.tag == 'text' or node.tag == 'document':
        return 0
    return score

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
