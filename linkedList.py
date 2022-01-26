#LinkedList --> Add, find, remove, print 


class Node:
    def __init__(self, d, n = None, p = None):
        self.data = d
        self.next_node = n
        # print(f'self.next_node : {self.next_node}')
        self.prev_node = p

    def printNode(self):
        return self.data

# n = Node([1, 2, 3])
# print(n.printNode())

class LinkedList:
    def __init__(self, r = None):
        self.root = r
        self.size = 0

    def add(self, d):
        this_node = Node(d, self.root)
        self.root = this_node
        self.size += 1  

    def find(self, d):
        this_node = self.root
        while this_node is not None:
            if this_node.data == d:
                return d
            else:
                this_node = this_node.next_node
        return 'no. not in the node'

    def remove(self, d):
        this_node = self.root
        prev_node = None
        while this_node is not None:
            if this_node.data == d: 
                if prev_node is not None: # data is not in root node
                    prev_node.next_node = this_node.next_node
                    print('-'*75)
                    print(prev_node.data)
                    print(prev_node.next_node.data)
                    print(this_node.data)
                    print(this_node.next_node.data)
                    print('-'*75)
                else:
                    self.root = this_node.next_node # data in root node
                self.size -= 1
                return True
            else:
                prev_node = this_node
                this_node = this_node.next_node    
        return False

    def printLinkedList(self):
        this_node = self.root
        while this_node is not None:
            print(this_node.data, end='->')
            this_node = this_node.next_node
        print('None')


# l = LinkedList()
# l.add(25)
# # l.printLinkedList()
# l.add(20)
# l.add(42)
# l.add(36)
# l.add(23)
# l.printLinkedList()
# # print(l.find(27))
# print(l.remove(36))
# l.printLinkedList()
# print(l.remove(23))
# l.printLinkedList()
# print(l.remove(65))



class Node:
    def __init__(self, d, n=None, p=None):
        self.data = d
        self.next = n
        self.prev = p

class LinkedList:
    def __init__(self, r=None):
        self.root = r
        self.size = 0

    def add_at_start(self, d):
        self.root = Node(d, self.root)
        self.size += 1

    def add_at_end(self, d):
        if not self.root:
            self.root = Node(d, self.root)
        else:
            cur_node = self.root
            while cur_node.next != None:
                cur_node = cur_node.next
            cur_node.next = Node(d, cur_node.next)
        self.size += 1

    def add_list_at_start(self, datalist):
        self.root = None
        for data in datalist:
            self.add_at_start(data)

    def add_list_at_end(self, datalist):
        # self.root = None
        for data in datalist:
            self.add_at_end(data)

    def add_at_index(self, d):
        cur_node = self.root
        if d < 0 and d > self.getlength(): return False
        
        count = 0
        while cur_node:
            if count == d:
                pass

    def find(self, d):
        cur_node = self.root
        while cur_node:
            if cur_node.data == d:
                return True
            else:
                cur_node = cur_node.next
        return False

    def remove(self, d):
        cur_node = self.root
        prev_node = None
        while cur_node:
            if cur_node.data == d:
                if prev_node:
                    prev_node.next = cur_node.next
                else:
                    self.root = cur_node.next
                self.size -= 1
                return True
            else:
                prev_node = cur_node
                cur_node = cur_node.next
        return False
    
    def remove_at(self, i):
        if i<0 or i>=self.getlength():
            raise Exception("Invalid Index")

        if i==0:
            self.root = self.root.next
            return

        count = 0
        itr = self.root
        while itr:
            if count == i - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count+=1


    def printlist(self):
        cur_node = self.root
        while cur_node:
            print(cur_node.data, end='->')
            cur_node = cur_node.next
        print(cur_node)

    def getlength(self):
        cur_node = self.root
        count = 0
        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count    

l = LinkedList()
# l.add_at_end(45)
# l.add_at_end(55)
# l.add_at_start(35)
# l.add_at_start(25)
# l.add_at_start(15)
# l.printlist()
# print(l.find(15))
# print(l.find(55))
# print(l.find(65))
# l.printlist()
# print(l.remove(15))
# l.printlist()
# print(l.remove(55))
# l.printlist()
# print(l.remove(35))
# l.printlist()
# print(l.remove(65))

# l.add_list_at_start(['red','blue','green','yellow','purple','violet'])
# l.printlist()
# l.add_list_at_end([25,35,45])
# l.printlist()
# # print(l.getlength())
# print(l.remove_at(0))
# l.printlist()
# l.remove_at(6)
# l.printlist()
datalist = [1,2,3,4,5]
datalist=list(reversed(datalist))
l.add_list_at_start(datalist)
# l.printlist()
# l.remove_at(3)
# l.printlist()



class Node:
    def __init__(self, d, n=None):
        self.data = d
        self.next = n

class LinkedList:
    def __init__(self):
        self.root = None

    def add(self, d):
        node = Node(d, self.root)
        self.root = node

    def add_at_end(self, d):
        if self.root is None:
            self.add(d)
            return
        itr = self.root
        while itr.next:
            itr = itr.next
        itr.next = Node(d, itr.next)

    def add_datalist(self, datalist):
        self.root = None
        for data in datalist:
            self.add_at_end(data)
        return

    def insert_at(self, index, d):
        if index < 0 or index >= self.get_length(): 
            raise Exception('Invalid index')
        if index == 0:
            self.add(d)
            return
        
        itr = self.root
        count = 0
        while itr:
            if count == index - 1:
                itr.next = Node(d, itr.next)
                break
            itr = itr.next
            count += 1
        

    def get_length(self):
        count = 0
        itr = self.root
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid index')
            
        if index == 0:
            self.root = self.root.next
            return

        count = 0
        itr = self.root
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1


    def printlist(self):
        lstr = ''
        itr = self.root
        while itr:
            lstr += str(itr.data) + '->'
            itr = itr.next
        print(lstr)

if __name__ == '__main__':
    l = LinkedList()
    l.add(52)
    l.add_at_end(41)
    l.add_at_end(63)
    l.add_datalist([56,72,96])
    l.printlist()
    print(l.get_length())
    l.remove_at(2)
    l.insert_at(0, 24)
    l.printlist()
    l.insert_at(2, 63)
    l.printlist()