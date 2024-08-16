# Software_and_Computing
## Table of content 
- Abstract
- How to
- The code 
- Results
## Abstract
High entropy alloys (HEAs) are loosely defined as solid solution alloys that contain more than five principal elements in equal or nearly equal atomic percent (at. %). 
Here we consider the Cantor Alloy, CoCrFeMnNi, with a single fcc-phase. The unit cell has dimensions (x,y,z)=(5x4x3), meaning that it is composed by 3 planes along z of 20 atoms each, for a total of 60 atoms. Since the elements Cr, Mn, Fe, Co, Ni have the same concentration, we have 12 atoms for each element in the unit cell.
The lattice parameter is 3.6 Å.

The code generates random configurations of the bulk-fcc unit cell by permutation of the positions of different elements atoms in the lattice. The new configuration is saved in the np array saved.npy only if it is not equivalent to the ones already saved (otherwise it generates another configuration until it finds a non-equivalent one). Two configurations are equivalent if their unit cells periodically repeated in 3-dim space generate the same lattice.

Each time the code is executed, it creates the input files: INCAR, POSCAR, POTCAR, KPOINTS for VASP (Vienna Ab initio Simulation Package) relaxation calculations of the new configuration.

## How to
The user has to first download the .zip folder and install the two python libraries used in the script: numpy and python ase. The installation of the packages can be done via pip (pip install package name) or, if a conda environment is used, using the command conda install package name.

Then the user can choose the input parameters by modifying the files: incar_settings.json, kpoints_settings.json and pseudo_setup.json.

Eventually, the user has just to run main.py using the command python main.py.


## The code
The code is structured into blocks:
- The file main.py which is the core script that calls the functions necessary to generate a new configuration, saves it if inequivalent and outputs the input files;
- the file functions.py that contains all functions used by main.py;
- the folder 'tests' which contains all the tests on the functions present in the file functions.py (to run a test use the command python -m unittest tets/file_name.py);
- the .json files where the user can modify the INCAR, KPOINS and pseudopotentials settings;
- the folder 'ase_pseudo' which contains the pseudopotentials stored in POTCAR files for each element necessary to write VASP input files.

## Results
The output of the code is a folder named 'conf_n', where n is the number of the nth configurationis generated, cointainig the input files: POSCAR, POTCAR, KPOINTS, INCAR.

The POTCAR file contains information on the geometry of the system and it can be visualized with VESTA, a 3D visualization program for structural models, volumetric data such as electron/nuclear densities, and crystal morphologies.
Here an example of the generated unit cell.