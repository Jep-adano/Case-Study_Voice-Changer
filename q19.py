import unittest

def equal():
    name = 'PEDRO'
    return name

class mytest (unittest.TestCase):
    def test(self):
        self.assertEqual(equal(),'PEDRO')
    
if __name__ == "__main__":
    unittest.main()