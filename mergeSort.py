# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr)//2
#     left = arr[:mid]
#     right = arr[mid:]
#     left = merge_sort(left)
#     right = merge_sort(right)
#     return merge_two_sorted_lists(left, right)

# def merge_two_sorted_lists(a, b):
#     sorted_list = []
#     len_a = len(a)
#     len_b = len(b)
#     i = j = 0
#     while i < len_a and j < len_b:
#         if a[i] <= b[j]:
#             sorted_list.append(a[i])
#             i += 1
#         else:
#             sorted_list.append(b[j])
#             j += 1

#     while i < len_a:
#         sorted_list.append(a[i])
#         i += 1

#     while j < len_b:
#         sorted_list.append(b[j])
#         j += 1
#     return sorted_list

# if __name__ == '__main__':
#     arr = [10,3,15,7,8,23,98,29]

#     print(merge_sort(arr))


def merge_sort(arr):                        #[10, 3, 15, 7, 8, 23, 98, 29]
    if len(arr) <= 1:                       #  0  1   2  3  4  5   6   7          
        return
    mid = len(arr) // 2
    left = arr[:mid]                        #[3, 7, 10, 15]                  
    right = arr[mid:]                       #[8, 23, 29, 98]                
    merge_sort(left)
    merge_sort(right)

    merge_two_sort_list(left, right, arr)   #[3, 7, 10, 15], [8, 23, 29, 98], [10, 3, 15, 7, 8, 23, 98, 29]

def merge_two_sort_list(l, r, arr):   #[3, 7, 10, 15], [8, 23, 29, 98], [10, 3, 15, 7, 8, 23, 98, 29]
    i = j = k = 0
    len_l = len(l)      #4
    len_r = len(r)      #4
    while i < len_l and j < len_r:  #4<4 and 1<4
        if l[i] <= r[j]:            #15 <= 23 t
            arr[k] = l[i]           #[3, 7, 8, 10, 15, 23, 98, 29]
            i+=1                    #i=4,j=1,k=5
        else:
            arr[k] = r[j]           #[3, 7, 8, 7, 8, 23, 98, 29]
            j+=1                    #i=2,j=1,k=3
        k+=1

    while i < len_l:                
        arr[k] = l[i]               #[29, 98]
        i+=1                        #i=1,j=1,k=2
        k+=1

    while j < len_r:                #3<4
        arr[k] = r[j]               #[3, 7, 8, 10, 15, 23, 29, 98]
        j+=1                        #i=4,j=3,k=7
        k+=1

if __name__ == '__main__':
    test_cases = [
        [10, 3, 15, 7, 8, 23, 98, 29],
        [],
        [3],
        [9,8,7,2],
        [1,2,3,4,5]
    ]

    # for arr in test_cases:
    #     merge_sort(arr)
    #     print(arr)



# ++++++++++++++++++++++++MERGE_SORT_EXERCISE+++++++++++++++++++++++++++++++++++
# Modify merge_sort function such that it can sort following list of athletes as per the time taken by them in the marathon,
# elements = [
#         { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
#         { 'name': 'rajab', 'age': 12,  'time_hours': 3},
#         { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
#         { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
#     ]
# merge_sort function should take key from an athlete's marathon log and sort the list as per that key. For example,
# merge_sort(elements, key='time_hours', descending=True)
# This will sort elements by time_hours and your sorted list will look like,
# elements = [
#         {'name': 'rajab', 'age': 12, 'time_hours': 3},
#         {'name': 'vignesh', 'age': 21, 'time_hours': 2.5},
#         {'name': 'chinmay', 'age': 24, 'time_hours': 1.5},
#         {'name': 'vedanth', 'age': 17, 'time_hours': 1},
#     ]
# But if you call it like this,
# merge_sort(elements, key='name')
# output will be,
# elements = [
#         { 'name': 'chinmay',   'age': 24, 'time_hours': 1.5},
#         { 'name': 'rajab', 'age': 12,  'time_hours': 3},
#         { 'name': 'vedanth',  'age': 17,  'time_hours': 1},
#         { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
#     ]

# def merge_Sort(arr, key, descending=False):
#     if len(arr) <= 1:
#         return
#     mid = len(arr) // 2
#     left = arr[:mid]
#     right = arr[mid:]
#     merge_Sort(left, key, descending)
#     merge_Sort(right, key, descending)
#     merge_Two_Sort_List(left, right, arr, key, descending)

# def merge_Two_Sort_List(l, r, arr, key, descending=False):
#     len_l = len(l)
#     len_r = len(r)
#     i = j = k = 0
#     if descending:
#         while i < len_l and j < len_r:
#             if l[i][key] >= r[j][key]:
#                 arr[k] = l[i]
#                 i+=1
#             else:
#                 arr[k] = r[j]
#                 j+=1
#             k+=1

#         while i < len_l:
#             arr[k] = l[i]
#             i+=1
#             k+=1
        
#         while j < len_r:
#             arr[k] = r[j]
#             j+=1
#             k+=1 
#     else:
#         while i < len_l and j < len_r:
#             if l[i][key] <= r[j][key]:
#                 arr[k] = l[i]
#                 i+=1
#             else:
#                 arr[k] = r[j]
#                 j+=1
#             k+=1

#         while i < len_l:
#             arr[k] = l[i]
#             i+=1
#             k+=1
        
#         while j < len_r:
#             arr[k] = r[j]
#             j+=1
#             k+=1

# OPTIMIZED SOLUTION
def merge_Sort(elements, key, descending=False):
    size = len(elements)

    if size == 1:
        return elements

    left_list = merge_Sort(elements[0:size//2], key, descending)
    right_list = merge_Sort(elements[size//2:], key, descending)
    sorted_list = merge(left_list, right_list, key, descending)

    return sorted_list

    
def merge(left_list, right_list, key, descending=False):
    merged = []
    if descending:
        while len(left_list) > 0 and len(right_list) > 0:
            if left_list[0][key] >= right_list[0][key]:
                merged.append(left_list.pop(0))
            else:
                merged.append(right_list.pop(0))

    else:
        while len(left_list) > 0 and len(right_list) > 0:
            if left_list[0][key] <= right_list[0][key]:
                merged.append(left_list.pop(0))
            else:
                merged.append(right_list.pop(0))

    merged.extend(left_list)
    merged.extend(right_list)
    return merged


if __name__ == '__main__':
    elements = [
        { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
        { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
    ]
    merge_Sort(elements, 'time_hours', True)
    # merge_Sort(elements, 'name')
    # print(elements)
    print(merge_Sort(elements, 'time_hours', True))