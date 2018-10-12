# The values of Roman numerals are as follows:
import unittest


# For the input XIV, for instance, you should return 14.

def convert(s):
    ref = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
    }
    total = 0
    if len(s) < 1:
        return 0
    for i in range(len(s) - 1):
        if ref[s[i]] >= ref[s[i + 1]]:
            total += ref[s[i]]
        else:
            total -= ref[s[i]]
    return total + ref[s[-1]]

class Roman2IntTest(unittest.TestCase):
    def test_edge(self):
        self.assertEqual(convert(""), 0)

    def test_reg(self):
        self.assertEqual(convert("I"), 1)
        self.assertEqual(convert("M"), 1000)
        self.assertEqual(convert("IM"), 999)
        self.assertEqual(convert("III"), 3)
        self.assertEqual(convert("XIV"), 14)
        self.assertEqual(convert("XVI"), 16)
        self.assertEqual(convert("MDC"), 1600)

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(Roman2IntTest))
    return test_suite

unittest.TextTestRunner().run(suite())