# This problem was asked by Morgan Stanley.

# In Ancient Greece, it was common to write text with the first line going left to right, 
# the second line going right to left, and continuing to go back and forth. This style was called "boustrophedon".

# Given a binary tree, write an algorithm to print the nodes in boustrophedon order.

# For example, given the following tree:

#        1
#     /     \
#   2         3
#  / \       / \
# 4   5     6   7
# You should return [1, 3, 2, 4, 5, 6, 7]
class Node: 
	def __init__(self,key): 
		self.left = None
		self.right = None
		self.val = key 

def boustrophedon(root):
    if root is None:
        return
    current_level = []
    next_level = []
    current_level.append(root)
    direction = False
    while len(current_level) > 0:
        node = current_level.pop()
        print(node.val)
        if direction:
            if node.right:
                next_level.append(node.right)
            if node.left:
                next_level.append(node.left)
        else:
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        # print(current_level)

        if len(current_level) == 0:
            # print("tri")
            direction = not direction
            current_level = next_level
            next_level =[]


root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.left = Node(6) 
root.right.right = Node(7)

# print(root.right.val)

boustrophedon(root)