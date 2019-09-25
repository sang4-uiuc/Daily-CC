# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

# Given the root to a binary tree, count the number of unival subtrees.

# For example, the following tree has 5 unival subtrees:

#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1

class Node:
    def __init__(self, data=None):
        self.data = data
        self.right = None
        self.left = None


def countTree(root):
    global count
    
    if (root is None):
        return
    left = countTree(root.left)
    right = countTree(root.right)
    
    if (left is None and right is None):
        
        # count += 1
        return (1, root.data)
    if (left[1] == root.data and left[0] == 1 and right[1] == root.data and right[0] == 1):
        # count += 1
        return (1, root.data)
    return (0, root.data)


a = Node(0)
b = Node(1)
c = Node(0)
d = Node(1)
e = Node(0)
f = Node(1)
g = Node(1)
a.left = b
a.right = c
c.left = d
d.left = f
d.right = g
c.right = e
count = 0
# def getUnivalTree(root):
    
#     countTree(root)
#     return count

# print(getUnivalTree(a))
countTree(a)
print(count)

# the logic it self isn't hard, but I had a hard time with python's bs scoping. I couldn't get the method parameter to keep count of the count
# that was super annoying, so I resorted to count using a global variable. It's not the best way and leaves me some warning, but it worked....

# looked up the correct solution, it's def more elegant than mine where they pass up the total count instead of incrementing it

# def count_unival_subtrees(root):
#     count, _ = helper(root)
#     return count

# # Also returns number of unival subtrees, and whether it is itself a unival subtree.
# def helper(root):
#     if root is None:
#         return 0, True
#     left_count, is_left_unival = helper(root.left)
#     right_count, is_right_unival = helper(root.right)
#     total_count = left_count + right_count
#     if is_left_unival and is_right_unival:
#         if root.left is not None and root.value != root.left.value:
#             return total_count, False
#         if root.right is not None and root.value != root.right.value:
#             return total_count, False
#         return total_count + 1, True
#     return total_count, False