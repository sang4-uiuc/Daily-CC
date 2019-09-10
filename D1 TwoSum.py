# Given an array of numbers, return whether any two sums to K.

# For example, given [10, 15, 3, 7] and K of 17, return true since 10 + 7 is 17.
import time
import random
def main():
    def twoSum(arr, k):
        s = set()
        for i in arr:
            if (k - i) in s:
                return True
            else:
                s.add(i)
        return False
    a = []
    for i in range(random.randint(10,20)):
        a.append(random.randint(1, 20))
        
    b = random.randint(20,40)
    print(twoSum(a,b))

start_time = time.time()
for i in range(100):
    main()
print("--- %s seconds ---" % (time.time() - start_time))