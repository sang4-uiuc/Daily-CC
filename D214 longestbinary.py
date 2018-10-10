# Given an integer n, return the length of the longest consecutive run of 1s in its binary representation.

# For example, given 156, you should return 3.

import unittest

def longestBinary(n):
    binary_number = []
    longest_run = 0
    count = 0
    while n > 0:
        binary_number.append(n%2)
        n = n // 2
    if len(binary_number) < 1:
        return 0

    for i in range(len(binary_number)):
        if binary_number[i] == 1:
            count += 1
            longest_run = max(longest_run, count)
        else:
            count = 0
    return longest_run
            
class BinaryTest(unittest.TestCase):
    def test_method(self):
        self.assertEqual(longestBinary(156), 3)
        self.assertEqual(longestBinary(0), 0)
        self.assertEqual(longestBinary(3), 2)
        self.assertEqual(longestBinary(2), 1)
        self.assertEqual(longestBinary(100000), 2)
        self.assertEqual(longestBinary(63), 6)


if __name__ == "__main__":
    unittest.main()