class Node:
    def __init__(self, d, n=None):
        self.data = d
        self.next = n

class Linkedlist:
    def __init__(self):
        self.root = None

    def add(self, d):
        self.root = Node(d, self.root)

    def add_at_end(self, d):
        if self.root is None:
            self.add(d)
        else:
            cur_node = self.root
            while cur_node.next != None:
                cur_node = cur_node.next
            cur_node.next = Node(d, cur_node.next)

    def add_at_index(self, i, d):
        if i < 0 or i >= self.get_length(): return
        if i == 0: self.root = Node(d, self.root)
        cur_node = self.root
        count = 0
        while cur_node:
            if count == i - 1:
                cur_node.next = Node(d, cur_node.next)
                return
            else:
                cur_node = cur_node.next
                count += 1

    def add_datalist_at_start(self, datalist):
        for data in datalist:
            self.add(data)

    def add_datalist_at_end(self, datalist):
        for data in datalist:
            self.add_at_end(data)
            
    def find(self, d):
        if self.root is None: return 
        cur_node = self.root
        while cur_node:
            if cur_node.data == d:
                return True
            else:
                cur_node = cur_node.next
        return False

    def print(self):
        cur_node = self.root
        while cur_node:
            print(cur_node.data, end=' -> ')
            cur_node = cur_node.next
        print(cur_node)

    def get_length(self):
        cur_node = self.root
        count = 0
        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count

if __name__ == '__main__':
    l = Linkedlist()
    l.add(65)
    print(l.find(25))
    l.print()
    print(l.get_length())
    ls = ['pineapple','banana','apple','grapes','mango','leechi']
    # l.add_datalist_at_start(ls)
    # l.print()
    l.add_datalist_at_end(ls)
    l.print()
    l.add_at_index(5, 'welcome')
    l.print()