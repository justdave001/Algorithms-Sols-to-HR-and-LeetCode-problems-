import unittest
#import validPassword
def validPassword(password):
        return True
  
def passLength(passwordlength):
    return False

class TestTDD(unittest.TestCase):
    
    def test_empty_string(self):
        self.assertFalse(validPassword(""))
    def password_length_test(self):
        self.assertTrue(passLength(""))
        
if __name__ == '__main__':
    unittest.main()
