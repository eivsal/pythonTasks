import unittest

# Decide if number is prime or not
def returnIfNumberIsPrime(number):
    #write your code here 
    
    return False
 



# The test based on unittest module
class TestGetAreaRectangle(unittest.TestCase):
    def runTest(self):
        number = returnIfNumberIsPrime(13)
        self.assertEqual(number, True, "Is a prime")

        number = returnIfNumberIsPrime(22)
        self.assertEqual(number, False, "Is not a prime")

        number = returnIfNumberIsPrime(31)
        self.assertEqual(number, True, "Is a prime")
 
# run the test
unittest.main()