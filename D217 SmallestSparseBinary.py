# We say a number is sparse if there are no adjacent ones in its binary representation. 
# For example, 21 (10101) is sparse, but 22 (10110) is not. 
# For a given input N, find the smallest sparse number greater than or equal to N.

# Do this in faster than O(N log N) time.

def findSmallSparse(n):
    s = dec_to_bin(n)
    print(s)
    for i in range(len(s) -1):
        if s[i] == s[i+1]:
            return findSmallSparse(n + 1)
    return n, "Sparse"

            


def dec_to_bin(x):
    return bin(x)[2:]

print(findSmallSparse(4))