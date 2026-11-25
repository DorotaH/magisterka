import sys
import xml.etree.ElementTree as etree


def get_attr_number(node):
    """
    Calculate the score of an XML document by summing up the number of attributes of each element.

    Args:
        node (xml.etree.ElementTree.Element): The root node of the XML document.

    Returns:
        int: The score of the XML document.
    """

    # Use a recursive function to traverse the tree and count the attributes of each element
    def count_attributes(element):
        # Base case: If the element has no children, return the number of attributes
        if len(element) == 0:
            return len(element.attrib)

        # Recursive case: Count the attributes of the current element and its children
        return len(element.attrib) + sum(count_attributes(child) for child in element)

    # Call the recursive function on the root node
    return count_attributes(node)


if __name__ == "__main__":
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
