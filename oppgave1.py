import unittest
 
def returnNumberOfLowerCaseLetters(word):
     #write your code here
    
    return 0





class TestGetNumberOfLowerCaseLetters(unittest.TestCase):
    def runTest(self):
        word = "qsadsSASC:-sqwd1219::--saklvøasfoeqfvsasdfl__:sadas3qIIøøæqååsdaASDSA::_[]≈≈ßdasjkdka"
        number = returnNumberOfLowerCaseLetters(word)
        self.assertEqual(number, 52, "incorrect number")

        word = "-..sdasfJSIAP??139;DSmdaskk3a;sad;;:s__sasidjas190139NND:_[]≈≈ßdasjkdka"
        number = returnNumberOfLowerCaseLetters(word)
        self.assertEqual(number, 32, "incorrect number")

        word = "øasfoeqfvsada;SDADcc,;;sas__13:_[]≈≈ßdasjkdka"
        number = returnNumberOfLowerCaseLetters(word)
        self.assertEqual(number, 26, "incorrect number")

        word = "qsadsa-_1313ksa:;;;;sa.--__sasdcSDSA::_[]≈≈ßdasjkdka"
        number = returnNumberOfLowerCaseLetters(word)
        self.assertEqual(number, 24, "incorrect number")

        word = "qsadsdasdsadYYYYdsa:::___sacnnsasdaASDSA::_[]≈≈ßdasjkdka"
        number = returnNumberOfLowerCaseLetters(word)
        self.assertEqual(number, 33, "incorrect number")
unittest.main()