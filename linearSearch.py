a = [2,5,6,1,4,3,9,0]
key = 9

def linearSearch(num, key):
    for i in range(len(num)):
        if num[i] == key:
            return True
    return False
            
# if linearSearch(a, key):
#     print(f'{key} found in the list')
# else:
#     print(f'{key} not found in the list')


transcation = [
    {
    'name': 'reema',
    'device_id': '12AB56',
    'amount': 56
    },
    {
    'name': 'aamir',
    'device_id': '679X1',
    'amount': 123
    },
    {
    'name': 'mahesh',
    'device_id': 'E451J',
    'amount': 87
    },
    {
    'name': 'andrea',
    'device_id': '00Z77',
    'amount': 644
    }
    ]
#search device_id = 00Z77
def transaction(transaction, d_id):
    for i,e in enumerate(transaction):
        # print(e['device_id'])
        if e['device_id'] == d_id:
            return e['name'] + ' ' + str(e['amount']) + ' index is ' + str(i)
    return -1
# print(transaction(transcation, '00Z77'))

import random
random.seed(12)
numbers = [random.randint(4,13) for i in range(10)]
numbers.sort()
k = 61
# print(numbers)
# num = random.sample(range(5,19), 10)
# num.sort()
# print(num)
def linearSearch(numbers, key):
    for i in numbers:        #O(n) time complexcity
        if i == key:
            return True
    return False
if linearSearch(numbers, k):
    print(f'key {k} found in the list')
else:
    print(f'key {k} not found in the list')
