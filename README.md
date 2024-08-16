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

The code creates the input files: INCAR, POSCAR, POTCAR, KPOINTS of bulk structure for VASP (Vienna Ab initio Simulation Package) relaxation calculations.

## How to
The user has to first download the .zip folder and install the two python libraries used in the script: numpy and python ase. The installation of the packages can be done via pip (pip install <package name>) or, if a conda environment is used, using the command conda install <package name>.

Then the user can choose the input parameters by modifying the files: <incar_settings.json>, <kpoints_settings.json> and <pseudo_setup.json>.



## The code
## Results