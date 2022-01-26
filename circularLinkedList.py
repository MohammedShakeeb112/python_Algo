class Node:
    def __init__(self, d, n=None, p=None):
        self.data = d
        self.next = n
        self.prev = p

class CircularList:
    def __init__(self, r=None):
        self.root = r
        self.size = 0

    def add(self, d):
        if self.size == 0:
            self.root = Node(d)
            self.root.next = self.root
        else:
            new_node = Node(d, self.root.next)
            self.root.next = new_node
        self.size += 1

    def find(self, d):
        cur_node = self.root
        while True:
            if cur_node.data == d:
                return d
            elif cur_node.next == self.root:
                return False
            cur_node = cur_node.next

    def remove(self, d):
        cur_node = self.root
        prev_node = None
        while True:
            if cur_node.data == d:  #data found
                if prev_node is not None:
                    prev_node.next = cur_node.next
                else:
                    while cur_node.next != self.root:
                        cur_node = cur_node.next
                    cur_node.next = self.root.next
                self.size -= 1
                return True     #data removed
            elif cur_node.next == self.root:
                return False    #data not found
            prev_node = cur_node
            cur_node = cur_node.next

    def printList(self):
        if self.root is None:
            return 
        cur_node = self.root
        print(cur_node.data, end='->')
        while cur_node.next != self.root:
            cur_node = cur_node.next
            print(cur_node.data, end='->')
        print()

cll = CircularList()
print('size='+str(cll.size))
for i in [5,7,3,8,9]:
    cll.add(i)
print('size='+str(cll.size))
cll.printList()
# print(cll.find(8))
# print(cll.find(12))

# my_node = cll.root
# print(my_node.data)
# print(my_node.data, end='->')
# print()
# for i in range(8):
#     my_node = my_node.next
#     print(my_node.data, end='->')
# print()