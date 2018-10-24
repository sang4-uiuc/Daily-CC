# This problem was asked by Twitter.

# Given a list of numbers, create an algorithm that arranges them in order to form the largest possible integer.
# For example, given [10, 7, 76, 415], you should return 77641510.

import unittest


def myCompare(a, b):
    ab = str(a) + str(b)
    ba = str(b) + str(a)
    # honestly a bit confused about this line here
    # what's the point of doing this minus
    return ((int(ba) > int(ab)) - (int(ba) < int(ab)))


def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'
    class K:
        def __init__(self, obj, *args):
            self.obj = obj

        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0

        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0

        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0

        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0

        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0

        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K


def largestNumber2(arr):
    # python provided cmptokey since it's from python2
    sorted_array = sorted(arr, key=cmp_to_key(myCompare))
    
    number = "".join([str(i) for i in sorted_array])
    return int(number)


def largestNumber(array):
    extval, ans = [], ""
    # basically every element should multiply and extend out to the length of the max value + 1
    l = len(str(max(array))) + 1
    for i in array:
        temp = str(i) * l
        extval.append((temp[:l], i))

    # sort extval in descending order
    extval.sort(reverse=True)
    for i in extval:
        ans += str(i[1])

    return int(ans)


class LargestNumberTest(unittest.TestCase):
    def test_largestNumber(self):
        self.assertEqual(largestNumber([1, 2, 3, 4, 5]), 54321)
        self.assertEqual(largestNumber([10, 7, 76, 415]), 77641510)
        self.assertEqual(largestNumber(
            [1, 34, 3, 98, 9, 76, 45, 4, 12, 121]), 99876454343121211)
    def test_largestNumber2(self):
        self.assertEqual(largestNumber2([1, 2, 3, 4, 5]), 54321)
        self.assertEqual(largestNumber2([10, 7, 76, 415]), 77641510)
        self.assertEqual(largestNumber2(
            [1, 34, 3, 98, 9, 76, 45, 4, 12, 121]), 99876454343121211)

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(LargestNumberTest))
    return test_suite

suite = suite()
unittest.TextTestRunner().run(suite)