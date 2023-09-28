import unittest 

def grade(x):

    return x >= 50

class MyTest(unittest.TestCase):

        def test(self):
            self.assertTrue (grade(90))
            print("PASSED")
            

if __name__== '__main__':

    unittest.main()