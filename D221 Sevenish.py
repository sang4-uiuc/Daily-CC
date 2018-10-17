# This problem was asked by Zillow.
# Let's define a "sevenish" number to be one which is either a power of 7, 
# or the sum of unique powers of 7. The first few sevenish numbers are 1, 7, 8, 49, and so on. 
# Create an algorithm to find the nth sevenish number.
import timeit
import unittest

def sevenish(n):
    l = []
    power = 0
    if n <= 0:
        return 0
    while n > 0:
        l.append(7 ** power)
        power += 1
        n -= 1
        if n == 0:
            break
        original_length = len(l)
        for i in range(original_length - 1):
            l.append(l[original_length-1]+l[i])
            n-=1
            if n == 0:
                break
    return l.pop()

# print(timeit.timeit("sevenish(6)", setup="from __main__ import sevenish", number=10000))
# [1, 7, 8, 49, 50, 56, 57, 343, 344, 350]

class SevenishTest(unittest.TestCase):
    def test_reg(self):
        self.assertEqual(sevenish(1), 1)
        self.assertEqual(sevenish(4), 49)
        self.assertEqual(sevenish(5), 50)
        self.assertEqual(sevenish(10), 350)
    def test_edge(self):
        self.assertEqual(sevenish(0), 0)
        self.assertEqual(sevenish(-1), 0)

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(SevenishTest))
    return test_suite

suite = suite()
unittest.TextTestRunner().run(suite)