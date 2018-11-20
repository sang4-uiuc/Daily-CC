import unittest
# This problem was asked by Facebook.

# Given an array of numbers of length N, find both the minimum and maximum using less than 2 * (N - 2) comparisons.



# If n is odd then initialize min and max as first element.
# If n is even then initialize min and max as minimum and maximum of the first two elements respectively.
# For rest of the elements, pick them in pairs and compare their
# maximum and minimum with max and min respectively.
def findMinMax(l):
#     Time Complexity: O(n)

# Total number of comparisons: Different for even and odd n, see below:

#        If n is odd:    3*(n-1)/2  
#        If n is even:   1 Initial comparison for initializing min and max, 
#                            and 3(n-2)/2 comparisons for rest of the elements  
#                       =  1 + 3*(n-2)/2 = 3n/2 -2

    if len(l) % 2 == 0:
        if l[0] > l[1]:
            l_max = l[0]
            l_min = l[1]
        else:
            l_max = l[1]
            l_min = l[0]
        i = 2
    else:
        l_min, l_max = l[0], l[0]
        i = 1
    while i < len(l) - 1:
        if l[i] > l[i + 1]:
            if l[i] > l_max:
                l_max = l[i]
            if l[i + 1] < l_min:
                l_min = l[i + 1]
        else:
            if l[i + 1] > l_max:
                l_max = l[i + 1]
            if l[i] < l_min:
                l_min = l[i]
        i += 1
    # print("hi")
    # print(l_min, l_max)
    return (l_min, l_max)

class FindMinMaxTest(unittest.TestCase):
    def test_reg(self):
        self.assertEqual(findMinMax([1,2,3,4,5,6,7,8]), (1, 8))
        self.assertEqual(findMinMax([27, 29, 26, 40, 1, 4, 5, 47]), (1, 47))
        self.assertEqual(findMinMax([29, 28, 27, 26, 25, 4, 89, 1]), (1, 89))
        self.assertEqual(findMinMax([37, 47, 28, 64, 101, 249, 10, 24, 55, 22]), (10, 249))

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(FindMinMaxTest))
    return test_suite

suite = suite()
unittest.TextTestRunner().run(suite)
# print(findMinMax([1,2,3,4,5,6,7,8]))