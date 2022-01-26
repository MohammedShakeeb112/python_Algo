def insertionSort(el):
    if len(el) == 0:
        return -1
    if len(el) == 1:
        return el
    for i in range(1, len(el)):     #4      range(1,7)
        check = el[i]  #2
        j = i - 1 #3
        while j >= 0 and check < el[j]:     # 0>=0 and 2 < 7
            el[j+1] = el[j]         # 4=29,3=11,2=9,1=7
            j -= 1                  # -1
        el[j+1] = check     # 0 = 2   
    return el                       # [2, 7, 9, 11, 29, 15, 28]
                                    #  0   1   2  3  4   5   6
# if __name__ == '__main__':
#     elements = [11, 9, 29, 7, 2, 15, 28]
#     print(insertionSort(elements))
#     tests = [
#         [21, 38, 29, 17, 4, 25, 11, 32, 9],
#         [3, 7, 9, 11],
#         [25, 22, 21, 10],
#         [29, 15, 28],
#         [],
#         [6]
#     ]
    # for i in tests:
    #     print(insertionSort(i))

# Exercise: Insertion Sort
# Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.
# Recall that the median of an even-numbered list is the average of the two middle numbers in a sorted list.
# For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:
# 2
# 1.5
# 2
# 3.5
# 2
# 2
# 2
# def insertion_sort(elements):
#     for i in range(1, len(elements)):
#         el = elements[i]
#         j = i-1
#         while j >= 0 and el < elements[j]:
#             elements[j+1] = elements[j]
#             j -= 1
#         elements[j+1] = el
#     return elements
# el = [2, 1, 5, 7, 2, 0, 5]
# # sorted    [0,  1,  2,   2,   5,  5,  7]
# #   idx      0   1   2    3    4   5   6
# # median     2  1.5  2   3.5   2   2   2
# print(insertion_sort(el))


def place_to_insert(array, key):
    index = 0
    for i in array:
        if i > key:
            break
        else:
            index += 1
    return index


def insert_to_sorted(array, key):
    index = place_to_insert(array, key)
    return array[0:index]+[key]+array[index:]


if __name__ == "__main__":
    array = [2, 1, 5, 7, 2, 0, 5]

    stream = []

    count = 0
    while(True):
        i = int(input())
        count += 1
        stream = insert_to_sorted(stream, i)
        if count % 2 == 1:
            print(f"Median of {stream} : {stream[(count)//2]}")
        else:
            i1 = count//2
            i2 = (count//2) - 1
            print(f"Median of {stream} : {(stream[i1] + stream[i2])/2}")