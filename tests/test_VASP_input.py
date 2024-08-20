import unittest
from unittest.mock import patch, MagicMock
from ase import Atoms
from functions import VASP_input
import numpy as np

class TestVASPInput(unittest.TestCase):
    """
    Unit test class for the VASP_input function. It uses unittest and mocking
    to verify the behavior of the VASP_input function in different scenarios.
    """

    @patch('functions.load_incar_settings')
    @patch('functions.load_kpoints_settings')
    @patch('functions.load_pseudo_setup')
    @patch('functions.os')
    @patch('functions.Vasp')

    
    def test_vasp_input(self, mock_vasp, mock_os, mock_load_pseudo_setup,
                        mock_load_kpoints_settings, mock_load_incar_settings):
        """
        Test case for the VASP_input function. It checks the following:
        1. That the correct INCAR, KPOINTS, and POTCAR settings are loaded.
        2. That the environment variable 'VASP_PP_PATH' is set correctly.
        3. That the Vasp calculator is instantiated with the correct arguments.
        4. That the write_input method is called with an Atoms object containing
           the correct atomic species, positions, and cell dimensions.
        """

        # setup mock return values
        mock_load_incar_settings.return_value = {'encut': 400, 'ismear': 0, 'sigma': 0.1}
        mock_load_kpoints_settings.return_value = {'kpts': [4, 4, 1]}
        mock_load_pseudo_setup.return_value = {'Co': '_Co', 'Cr': '_Cr', 'Fe': '_Fe'}
       
        # mock the environment variable
        mock_os.environ = {}
       
        # mock the Vasp calculator
        mock_calc = MagicMock()
        mock_vasp.return_value = mock_calc
       
        # define input parameters
        species = ['Co', 'Cr', 'Fe']
        positions = [(0, 0, 0), (0.5, 0.5, 0.5), (1, 1, 1)]
        n = 1
       
        # call the function
        VASP_input(species, positions, n)
       
        # check that the environment variable was set
        self.assertEqual(mock_os.environ["VASP_PP_PATH"], 'ase_pseudo')
       
        # check that Vasp was instantiated with the correct arguments
        mock_vasp.assert_called_once_with(
            directory='conf_1',
            xc='PBE',
            setups={'Co': '_Co', 'Cr': '_Cr', 'Fe': '_Fe'},
            encut=400,
            ismear=0,
            sigma=0.1,
            kpts=[4, 4, 1]
        )
       
        # check that write_input was called with the correct Atoms object
        mock_calc.write_input.assert_called_once()
        atoms_arg = mock_calc.write_input.call_args[0][0]
       
        # verify the Atoms object
        self.assertEqual(atoms_arg.get_chemical_symbols(), species)
        self.assertTrue((atoms_arg.get_positions() == positions).all())
        self.assertTrue(np.all(np.isclose(atoms_arg.get_cell(), [[12.727922061357855, 0.0, 0.0],
                                                                 [0.0, 8.81816307401944, 0.0],
                                                                 [0.0, 0.0, 6.235382907247957]])))
        self.assertTrue(np.all(atoms_arg.get_pbc()))

# If the file is correctly executed, then tests are executed
if __name__ == '__main__':
    unittest.main()