# This problem was asked by Amazon.

# Given a sorted array, find the smallest positive integer that is not the sum of a subset of the array.

# For example, for the input [1, 2, 3, 10], you should return 7.

# Do this in O(N) time.
import unittest

def smallestSubset(arr):
    res = 1
    for i in arr:
        if res >= i:
            res += i
        else:
            break
    return res

class smallestSubsetTest(unittest.TestCase):
    def test_reg(self):
        self.assertEqual(smallestSubset([1,2,3,10]), 7)
        self.assertEqual(smallestSubset([1,2,3,4]), 11)
        self.assertEqual(smallestSubset([1,3,10]), 2)
        self.assertEqual(smallestSubset([1,2,5,6,7]), 4)

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(smallestSubsetTest))
    return test_suite

unittest.TextTestRunner().run(suite())
