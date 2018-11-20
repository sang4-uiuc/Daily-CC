# This problem was asked by Apple.

# Implement the function fib(n), which returns the nth number in the Fibonacci sequence, using only O(1) space.

def fib(n):
    pre = 1
    prepre = 1
    res = 0
    if n < 0:
        return -1
    elif n <= 1:
        return 1
    else:
        for i in range(2, n+1):
            print(res)
            res = pre + prepre
            prepre = pre
            pre = res
            
    return res

print(fib(2))