# class maxHeap():
    # def __init__(self, items=[]): #by default an empty list is produced
    #     super().__init__()
    #     self.heap = [0] # As maxHeap start at 1 index by default 0 is given at 0 index
    #     # print(self.heap)
    #     for item in items:
    #         self.heap.append(item)
    #     # print(self.heap)
        

class maxHeap():
    def __init__(self, items = []):
        super().__init__()
        self.heap = [0]
        for item in items:                              #[5, 45, 3, 6, 7, 8, 9, 100, 13, 41]
            self.heap.append(item)                      #[0, 100, 45, 9, 13, 6, 3, 8, 5, 7, 41]
            self.__floatUp(len(self.heap) - 1)          #10

    def push(self, data): # add item in the heap and if no. is greater than root then with current index to root index 
        self.heap.append(data)
        print(self.heap)
        self.__floatUp(len(self.heap) - 1)

    def peek(self): # render the root node
        if len(self.heap) > 1:    
            return self.heap[1]
        else:
            False
        
    def __floatUp(self, index): # move max no. at root node         #5
        parent = index//2                                           #2
        if index <= 1:
            return
        elif self.heap[index] > self.heap[parent]:                  #41>45
            self.__swap(index, parent)                              #[0, 100, 45, 9, 13, 41, 3, 8, 5, 7, 6]
            self.__floatUp(parent)                                  #5 

    def pop(self):
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap) - 1)
            print(self.heap)
            popValue =  self.heap.pop()
            print(self.heap)
            print('Entering to bubble down')
            self.__bubbleDown(1)
            print('Exiting from bubble down')
        elif len(self.heap) == 2:
            popValue = self.heap.pop()
        else:
            popValue = False

        return popValue, self.heap

    def __swap(self, i, j): # swap the values 
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __bubbleDown(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index 
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
            print(f'left largest : {largest}')
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right 
            print(f'right largest : {largest}')
        if largest != index:
            print(f'Not equal : largest:{largest}, index:{index}')
            print(self.heap)
            print('entering swap')
            self.__swap(index, largest)
            print(self.heap)
            print('exiting swap')
            print('Again Entering to bubble down')
            self.__bubbleDown(largest)
            print('Final Exiting from bubble down')

    def __str__(self):
        # return str((self.heap, len(self.heap)))
        return str(self.heap)


# m = maxHeap([5,10])
# print(m)
# # print(len(m.heap))

# m.push(8)
# print(m)

# m.push(45)
# print(m)

# print(m.peek())
# print(m.pop())



# m = maxHeap([88,10,34])
# print(m)
# print(len(m.heap))
# m.push(21) #add at 3rd position of the list 
# print(m)
# print(m.pop()) #remove at 2nd position of the list
# print(m)
# print(m.peek()) #will give 2nd position of the list without removing it
# print(m)

arr = [5, 45, 3, 6, 7, 8, 9, 100, 13, 41]
maxH = maxHeap(arr)
print(maxH)