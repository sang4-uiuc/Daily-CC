# This problem was asked by PayPal.
import random

# Given a binary tree, determine whether or not it is height-balanced. 
# A height-balanced binary tree can be defined as one in which the heights of the two subtrees 
# of any node never differ by more than one.
# Python program to print all permutations with 
class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

# run time is O(N^2) since on each node, we recurse through its entire subtree, meaning getHeight is called on the same nodes
def balanceBinaryTree(root):
    if root == None:
        return True
    height_diff = getHeight(root.left) - getHeight(root.right)
    if abs(height_diff) > 1:
        return False
    else:
        return balanceBinaryTree(root.left) and balanceBinaryTree(root.right)

def getHeight(root):
    if root == None:
        return 0
    return max(getHeight(root.left), getHeight(root.right)) + 1

def balanceBinaryTreeEfficient(root):
    if root == None:
        return 0

    left_height = balanceBinaryTreeEfficient(root.left)
    if left_height == -1:
        return -1
    
    right_height = balanceBinaryTreeEfficient(root.right)
    if right_height == -1:
        return -1

    height_diff = getHeight(root.left) - getHeight(root.right)
    if abs(height_diff) > 1:
        return -1
    else:
        return max(left_height, right_height) + 1

def isBalanced(root):
    if balanceBinaryTreeEfficient(root) == -1:
        return False
    else:
        return True
root = Node(1)
root.left = Node(2)
root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.right.left = Node(6)
# root.right.right = Node(7)

l = root

for i in range(50):
    if random.random() < .5:
        l.left = Node(4)
        l = l.left
    else:
        l.right = Node(5)
        l = l.right
        
    if random.random() < .5:
        l.left = Node(4)
    else:
        l.right = Node(5)

def printViewUtil(root, space):
    if root == None:
        return

    space += 10
    printViewUtil(root.right, space)
    print('\n')
    for i in range(10, space, 1):
        print(' ', end='')
    print(root.val)
    print('\n')
    printViewUtil(root.left, space)

def printView(root):
    printViewUtil(root, 0)

# printView(root)
import time
start1 = time.time()

for i in range(10000):
    balanceBinaryTree(root)
    
end1 = time.time() - start1

print("time spent on inefficient: {}".format(end1))

start2 = time.time()
for i in range(10000):
    isBalanced(root)
    
end2 = time.time() - start2

print("time spent on efficient: {}".format(end2))