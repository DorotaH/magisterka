import sys
import xml.etree.ElementTree as etree


def get_attr_number(node):
	"""Calculate the score of the XML document by summing the number of attributes of each element."""
	score = sum(get_attr_number(child) for child in node)
	# Add the number of attributes of the current node to the score
	score += len(node.attrib)
	# If the node is not an element (i.e., it's a text), return 0
	return 0 if node.tag in ["text", "document"] else score


if __name__ == "__main__":
	sys.stdin.readline()
	xml = sys.stdin.read()
	tree = etree.ElementTree(etree.fromstring(xml))
	root = tree.getroot()
	print(get_attr_number(root))
