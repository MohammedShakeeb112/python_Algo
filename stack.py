# FILO => FIRST_IN - LAST_OUT
# LIFO => LAST_IN - FIRST_OUT

class Stack():
    #constructor class
    def __init__(self):
        self.stack = []
    
    #push function
    def push(self, item):
        self.stack.append(item)
    
    #pop function
    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return 'No element left to pop'
    #peek function
    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack)-1]
        else:
            return 'No element left to peek'
    
    #str function
    def __str__(self):
        return str(self.stack)


myStack = Stack()
myStack.push(3)
myStack.push(4)
myStack.push(5)
myStack.push(6)
print(myStack)
# print(myStack.__str__())
print(myStack.pop())
print(myStack.pop())
print(myStack)
print(myStack.peek())
