import unittest

def add(x,y):
    return x+y

# Function to test if string is a palendrome
def isPalendrome(inputS):
    pos = 1
    for i in inputS:
        if i == inputS[len(inputS)-pos]:
            pos+=1
            continue
        else:
            return False
    return True

# Function to test if string only contains letters
def isAlpha(inputS):
    return inputS.isalpha()

def Fibonacci(n):
    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        print("Incorrect input")

    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0

    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1

    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

class TestClass(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,3), 5)
        pass
    
    def test_palendrome(self):
        self.assertFalse(isPalendrome("Test"))

        self.assertTrue(isPalendrome("ABBA"))
        self.assertTrue(isPalendrome("ABCBA"))
        self.assertTrue(isPalendrome("ABCBA"))
        pass

    def test_alpha(self):
        self.assertFalse(isAlpha("0123"))
        self.assertFalse(isAlpha("0123abc"))
        self.assertFalse(isAlpha("0123ABC"))
        self.assertFalse(isAlpha("abc abc abc"))

        self.assertTrue(isAlpha("abcABC"))
        pass

    def test_fibonachi(self):
        self.assertEqual(Fibonacci(3), 2)
        self.assertEqual(Fibonacci(9), 34)
        pass
        

if __name__ == '__main__':
    unittest.main()