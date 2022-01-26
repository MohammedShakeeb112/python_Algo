from util import time_it

#average case 
numbers = [4, 9, 11, 17, 21, 25, 29, 32, 38]
#          0  1   2   3   4   5   6   7   8
target = 9
# print(len(numbers))

#worst case
# numbers = [i for i in range(1,1000001)]
# target = 1000000

@time_it
def linearSearch(numbers, target):
    itr = 0
    for i, e in enumerate(numbers):
        itr += 1
        if e == target:
            return i, itr
    return -1, itr
# print(linearSearch(numbers, target))

@time_it
def binarySearch(num, target):
    itr = 0
    left = 0
    right = len(num) - 1
    while left <= right:
        mid = (left + right) // 2
        itr += 1
        if num[mid] < target:
            left = mid + 1
        elif num[mid] > target:
            right = mid - 1
        else:
            return mid, itr
    return -1, itr
# print(binarySearch(numbers, target))

def binarySearchRecursive(numbers, target, left, right, itr):
    itr += 1
    if left > right:
        return - 1
    mid = (left + right) // 2
    if mid >= len(numbers) or mid < 0:
        return -1
    if numbers[mid] < target:
        left = mid + 1
    elif numbers[mid] > target:
        right = mid -1
    else:
        return mid, itr
    return binarySearchRecursive(numbers, target, left, right, itr)
# print(binarySearchRecursive(numbers, target, 0, len(numbers)-1, 0))

@time_it
def cal_square(arr):
    result = []
    for i in arr:
        result.append(i**2)
    return result

@time_it
def cal_cube(arr):
    result = []
    for i in arr:
        result.append(i**3)
    return result

arr = range(1, 11)
# print(arr)
# print(cal_square(arr))
# print(cal_cube(arr))


# Find index of all the occurances of a number from sorted list
numbers = [1, 4, 6, 9, 11, 15, 15, 15, 17, 21, 34, 34, 56]
#          0  1  2  3   4   5   6   7   8   9  10  11  12
number_to_find = 15  

#  using linearsearch method
@time_it
def occurance_linearSearch(numbers, number_to_find):
    result = []
    for i, e in enumerate(numbers):
        if e == number_to_find:
            result.append(i)
            
    # corner case
    if len(result) == 0:
        return -1
    return result 
print(occurance_linearSearch(numbers, number_to_find), 'are indices containing number 15 in the array')

def binSearch(numbers, target):
    left, right = 0, len(numbers) - 1
    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] < target:
            left = mid + 1
        elif numbers[mid] > target:
            right = mid - 1
        else:
            return mid
    return -1

@time_it
def occurance_binarySearch(numbers, number_to_find):
    index = binSearch(numbers, number_to_find)
    indices = [index]
    i = index - 1
    while i >= 0:
        if numbers[i] == number_to_find:
            indices.append(i)
        else:
            break
        i -= 1
    j = index + 1
    while j <= len(numbers) - 1:
        if numbers[j] == number_to_find:
            indices.append(j)
        else:
            break
        j += 1
    indices.sort()
    return indices

print(occurance_binarySearch(numbers, number_to_find), 'are indices containing number 15 in the array')