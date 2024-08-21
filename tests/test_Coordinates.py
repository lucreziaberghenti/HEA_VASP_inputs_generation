import unittest
import numpy as np
from unittest.mock import patch
from ase.build import fcc111
from functions import Coordinates

class TestCoordinates(unittest.TestCase):
    """
    Unit test class for the Coordinates function.
    """

    @patch('functions.load_alat')
    def test_coordinates_shape(self, mock_load_alat):
        """
        Test if the Coordinates function returns an array with shape (60, 3).
        """
        mock_load_alat.return_value = 3.6
        coords = Coordinates()
        self.assertEqual(coords.shape, (60, 3))

    @patch('functions.load_alat')
    def test_atom_positions(self, mock_load_alat):
        """
        Test if the first atomic positions returned by Coordinates
        match the expected positions for Ni fcc(111).
        """
        mock_load_alat.return_value = 3.6

        expected_positions = np.array([
            [ 1.27279221,  0.73484692,  0.        ],
            [ 3.81837662,  0.73484692,  0.        ],
            [ 6.36396103,  0.73484692,  0.        ],
            [ 8.90954544,  0.73484692,  0.        ],
            [11.45512986,  0.73484692,  0.        ],
            [ 0.        ,  2.93938769,  0.        ]
            # ... more positions can be added as needed ...
        ])
      
        coords = Coordinates()
      
        # Verify that the first n positions are equal to the expected ones (with a certain tolerance)
        np.testing.assert_almost_equal(coords[:len(expected_positions)], expected_positions, decimal=6)

    @patch('functions.load_alat')
    def test_fcc_properties(self, mock_load_alat):
        """
        Test some properties of the fcc lattice, such as the nearest neighbor distance
        and the angle between base vectors.
        """
        mock_load_alat.return_value = 3.6


        coords = Coordinates()

        # Test the distance between nearest neighbors
        d = np.linalg.norm(coords[0] - coords[1]) 
        expected_d = 3.6 / np.sqrt(2)
        self.assertAlmostEqual(d, expected_d, places=6)

        # Test the angle between base vectors
        v1 = coords[1] - coords[0]
        v2 = coords[2] - coords[0]
        angle = np.arccos(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))
        self.assertAlmostEqual(angle, 0, places=6)

if __name__ == '__main__':
    """
    Executes the test cases when the script is run directly.
    """
    unittest.main()