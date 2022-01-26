class Node:
    def __init__(self, d,  n = None, p = None):
        self.data = d
        self.next_node = n
        self.prev_node = p

    def printNode(self):
        return self.data

    def __str__(self):
        return str(self.data)


n = Node([10, 20, 30])
print(n)
print(type(n))
print(n.printNode())
print(len(n.data))
print(n.data[0])