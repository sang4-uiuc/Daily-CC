# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i. 
# Solve it without using division and in O(n) time.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

def ProductArray(arr):
    l = [1]
    r = [1]
    t = []
    for i in range(1, len(arr)):
        l.append(arr[i] * l[i - 1])
    for i in range(len(arr) - 1, 0, -1):
        r.append(arr[i] * r[-i + len(arr) - 1])
    # print(l)
    # print(r[::-1])
    r = r[::-1]
    l.insert(0,1)
    r.append(1)
    for i in range(len(arr)):
        t.append(l[i] * r[i])
    print(t)
    
arr = [1,2,3,4,5]
ProductArray(arr)

# this was annoying, weird way of solving it by having an array of the products to the left of i and an array of the products to the right of i
# then combining the two arrays to make the final product array