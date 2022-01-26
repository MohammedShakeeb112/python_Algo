# LILO => LAST_IN - LAST_OUT
# FIFO => FIRST_IN - FIRST_OUT

# Enqueue will add item to the end of the line
# Dequeue will remove item from the front of the line

# use append() to enqueue an item 
# popleft() to dequeue an item

# from collections import deque #collections module 

# myqueue = deque()
# myqueue.append(24)
# myqueue.append(25)
# myqueue.appendleft(23) #add at first index of the list

# print(myqueue)
# print(myqueue.pop()) #remove last item of the list
# print(myqueue.popleft()) #remove first item of the list


# wrapper class Queue
class Queue():
    #constructor class
    def __init__(self) -> None:
        self.queue = []

    # Enqueue an item 
    def enqueue(self, item):
        self.queue.append(item)

    # Dequeue an item 
    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        else:
            return "List is empty"

    def print(self):
        print(self.queue)


myQueue = Queue()
myQueue.enqueue(23)
myQueue.enqueue(24)
myQueue.enqueue(25)

myQueue.print()

myQueue.dequeue()

myQueue.print()