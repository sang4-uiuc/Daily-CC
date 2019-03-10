# Write a function, add_subtract, which alternately adds and subtracts curried arguments. Here are some sample operations:

# add_subtract(7) -> 7

# add_subtract(1)(2)(3) -> 1 + 2 - 3 -> 0

# add_subtract(-5)(10)(3)(9) -> -5 + 10 - 3 + 9 -> 11

import unittest

def add_subtract(*args):
    if len(args) < 1:
        return 0
    total = args[0]
    for i in range(1, len(args)):
        if i % 2 != 0:
            total += args[i]
        else:
            total -= args[i]
    return total

class AddSubtractTest(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(add_subtract(7), 7)
        self.assertEqual(add_subtract(1,2,3), 0)
        self.assertEqual(add_subtract(4,4,4), 4)
        self.assertEqual(add_subtract(-5, 10, 3, 9), 11)
        self.assertEqual(add_subtract(12, 6, 7, 3, 13), 1)

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(AddSubtractTest))
    return test_suite

suite = suite()
unittest.TextTestRunner().run(suite)
