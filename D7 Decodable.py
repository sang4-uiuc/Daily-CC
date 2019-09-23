# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

# For example, the message '111' would give 3, since it could be decoded as 'aaa, 'ka', and 'ak'.

# You can assume that the messages are decodable. For example, '001' is not allowed.

dic = {}
for i in range(1, 27):
    dic[i] = chr(96 + i)
    



def decodeable(m):
    count = [0] * (len(m) + 1)
    count[0] = 1
    count[1] = 1
    
    for i in range(2, len(m) + 1):
        if m[i - 1] > '0':
            count[i] = count[i - 1]
        if m[i - 2] == '1' or (m[i - 2] == '2' and m[i - 1] < '7'):
            count[i] += count[i - 2]
    print(count)
    return count[len(m)]


s = '1234'
print(decodeable(s))

# this one was a bit tricky, need to think in recursion of adding up previous results.