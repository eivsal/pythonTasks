import unittest

# return the fibonacci number on the given index
def returnTheNthFibonacciNumber(index): 
    #write your code here 
    return 0
 
 
# The test based on unittest module
class TestGetAreaRectangle(unittest.TestCase):
    def runTest(self):
        fibNumber = returnTheNthFibonacciNumber(3)
        self.assertEqual(fibNumber, 1, "Wrong number")

        fibNumber = returnTheNthFibonacciNumber(5)
        self.assertEqual(fibNumber, 3, "Wrong number")

        fibNumber = returnTheNthFibonacciNumber(7)
        self.assertEqual(fibNumber, 8, "Wrong number")
 
# run the test
unittest.main()