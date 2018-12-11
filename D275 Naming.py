# This problem was asked by Epic.

# The "look and say" sequence is defined as follows: beginning with the term 1, each subsequent term visually 
# describes the digits appearing in the previous term. The first few terms are as follows:

# 1
# 11
# 21
# 1211
# 111221
# As an example, the fourth term is 1211, since the third term consists of one 2 and one 1.

# Given an integer N, print the Nth term of this sequence.

# O(n * m) with n being the Nth term, and m being the size of each term
# space complexity is O(n), but could be optimized to O(1), with just the top variable
def getTerm(n):
    l = ["1"]
    for i in range(n):
        term = l[len(l)-1]
        s = ""
        count = 1
        for i in range(len(term)-1):
            if term[i] != term[i+1]:
                s += str(count)
                s += str(term[i])
                count = 1
            else:
                count += 1
        s += str(count)
        s += str(term[-1])
        l.append(s)
    return l[n-1]

print(getTerm(4))