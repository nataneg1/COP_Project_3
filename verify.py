import os

class NodeNotFoundException(Exception):
	def __init__(self, value):
		self.value = value
	
	def __str__(self):
		return repr(self.value)


class Node:
	def __init__(self, key, children=None):
		self.key = key
		self.children = children or []
	
	def __str__(self):
		return str(self.key)

class naryTree:

	def __init__(self):
		self.root = None
		self.size = 0

	def find_node(self, node, key):
		if node == None or node.key == key:
			return node		
		for child in node.children:
			return_node = self.find_node(child, key)
			if return_node: 
				return return_node
		return None	


	def depth(self, key):
		node = self.find_node(self.root, key)
		if not(node):
			raise NodeNotFoundException('No element was found with the informed parent key.')
		return self.max_depth(node)

	def max_depth(self, node):
		if not(node.children):
			return 0
		children_max_depth = []
		for child in node.children:
			children_max_depth.append(self.max_depth(child))
		return 1 + max(children_max_depth)

	def add(self, new_key, parent_key=None):
		new_node = Node(new_key)
		if parent_key == None:
			self.root = new_node
			self.size = 1
		else:
			parent_node = self.find_node(self.root, parent_key)
			if not(parent_node):
				raise NodeNotFoundException('No element was found with the informed parent key.')
			parent_node.children.append(new_node)
			self.size += 1
	
	def print_tree(self, node, str_aux):
		if node == None: return "empty"
		str_aux += str(node) + ''
		for i in range(len(node.children)):
			child = node.children[i]
			end = '' if i < len(node.children) - 1 else ''
			str_aux = self.print_tree(child, str_aux) + end
		str_aux += ''
		return str_aux

	def is_empty(self):
		return self.size == 0

	def lenght(self):
		return self.size

	def __str__(self):
		return self.print_tree(self.root, "")

def tickerExists(tickerName):
    string = tickerName
    str_match = [s for s in arry if string in s]
    if not str_match:
        return False
    else:
        return True




arry = []
tree = naryTree()

directory = 'Stocks'
for filename in os.scandir(directory):
    if filename.is_file():
        string = filename.path
        x = slice(0, 7195)
        arry.append(string[7:-7])
        tree.add(arry[x])

# val = input("Name: ")
# tickerExists(arry, val)