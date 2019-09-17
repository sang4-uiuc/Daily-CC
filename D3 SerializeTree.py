# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

class Node:
    def __init__(self, data = None):
        self.left = None
        self.right = None
        self.data = data

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)
g = Node(7)
a.left = b
b.left = c
b.right = d
a.right = e
e.left = f
e.right = g

def serializeTree(root, f):
    if root == None:
        f.write('x')
        return
    f.write(str(root.data))
    serializeTree(root.left, f)
    serializeTree(root.right, f)

def deserializeTree(f):
    val = f.read(1)
    if not val:
        return
    root = Node()
    if val != 'x':
        root = Node(val)
        root.left = deserializeTree(f)
        root.right = deserializeTree(f)
    return root
    
    
def deserializeTree2(root, f):
    val = f.read(1)
    if not val:
        return
    root = Node(val)
    deserializeTree2(root.left, f)
    deserializeTree2(root.right, f)

def main():
    f = open("D3 serialized.txt", "w+")
    serializeTree(a, f)
    f.close()

    
    f = open("D3 serialized.txt", "r")
    z = deserializeTree(f)
    f.close()
    preorder(z)

def preorder(root):
    if (root):
        print(root.data)
        preorder(root.left)
        preorder(root.right)


main()

# took awhile to get used to it, was stuck on having to do it one way without assigning value
# but yeah, if you get it this should be easy. Serializing/Deserializing is just fancy word for storing shit in another format lmao