# first/root  value will be the SMALLEST
# 1ST property follows for every node
# complete binary tree

# pos = 6
# 1st child = (2*pos)+1         => (2*6)+1=13
# 2nd child = (2*pos)+2         => (2*6)+2=14
# parent = (pos-1)//2           =>parent of 13 = (13-1)//2 = 6, parent of 14 = (14-1)//2 = 6
# 
#                             MIN_HEAP                                                
#                               ___                            ============================================ 
#                              | 7 |       LEVEL 0             ||  CONDITION: PARENT must be < CHILDNODE  ||
#                               ---                            ============================================= 
#                             /     \   
#                            /       \
#                     ____             ____   
#                    | 11 |           | 23 |       LEVEL 1
#                     ----             ----
#                  /        \          /   \ 
#                 /          \        /     \
#              ____         ____      ____    ____ 
#             | 17 |       | 31 |    | 30 |  | 49 |    LEVEL 2
#              ----         ----      ----    ----
#             /    \ 
#            /      \
#          _____    ____
#         | 101 |  | 18 |             LEVEL 3
#                               -----    ----
#   left -> right = [3, 11, 23, 17, 31, 30, 49, 101, 181]      Array Representation
#   level 0 to level n = [3, 11, 23, 17, 31, 30, 49, 101, 181]  Tree Representation     
# 
# OPERATION OF MINHEAP               
# -> PEEK   => independent => return the root value/ value at 0th index/ minimum value of array/ minHeap 
# -> INSERT => SIFT_UP  =>    
# -> REMOVE, BUILD_HEAP => SIFT_DOWN =>
# Insert => number 5
#       1.  Append the new_value at the end of the array
#       2.  Idx -> index where the  new_value is stored
#       3.  compute the parent idx of the cur idx
#       4.  compare the value of number at the parent idx and cur idx
#       5.  if numParIdx > numCurIdx -> SWAP


# ===================INSERT a value is said to be SIFT_UP OPERATION=================================== 
#  1. inserted 5 in 31's childNode 
#                                         7
#                                     /         \
#                                  11             23
#                               /    \          /      \
#                            17        31      30       49
#                          /    \       /
#                       101     18     5       
# 
# 2. check if 31 >5 then swap
#                                          7
#                                     /         \
#                                  11             23
#                               /    \          /      \
#                            17        5      30       49
#                          /    \       /
#                       101     18     31       
#         
# 
# 3. check if 11 >5 then swap
# 
#                                          7
#                                     /         \
#                                  5             23
#                               /    \          /      \
#                            17        11      30       49
#                          /    \       /
#                       101     18     31
# 
# 
# 
# 4. check if 7 >5 then swap
#                                          5
#                                     /         \
#                                  7             23
#                               /    \          /      \
#                            17        11      30       49
#                          /    \       /
#                       101     18     31       
# 
# 
#                                   REMOVE OR BUILD_HEAP
# REMOVE CAN BE DONE FROM ROOT OR MIN_HEAP VALUE
# ====================================SIFT_DOWN OPERATION====================================
#                               7
#                           /       \
#                         11        23
#                       /   \       /   \
#                     17     31     30   49
#                   /   \     /  
#                  101  18   45     
# 
# 1. swap the root value with end value
#                               45
#                           /       \
#                         11        23
#                       /   \       /   \
#                     17     31     30   49
#                   /   \     /  
#                  101  18   7
# 
# 2. now root value is at the end of tree    
# 
#                               45
#                           /       \
#                         11        23
#                       /   \       /   \
#                     17     31     30   49
#                   /   \     /  
#                  101  18   7
# 
# 3. pop the last_value from the tree
#                               45
#                           /       \
#                         11        23
#                       /   \       /   \
#                     17     31     30   49
#                   /   \       
#                  101  18   
# 
# 4. SWAP_DOWN from the root idx
#                               11
#                           /       \
#                         45        23
#                       /   \       /   \
#                     17     31     30   49
#                   /   \      
#                  101  18   
# 
# 5. SWAP_DOWN from rootChild till end 
# 6. SWAP_DOWN  
#                               11
#                           /       \
#                         17        23
#                       /   \       / \
#                     18     31    30  49
#                   /   \       
#                  101  45   
# 
# 
# C1_idx = (p_idx * 2) + 1
# C2_idx = (p_idx * 2) + 2 
# check if C2_idx not exist in tree   C2_idx <= end_idx
# end_idx = len(heap or tree) - 1
# 
#                           BUILD_HEAP
#   0   1   2   3   4   5   6   7   8   9   
# [100, 5, 45,  3,  6,  7,  8,  9,  13, 41]
#   
# 1. consider the recent parent
# 2. msuppose recent parent at index idx
# 3. loop through from idx till 0            
#       a) for every idx perform SIFT_DOWN operations
# 
# 
# 
# 
# 
# 
# 
#   =======================================================================================================================

#                                                              ==========================================             
#                               MAX_HEAP                       || CONDITION: PARENT must be > CHILDNODE ||   
#                                 _____                        ==========================================     
#                                | 181 |              LEVEL 0
#                                 -----
#                                /     \
#                               /       \
#                           _____       ____
#                          | 101 |     | 49 |         LEVEL 1  
#                           -----       ----
#                          /    \        /   \
#                         /      \      /     \
#                      ____    ____     ____    ____
#                     | 31 |  | 17 |   | 30 |  | 23 |     LEVEL 2
#                      ----    ----     ----    ---- 
#                       / \
#                      /   \
#                   ____   ___
#                  | 11 | | 7 |            LEVEL 3
#                   ----   ---    
#    left to right = [181, 101, 49, 31, 17, 30, 23, 11, 7]      Array Representation
#    level 0 to level n = [181, 101, 49, 31, 17, 30, 23, 11, 7]    Tree Representation


# operation in MINHEAP
# PEEK => independent
# INSERT => depend on SIFT_UP
# BUILD_HEAP, REMOVE => depends on SIFT_DOWN

class minHeap:
    def __init__(self, items=[]):
        self.heap = [0]
        for item in items:                              # 0  1  2  3  4    5  6   7  8
            self.heap.append(item)                      #[0, 3, 5, 7, 9, 6, 45, 8, 100, 13, 41]
            self.floatup(len(self.heap) - 1)            #9

    def floatup(self, idx):                             #9
        parent = (idx - 1) // 2                               #4
        if idx <= 1: return                             
        elif self.heap[idx] < self.heap[parent]:        #13<9
            self.swap(idx, parent)                      #[0, 3, 5, 7, 9, 6, 45, 8, 100]
            self.floatup(parent)                        #4

    def swap(self ,i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


    def __str__(self):
        return str(self.heap[1:])


arr = [100, 5, 45, 3, 6, 7, 8, 9, 13, 41]
#       0   1   2  3  4  5  6  7   8   9
minH = minHeap(arr)
# print(minH)


class maxHeap:
    def __init__(self, items = []):
        self.heap = [0]
        for item in items:
            self.heap.append(item)
            self.floatup(len(self.heap) - 1)
    
    def floatup(self, idx):
        p_idx = (idx) // 2
        if idx <= 1: return
        elif self.heap[idx] > self.heap[p_idx]:
            self.swap(idx, p_idx)
            self.floatup(p_idx)

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __str__(self):
        return str(self.heap[1:])

arr = [5, 45, 3, 6, 7, 8, 9, 100, 13, 41]
#       0   1   2  3  4  5  6  7   8   9
maxH = maxHeap(arr)
print(maxH)