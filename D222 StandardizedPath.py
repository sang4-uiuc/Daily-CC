# This problem was asked by Quora.

# Given an absolute pathname that may have . or .. as part of it, return the shortest standardized path.

# For example, given "/usr/bin/../bin/./scripts/../", return "/usr/bin/".
import unittest

def standardizePathName(s):
    l = s.split("/")
    stack = []
    output = ""
    for i in l:
        if i == "." or i == "":
            continue
        if i == "..":
            try:
                stack.pop()
            except:
                continue
        else:
            stack.append(i)
    if len(stack) == 0:
        return "/"
    for i in stack:
        output += "/" + i
    return output

class PathnameTest(unittest.TestCase):
    def test_reg(self):
        self.assertEqual(standardizePathName("/usr/bin/../bin/./scripts/../"), "/usr/bin")
        self.assertEqual(standardizePathName("/home/"), "/home")
        self.assertEqual(standardizePathName("/a/./b/../../c/"), "/c") 
        self.assertEqual(standardizePathName("/a/.."), "/")
        self.assertEqual(standardizePathName("/../../../../../a"), "/a")
        self.assertEqual(standardizePathName("/a/./b/./c/./d/"), "/a/b/c/d")
        self.assertEqual(standardizePathName("/a//b//c//////d"), "/a/b/c/d")

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(PathnameTest))
    return test_suite

unittest.TextTestRunner().run(suite())



