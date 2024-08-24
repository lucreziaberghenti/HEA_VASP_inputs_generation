import unittest
import os
from ase import Atoms
from functions import VASP_input
from ase.calculators.vasp import Vasp
import numpy as np
import json

#load the dictionary used for testing: settings_tests.json
file_path = './tests/settings_tests.json'
with open(file_path, 'r') as file:
    settings = json.load(file)

class TestVASPInput(unittest.TestCase):
    """
    Unit test class for the VASP_input function.

    """
       
    def test_incar_settings(self):
        """
        given: the parameters of settings_tests.json (dictionary used for testing only)
        when: loading the incar settings
        expected output: the loaded incar settings match the value of expected_settings variable
        """

        incar_settings=settings["incar_settings"]
    
        
        # Expected dictionary for INCAR settings
        expected_settings = {
            "istart": 0,
            "icharg": 2,
            "encut": 400,
            "algo": "Normal",
            "nelm": 60,
            "ediff": 1E-06,
            "ismear": 1,
            "sigma": 0.1,
            "ispin": 2,
            "ediffg": -5E-02,
            "nsw": 20,
            "ibrion": 1
        }
        
        # Compare the incar settings loaded from the dictionary with the ones expected
        self.assertEqual(incar_settings, expected_settings)

    def test_kpoints_settings(self):
        """
        given: the parameters of settings_tests.json (dictionary used for testing only)
        when: loading the kpoints settings
        expected output: the loaded kpoints settings match the value of expected_settings variable
        """
        
        kpoints_settings=settings["kpoints_settings"]
    
        # check that Vasp was instantiated with the correct arguments
        # Expected dictionary for INCAR settings
        expected_settings = {
            "kpts": [2, 3, 4],
            "gamma": True
        }

        # Compare the incar settings loaded from the dictionary with the ones expected
        self.assertEqual(kpoints_settings, expected_settings)

    def test_pseudo_setup(self):
        """
        given: the parameters of settings_tests.json (dictionary used for testing only)
        when: loading the pseudopotentials settings
        expected output: the loaded pseudo settings match the value of expected_settings variable
        """

        pseudo_settings=settings["pseudo_setup"]

        expected_settings={
            "base": "recommended"
        }

        # Compare the incar settings loaded from the dictionary with the ones expected
        self.assertEqual(pseudo_settings, expected_settings)

    def test_directory_creation(self):
        """
        given: settings_tests.json (dictionary used for testing only), the integer n of the nth configuration, the lists of species and positions
        when: calling the VASP_input function 
        expected output: a new directory 'conf_1' is created
        """
        species = ['Co', 'Cr', 'Fe']
        positions = [(0, 0, 0), (0.5, 0.5, 0.5), (1, 1, 1)]
        n = 1

        VASP_input(species, positions, n, file_path)

        #check if directory conf_1 is created
        path_dir='./conf_1'
        self.assertTrue(os.path.exists(path_dir), "No directory of file inputs created")

# If the file is correctly executed, then tests are executed
if __name__ == '__main__':
    unittest.main()