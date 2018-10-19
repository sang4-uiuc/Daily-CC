# Typically, an implementation of in-order traversal of a binary tree has O(h) space complexity, 
# where h is the height of the tree. Write a program to compute the in-order traversal of a binary tree using O(1) space.

# I have no idea how to do this, use a dictionary? 
# I'm just gonna solve inorder traversal without recursion, but with stack
class Node: 
      
    # Constructor to create a new node 
    def __init__(self, data): 
        self.data = data  
        self.left = None
        self.right = None

def inOrder(root): 
    current = root  
    s = []
    output = []
    while True:
        if current:
            s.append(current)
            current = current.left
        else:
            if len(s) > 0:
                current = s.pop()
                output.append(current.data)
                current = current.right
            else:
                break
    return output

root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
  
print(inOrder(root))
      