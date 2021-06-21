class Node:
    	def __init__(self, value=None):
		self.value = value
		self.left = None
		self.right = None
	def __str__(self):
		return str(self.value)
class BinaryTree:
	def __init__(self, root=None):
		self.root = root
	def preOrder(self):
		output = []
		if self.root == None:
			return output
		def walk(root):
			output.append(root.value)
			if root.left:
				walk(root.left)
			if root.right:
				walk(root.right)
		walk(self.root)
		return output
def tree_intersection(tree1, tree2):
	result = []
	if tree1.root == None or tree2.root == None:
		return None
	def _walk(root1, root2):
		if root1.value == root2.value:
			result.append(root1.value)
		if root1.left and root2.left:
			_walk(root1.left, root2.left)
		if root1.right and root2.right:
			_walk(root1.right, root2.right)
	_walk(tree1.root, tree2.root)
	return result

if __name__ == "__main__":
	tree1 = Node(150)
	tree1.left = Node(100)
	tree1.left.left = Node(75)
	tree1.left.right = Node(160)
	tree1.left.right.left = Node(125)
	tree1.left.right.right = Node(175)
	tree1.right = Node(250)
	tree1.right.left = Node(200)
	tree1.right.right = Node(350)
	tree1.right.right.left = Node(300)
	tree1.right.right.right = Node(500)
	binary_tree1 = BinaryTree(tree1)
	print(binary_tree1.preOrder())
	tree2 = Node(42)
	tree2.left = Node(100)
	tree2.left.left = Node(15)
	tree2.left.right = Node(160)
	tree2.left.right.left = Node(125)
	tree2.left.right.right = Node(175)
	tree2.right = Node(600)
	tree2.right.left = Node(200)
	tree2.right.right = Node(350)
	tree2.right.right.left = Node(4)
	tree2.right.right.right = Node(500)
	binary_tree2 = BinaryTree(tree2)
	print(binary_tree2.preOrder())
	print(tree_intersection(binary_tree1, binary_tree2))
