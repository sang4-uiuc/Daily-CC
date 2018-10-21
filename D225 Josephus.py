# This problem was asked by Bloomberg.

# There are N prisoners standing in a circle, waiting to be executed. 

# The executions are carried out starting with the kth person, and removing 
# every successive kth person going clockwise until there is no one left.

# Given N and k, write an algorithm to determine where a prisoner should stand in order to be the last survivor.

# For example, if N = 5 and k = 2, the order of executions would be [2, 4, 1, 5, 3], so you should return 3.

# Bonus: Find an O(log N) solution if k = 2.

def josephus(n, k):
    
    if n == 1:
        return 1
    elif k == 2:
        return josephus2k(n)
    else:
        # After the first person (kth from begining) is killed,
        #  n-1 persons are left. So we call josephus(n – 1, k) to get the position with n-1 persons. 
        #  But the position returned by josephus(n – 1, k) will consider the position starting from k%n + 1. 
        #  So, we must make adjustments to the position returned by josephus(n – 1, k).
        return (josephus(n - 1, k) + k-1) % n + 1
    # quite difficult to grasp this one line that kinda compensates everything

def josephus2k(n): 
      
    # Find value of 2 ^ (1 + floor(Log n)) 
    # which is a power of 2 whose value 
    # is just above n. 
    p = 1
    while p <= n: 
        p *= 2
  
    # Return 2n - 2^(1 + floor(Logn)) + 1 
    return (2 * n) - p + 1

print(josephus(17,2))