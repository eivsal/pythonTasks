import unittest
 
def returnWordReversed(word):
    #write your code here
    return "returnastringhere"




    
 
# The test based on unittest module
class TestGetWordReversed(unittest.TestCase):
    def runTest(self):
        word = "desreverebdluohssiht"
        reversedWord = returnWordReversed(word)
        self.assertEqual(reversedWord, "thisshouldbereversed", "incorrect word")

        word = "desreverebotdrowdnoces"
        reversedWord = returnWordReversed(word)
        self.assertEqual(reversedWord, "secondwordtobereversed", "incorrect word")

        word = "sdrowllaekamuoynac"
        reversedWord = returnWordReversed(word)
        self.assertEqual(reversedWord, "canyoumakeallwords", "incorrect word")

        word = "noisreverlanif"
        reversedWord = returnWordReversed(word)
        self.assertEqual(reversedWord, "finalreversion", "incorrect word")
 
# run the test
unittest.main()