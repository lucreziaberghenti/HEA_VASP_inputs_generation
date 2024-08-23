import unittest
import numpy as np
from ase.build import fcc111
from functions import Coordinates
import json

#load the dictionary used for testing: settings_tests.json
#in this dictionary alat=3.6
file_path = './tests/settings_tests.json' 

class TestCoordinates(unittest.TestCase):
    """
    Unit test class for the Coordinates function.
    """

    def test_coordinates_shape(self):
        """
        what: call Coordinate function
        expected output: a 3-dim array of 60 atoms having dimensions (60,3)
        
        """
        coords = Coordinates(file_path)
        self.assertEqual(coords.shape, (60, 3))

    
    def test_atom_positions(self):
        """
        given: the value for the lattice parameter of the dictionary 'settings_tests.json': alat=3.6
        what: call Coordinate function
        expected output: the positions match with the ones of a (111)-fcc lattice calculated using alat of settings_test.json

        """

        expected_positions = np.array([
            [ 1.27279221,  0.73484692,  0.        ],
            [ 3.81837662,  0.73484692,  0.        ],
            [ 6.36396103,  0.73484692,  0.        ],
            [ 8.90954544,  0.73484692,  0.        ],
            [11.45512986,  0.73484692,  0.        ],
            [ 0.        ,  2.93938769,  0.        ]
            # ... more positions can be added as needed ...
        ])
      
        coords = Coordinates(file_path)
      
        # Verify that the first n positions are equal to the expected ones (with a certain tolerance)
        np.testing.assert_almost_equal(coords[:len(expected_positions)], expected_positions, decimal=6)

    def distance_between_nearest_neighbors(self):
        """
        given: the value for the lattice parameter of the dictionary 'settings_tests.json': alat=3.6
        what: call Coordinate function and calculate distance between nearest neighbours
        expected output: the distance between nearest neighbors matches with the one calculated using alat of settings_test.json

        """
        
        coords = Coordinates(file_path)

        # Test the distance between nearest neighbors
        d = np.linalg.norm(coords[0] - coords[1]) 
        expected_d = 3.6 / np.sqrt(2)

        self.assertAlmostEqual(d, expected_d, places=6)

    def angle_between_vectors(self):
        """
        given: the value for the lattice parameter of the dictionary 'settings_tests.json': alat=3.6
        what: call Coordinate function and calculate angle between vectors
        expected output: the angle between base vectors matches with the one calculated using alat of settings_test.json

        """

        coords = Coordinates(file_path)

        # Test the angle between base vectors
        v1 = coords[1] - coords[0]
        v2 = coords[2] - coords[0]
        angle = np.arccos(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))
        print(angle)
        self.assertAlmostEqual(angle, 0, places=6)

if __name__ == '__main__':
    """
    Executes the test cases when the script is run directly.
    """
    unittest.main()