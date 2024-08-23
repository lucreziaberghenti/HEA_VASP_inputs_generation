import unittest
from functions import element

class TestElementFunction(unittest.TestCase):
    """
    Unit test class for the Element function.
    """

    def test_positive_cases(self):
        """
        input: an integer between the range 1:5
        what: apply 'element' to the input which maps int in the range 1:5 to a certain string 
        expected output: a string corresponding to a precise element

        """

        self.assertEqual(element(1),'Co')

        self.assertEqual(element(2),'Cr')

        self.assertEqual(element(3),'Fe')

        self.assertEqual(element(4),'Mn')

        self.assertEqual(element(5),'Ni')

    def test_negative_cases(self):

        """
        input: an integer between outside the range 1:5
        what: apply 'element'to the input which maps int in the range 1:5 to a certain string 
        expected output: an error since the input is outside the range of 'element' function
        
        """
        self.assertEqual(element(0),'error')

        self.assertEqual(element(6),'error')

        self.assertEqual(element(-10),'error')


# if the file is correctly executed then tests are executed
if __name__ == '__main__':
    unittest.main()