# # [1, 6, 2, 7, 12, 9, 17, 23, 21, 53, 78, 61, 89]
# # 0 1  2  3   4  5  6   7   8   9   10  11  12

# SHELL_SORT is an optimization over INSERTION_SORT
def shell_Sort(arr):
    size = len(arr)         #13
    gap = size // 2         #6
    while gap > 0:
        for i in range(gap, size):    #6-13
            anchor = arr[i]           #1
            j = i                     #12
            while j >= gap and arr[j-gap] > anchor:     #6>=6 and 17>1
                arr[j] = arr[j-gap]                     # [1, 12, 9, 7, 6, 2, 17, 78, 61, 53, 23, 21, 89]
                j -= gap                                #  0   1  2  3  4  5   6   7  8   9   10  11  12
            arr[j] = anchor
        gap = gap//2
    

# if __name__ == '__main__':
    # elements = [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1]
              #   0   1   2   3    4   5   6   7  8  9  10 11 12
#     tests = [
#         [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1],
#         [],
#         [1,5,8,9],
#         [234,3,1,56,34,12,9,12,1300],
#         [5]
#     ]
#     for elements in tests:
#         shell_Sort(elements)
#         print(elements)


def dub_Shell_Sort(el):
    size = len(el)
    div = 2
    gap = size // div
    while gap > 0:
        idx_del = []
        for i in range(gap, size):
            anchor = el[i]
            j = i
            while j >= gap and el[j-gap] >= anchor:
                if el[j-gap] == anchor:
                    idx_del.append(j)
                el[j] = el[j-gap]
                j -= gap
            el[j] = anchor
        gap = gap // 2
        idx_del = list(set(idx_del))
        idx_del.sort()
        if idx_del:
            for i in idx_del[::-1]:
                del el[i]

        div *= 2
        size = len(el)
        gap = size // div
    return el

print(dub_Shell_Sort([2, 1, 5, 7, 2, 0, 5, 1, 2, 9, 5, 8, 3]))