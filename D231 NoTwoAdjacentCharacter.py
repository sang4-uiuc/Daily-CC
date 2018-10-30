# This problem was asked by IBM.

# Given a string with repeated characters, rearrange the string so that no two adjacent characters are the same. If this is not possible, return None.

# For example, given "aaabbc", you could return "ababac". Given "aaab", return None.

def noAdjacent(s):
    dic = {}
    output = ""
    for char in s:
        dic.get(char, 0) + 1
    l = dic.values()
    most_count = max(l)
    rem_count = sum(l) - max(l)
    if most_count - rem_count > 1:
        return None
    else:
        for key, value in dic.items():
            if value > 0:
                # stop, go use priority que
