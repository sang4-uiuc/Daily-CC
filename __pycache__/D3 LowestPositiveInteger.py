# Given an array of integers, find the first missing positive integer in linear time and constant space. 
# In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

# You can modify the input array in-place.


def lowestPositiveIntegerHashWay(arr):
    dic = {}
    m = 0
    for i in arr:
        if i > m:
            m = i
        dic[i] = 1
    for i in range(1, m):
        if i in dic.keys():
            continue
        else:
            return i
    return m + 1


def lowestPositiveInteger(arr):
    m = max(arr)
    if m < 1:
        return 1
    if len(arr) == 1:
        return 2 if arr[0] == 1 else 1
    l = [0] * m
    for i in range(len(arr)):
        if arr[i] > 0:
            if l[arr[i] - 1] != 1:
                l[arr[i] - 1] = 1

    for i in range(len(l)):
        if l[i] == 0:
            return i + 1

    return i + 2

arr = [1,2,3,4,5,6,7,8,9,27]
print(lowestPositiveInteger(arr))
        
# very interesting concept of solving it, I couldn't think of this myself at first.
# basically have another array from 1 to max, and mark the index 1 to indicate that number exists in the origianl array
# go through it and the first one with 0 is the smallest integer, if they are all filled, then i + 2