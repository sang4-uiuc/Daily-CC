# An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

# If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.


dic = {}
class Node:
    
    def __init__(self, data = None):
        self.npx = None
        self.data = data
        dic[id(self)] = self
        

    def add(self, n):
        # this line is fucked
        prev_add = self.npx ^ id(self) if self.npx is not None else 0
        n.npx = id(self) ^ 0
        print(prev_add, id(n), id(self))
        self.npx = prev_add ^ id(n)
        
        
        

a = Node(5)
b = Node(6)
c = Node(7)
d = Node(8)
a.add(b)
b.add(c)
c.add(d)
# print(a.npx)

# print(id(d))

for key, val in dic.items():
    print(key, val.npx, val.data)

def traverse(root, prev_add):
    next_add = root.npx ^ prev_add
    print(id(root), root.npx, root.data)
    print(root.npx, prev_add)
    print(next_add)
    if next_add == 0:
        return
    traverse(dic[next_add], id(root))

    
traverse(a, 0)

# this took way too much time, like over an hour. I can't wrap my head around how to get the previous address