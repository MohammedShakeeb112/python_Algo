from util import time_it

a = [5, 2, 4, 6, 3, 1] #len = 6
#    0  1  2  3  4  5
def bubbleSort(d):
    for i in range(len(d)):
        for j in range(len(d)-1-i):
            if d[j] > d[j+1]:
                d[j], d[j+1] = d[j+1], d[j]
    return d

# print(bubbleSort(a))

arr = [38, 9, 29, 7, 2, 15, 28]
#method1
@time_it
def bSort(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
        j += 1
    return arr
# print(bSort(arr))

# method 2
@time_it
def anBSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
# print(anBSort(arr))


#in built function perform far better 
@time_it
def srt():
    arr.sort()
    return arr
# print(srt())

elements = ["mona", "dhaval", "aamir", "tina", "chang"]
# elements = [5,9,2,1,67,34,88,34]
@time_it
def bubble_sort(elements):
    size = len(elements)
    for i in range(size - 1):
        swap = False
        for j in range(size - 1 - i):
            if elements[j] > elements[j+1]:
                elements[j], elements[j+1] = elements[j+1], elements[j]
                swap = True
        if not swap:
            break
    return elements
# print(bubble_sort(elements))

# ++++++++++++++++++++++++Bubble Sort Exercise+++++++++++++++++++++++++++++++++++++++++++

# Modify bubble_sort function such that it can sort following list of transactions happening in an electronic store,
elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]
# bubble_sort function should take key from a transaction record and sort the list as per that key. For example,
# bubble_sort(elements, key='transaction_amount')
def bubble_sort(elements, key = 'transaction_amount'):
    size = len(elements)
    for i in range(size - 1):
        swap = False
        for j in range(size - 1 - i):
            if elements[j][key] > elements[j+1][key]:
                elements[j], elements[j+1] = elements[j+1], elements[j]
                swap = True
        if not swap:
            break
    return elements
print(bubble_sort(elements))

# This will sort elements by transaction_amount and your sorted list will look like,
elements = [
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
    ]

print(bubble_sort(elements, key='name'))