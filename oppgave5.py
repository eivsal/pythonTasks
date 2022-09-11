import unittest

# A palindrome is a word which reads the same backward as forward, such as anna.
def returnIfWordIsPalindrome(word): 
    #write your code here 
    
    return False
 
 
# The test based on unittest module
class TestGetAreaRectangle(unittest.TestCase):
    def runTest(self):
        isPalindrome = returnIfWordIsPalindrome("notapalindrome")
        self.assertEqual(isPalindrome, False, "Word is not a palindrome")

        isPalindrome = returnIfWordIsPalindrome("racecar")
        self.assertEqual(isPalindrome, True, "Word is a palindrome")

        isPalindrome = returnIfWordIsPalindrome("madam")
        self.assertEqual(isPalindrome, True, "Word is a palindrome")
 
# run the test
unittest.main()