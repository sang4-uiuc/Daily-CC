# Given an array of integers out of order, determine the bounds of the 
# smallest window that must be sorted in order for the entire array to be sorted. 
# For example, given [3, 7, 5, 6, 9], you should return (1, 3).

def smallestWindow(l):
    if len(l) < 2:
        return
    # start = 0
    end = len(l) - 1
    for start in range(len(l) - 1):
        if l[start] > l[start + 1]:
            # start = i
            break
    # print(start)
    if start == end - 1:
        return "Sorted"
    for i in range(end, 0, -1):
        if l[i] < l[i - 1]:
            end = i
    
    maxx = max(l[start:end + 1])
    minn = min(l[start:end + 1])

    for i in range(start):
        if l[i] > minn:
            start = i
            break
    i = len(l) - 1
    while i > end:
        if l[i] < maxx:
            end = i
            break
        i -= 1
    # print()
    return (start, end)
l = [3, 7, 5, 6, 9]
print(smallestWindow(l))
print(smallestWindow([5,2,3,4,1,6,2]))