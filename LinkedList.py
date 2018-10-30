class Node:
  def __init__(self, val):
    self.val = val
    self.next = None


class LinkedList:
    def __init__(self):
      self.head = None

    def insert(self, val):
      n = self.head
      if n == None:
        self.head = Node(val)
        return
      # n = self.head
      while n.next:
        n = n.next
      n.next = Node(val)


    def traverse(self):
      n = self.head
      while n:
        print(n.val, end = ' -> ')
        n = n.next
      print("null")

    def pop(self):
      n = self.head
      if n == None:
        return
      while n.next != None:
        n = n.next
      n.next = None

    def insertLeft(self, val):
      n = self.head
      self.head = Node(val)
      self.head.next = n

    def remove(self, val):
      n = self.head
      if n == None:
        return
      if n.val == val:
        self.head = n.next
        return
      while n.next:
          prev = n
          n = n.next
          if n.val == val:
            prev.next = n.next
          
    def removeDup(self):
      check = set()
      n = self.head
      previous = Node
      if n == None:
        return
      while n:
        if n.val in check:
          previous.next = n.next
        else:
          check.add(n.val)
          previous = n
        n = n.next

    def removeDup2(self):
      n = self.head
      while n:
        runner = n
        while runner.next:
          if runner.next.val == n.val:
            runner.next = runner.next.next
          else: 
            runner = runner.next
        n = n.next

    def kthLast(self, k):
      n = self.head
      runner = None
      for i in range(k):
        if n:
          runner = n.next
          n = n.next
      n = self.head
      while runner:
        n = n.next
        runner = runner.next
      print(n.val)
      return n
      
    def sumLists(j, k):
      num1 = ""
      num2 = ""
      p1 = j.head
      p2 = k.head
      while p1:
        num1 += (str(p1.val))
        p1 = p1.next
      while p2:
        num2 += (str(p2.val))
        p2 = p2.next
      num1 = num1[::-1]
      num2 = num2[::-1]

      num3 = int(num1) + int(num2)
      num3 = str(num3)[::-1]
      # print(num3)
      i = LinkedList()
      for c in num3:
        i.insert(int(c))
      i.traverse()
    
    def sumLists2(j, k):
      num1 = ""
      num2 = ""
      p1 = j.head
      p2 = k.head
      while p1:
        num1 += str(p1.val)
        p1 = p1.next
      while p2:
        num2 += str(p2.val)
        p2 = p2.next
      num3 = str(int(num1) + int(num2))
      i = LinkedList()
      for c in num3:
        i.insert(int(c))
      i.traverse()
    
    def reverse(self): 
        prev = None
        current = self.head 
        while(current is not None): 
            next = current.next
            current.next = prev 
            prev = current 
            current = next
        self.head = prev 

    def palindromeCheck(self):
      n = self.head
      check = ""
      if n == None:
        return
      while n:
        check += str(n.val)
        n = n.next
      if check[::-1] == check:
        return True
      else:
        return False



l = LinkedList()
l.head = Node(54)
l.insert(40)
l.insert(24)
l.insert(54)
l.insert(57)
# l.insertLeft(36)
# l.remove(36)
l.insertLeft(54)
l.insert(18)
l.insert(54)
# l.traverse()
j = LinkedList()
j.head = Node(7)
j.insert(1)
j.insert(6)
k = LinkedList()
k.head = Node(5)
k.insert(9)
k.insert(2)
# l.removeDup2()
# l.traverse()
# l.kthLast(4)
x = LinkedList()
x.insert(6)
x.insert(1)
x.insert(7)
y = LinkedList()
y.insert(2)
y.insert(9)
y.insert(5)
l.traverse()
# LinkedList.sumLists2(x, y)
t = LinkedList()
t.insert(0)
t.insert(1)
t.insert(2)
t.insert(1)
t.insert(2)
l.reverse()
l.traverse()
# print(t.palindromeCheck())

