# # Hoare partition Scheme, Lomuto partition Scheme

# ++++++++++++++++++++++ HOARE PARTITION SCHEME ++++++++++++++++++++++++++
# swap on basis of ascending order
def swap(el, start, end):
    if start != end:
        el[start], el[end] = el[end], el[start]

# partition the elements on ascending order
def partition(el, start, end):
    pivot_idx = start
    pivot = el[pivot_idx]
    while start < end:
        while start < len(el) and el[start] <= pivot:
            start += 1
        while el[end] > pivot:
            end -= 1
        if start < end:
            swap(el, start, end)
    swap(el, pivot_idx, end)
    return end

    # main function to arrange in ascending order
def quickSort(el, start, end):
    # corner case
    if len(el) == 0:
        return -1
    if len(el) == 1:
        return el
    if start < end:
        pi = partition(el, start, end)
        #for left partition
        quickSort(el, start, pi-1)
        #for right partition
        quickSort(el, pi+1, end)
    return el

# if __name__ == '__main__':
#     elements = [11, 9, 29, 7, 2, 15, 28]
#     #           0   1   2  3  4   5   6
#     print(quickSort(elements, 0, len(elements)-1))
#     tests = [
#         [11,9,29,7,2,15,28],
#         [3, 7, 9, 11],
#         [25, 22, 21, 10],
#         [29, 15, 28],
#         [],
#         [6],
#         ["mona", "dhaval", "aamir", "tina", "chang"]
#     ]
#     for el in tests:
#         print(quickSort(el, 0, len(el)-1))

# ++++++++++++++++ LOMUTO PARTITION SCHEME ++++++++++++++++++++++++++

def swap(el, start, end):
    if start != end:
        el[start], el[end] = el[end], el[start]
def partition(el, start, end):
    p_idx = start
    pivot = el[end]
    for i in range(start, end):
        if el[i] <= pivot:
            swap(el, i, p_idx)
            p_idx += 1
    swap(el, p_idx, end)
    return p_idx    

def quickSortLPS(el, start, end):
    if len(el) == 0:
        return -1
    if len(el) == 1:
        return el
    if start < end:
        pi = partition(el, start, end)
        quickSortLPS(el, start, pi-1)
        quickSortLPS(el, pi+1, end)

    return el

if __name__ == '__main__':
    elements = [11, 9, 29, 7, 2, 15, 28]
    #           0   1   2  3  4   5   6
    print(quickSortLPS(elements, 0, len(elements)-1))
    tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6],
        ["mona", "dhaval", "aamir", "tina", "chang"]
    ]
    for e in tests:
        print(quickSortLPS(e, 0, len(e)-1))