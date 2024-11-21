# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 19:21:43 2024

@author: atul.sharma
"""

print("cookbook Chapter1")

# move all the zero begining of the array

arr = [0, 1, 2, 0, 4, 3, 0, 5, 0]

j = 0

for i in range(1, len(arr)):
    if not arr[i]:
        arr[j], arr[i] = arr[i], arr[j]
        j += 1

# print(arr)
# ----------------------------------------------------------------
# move all the zero at the end of array

arr1 = [0, 1, 2, 0, 4, 3, 0, 5, 0]

n = len(arr1)

j = n - 1
i = 0
while i < j:
    if not arr1[j]:
        j -= 1
        continue

    if not arr1[i]:
        arr1[j], arr1[i] = arr1[i], arr1[j]
        j -= 1
    i += 1
# print(arr1)
# ----------------------------------------------------------------

'''
# diffrence  between set and get default
# set default adds key in dict if it is not available
# get only return the value does not add anything
'''

d = dict()

# print(d.get('missing key','default_value_0'))

# print(d.setdefault('missing_key','default_value_1'))

# print(d)

try:
    d['e_missing_key']
except KeyError:
    d['e_missing_key'] = 'e_default_value'
# print(d)

# ----------------------------------------------------------------

list1 = [1, 2, 3, 45, 47, 2323, 67, 1, 22244, 6666666, 23, 454, 0, 444444444]

from collections import defaultdict

d1 = defaultdict(list)

for elem in list1:
    n = len(str(elem))
    d1[n].append(elem)

# print(d1)

# ----------------------------------------------------------------
d3 = {}

for ele in list1:
    k = len(str(ele))
    d3.setdefault(k, []).append(ele)

# print(d3)

# -------------------------------------------------------------------------------
'''sliding window'''
# max  sum of K size window
list1 = [1, 2, 5, 7, 4, 9, 0, 3, 12, 0, 5, -5]
n = len(list1)
i = 0
K = 3

max_value = 0
for j in range(1, n):
    if j - i + 1 < K:
        continue
    if j - i + 1 == K:
        sum1 = sum(list1[i:j + 1])
        max_value = max(max_value,sum1)
        i += 1

# print(max_value)#20

# ----------------------------------------------------------------
window_sum = sum(list1[0:K])
max_sum = window_sum
# print(window_sum)
for i in range(n - K):
    window_sum = window_sum + list1[K + i] - list1[i]
    max_sum = max(max_sum, window_sum)

# print(max_sum)

# ----------------------------------------------------------------

'''# first negative in K size window'''

list2 = [12, -3, -5, 7, 8, 9, -1, 0, -2, 10, 11, 11]
res = []
n = len(list2)
i = 0

for j in range(1, n):
    if j - i + 1 < K:
        continue
    if j - i + 1 == K:
        # print(list2[i:j+1])
        if len(list2[i:j + 1]) == len([x for x in list2[i:j + 1] if x > 0]):
            res.append(0)
        for ele in list2[i:j + 1]:
            if ele < 0:
                res.append(ele)
                break
        i += 1
print(res)
# print(neg_num)
# ----------------------------------------------------------------
#































