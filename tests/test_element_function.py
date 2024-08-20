import unittest
from functions import element

class Test_Element_Function(unittest.TestCase):
    """
    Unit test class for the Element function.
    """

    def test_element(self):
        """
        Test if the Element function returns:
        - the correct element corresponding to input in the range 1:5
        - 'error' if the input is outside the range 1:5
        """

        print("running test...")

        # test of correct cases
        self.assertEqual(element(1),'Co')

        self.assertEqual(element(2),'Cr')

        self.assertEqual(element(3),'Fe')

        self.assertEqual(element(4),'Mn')

        self.assertEqual(element(5),'Ni')

        # test of input of element function outside of the range 1:5
        self.assertEqual(element(0),'error')

        self.assertEqual(element(6),'error')

        self.assertEqual(element(-10),'error')


# if the file is correctly executed then tests are executed
if __name__ == '__main__':
    unittest.main()