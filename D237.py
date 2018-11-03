# This problem was asked by Amazon.

# A tree is symmetric if its data and shape remain unchanged when it is reflected about the root node. The following tree is an example:

#         4
#       / | \
#     3   5   3
#   /           \
# 9              9
# Given a k-ary tree, determine whether it is symmetric.

# Node structure 
class NetworkNode: 
  
    # Utility function to create new node 
    def __init__(self, value): 
        self.value = value 
        self.children = []


    def insert(self, NetworkNode):
        self.children.append(NetworkNode)

    def traverse(self):
        node = self # start from the head node
        print(len(node.children))
        if len(node.children) == 0:
            print(node.value)
  
def getValue(root, stack, queue):
        stack.append(root.value)
        queue.append(root.value)
        return
  
# the basic idea is that on each level, there would be a stack and queue both pushing in items
# and if the order of popping the stack and dequeueing the queue is the same
# then it's good, else false
# i somehow can't code it out
def isSymmetric(root): 
        stack = []
        queue = []
        if root:
            for child in root.children:
                getValue(child, stack, queue)
        while len(stack)!=0 and len(queue) != 0:
            a = stack.pop()
            b = queue.pop(0)
            if a != b:
                
                return False
            
        if len(stack) != 0 or len(queue) != 0:
            print('ch2')
            return False
        return True
def isMirrorBinary(root1 , root2): 
    # If both trees are empty, then they are mirror images 
    if root1 is None and root2 is None: 
        return True 
    """ For two trees to be mirror images, the following three 
        conditions must be true 
        1 - Their root node's key must be same 
        2 - left subtree of left tree and right subtree 
          of right tree have to be mirror images 
        3 - right subtree of left tree and left subtree 
           of right tree have to be mirror images 
    """
    if (root1 is not None and root2 is not None): 
            if  root1.key == root2.key: 
                return (isMirror(root1.left, root2.right)and
                isMirror(root1.right, root2.left)) 
  
    return False
  
def isSymmetricBinary(root): 
    return isMirror(root, root) 


i = NetworkNode(4)
j = NetworkNode(3)
i.insert(j)
k = NetworkNode(5)
i.insert(k)
l = NetworkNode(3)
i.insert(l)
# k.insert(NetworkNode(15))
# k.insert(NetworkNode(8))
# i.insert(k)
# j.insert(NetworkNode(11))
# j.insert(NetworkNode(2))
# j.insert(NetworkNode(3))
print(i.children)
i.traverse()
print(isSymmetric(i))
