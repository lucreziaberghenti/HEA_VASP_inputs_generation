# Software and Computing

## Table of Contents
- [Abstract](#abstract)
- [How to Use](#how-to-use)
- [The Code Structure](#the-code-structure)
- [Results](#results)

## Abstract
High entropy alloys (HEAs) are loosely defined as solid solution alloys that contain more than five principal elements in equal or nearly equal atomic percent (at.%). Here we consider the Cantor Alloy, CoCrFeMnNi, with a single FCC-phase. The unit cell has dimensions of (x, y, z) = (5x4x3), meaning that it is composed of 3 planes along the z-axis, each containing 20 atoms, for a total of 60 atoms. Since the elements Cr, Mn, Fe, Co, and Ni have the same concentration, there are 12 atoms for each element in the unit cell. The lattice parameter is 3.6 Å.

This code generates random configurations of the bulk-FCC unit cell by permuting the positions of different element atoms in the lattice. A new configuration is saved in the numpy array `saved.npy` only if it is not equivalent to the ones already saved. If the configuration is equivalent to any existing configuration, the code generates another configuration until a non-equivalent one is found. Two configurations are considered equivalent if their unit cells, when periodically repeated in 3D space, generate the same lattice.

Each time the code is executed, it creates the input files: `INCAR`, `POSCAR`, `POTCAR`, and `KPOINTS` for VASP (Vienna Ab initio Simulation Package) relaxation calculations of the new configuration.

## How to Use
1. **Download and Installation:**
   - First, download the `.zip` folder containing the code.
   - Install the required Python libraries: `numpy` and `python-ase`. You can install these packages using pip:
     ```
     pip install numpy ase
     ```
     Alternatively, if you are using a conda environment, use:
     ```
     conda install numpy ase
     ```

2. **Configuration:**
   - Adjust the input parameters by modifying the following files in the `settings` folder:
     - `incar_settings.json`
     - `kpoints_settings.json`
     - `pseudo_setup.json`

3. **Execution:**
   - Run the main script by executing the following command:
     ```
     python main.py
     ```

## The Code Structure
The code is organized into the following components:

- **`main.py`:** The core script that calls the necessary functions to generate a new configuration, saves it if it is inequivalent, and outputs the input files.
- **`functions.py`:** Contains all the functions that are used by `main.py`.
- **`tests/`:** A folder containing tests for the functions present in `functions.py`. To run a test, use the command:
     ```
     python -m unittest tests/file_name.py
     ```

- **`settings/`:** A folder containing the `.json` files that the user can modify to adjust the INCAR, KPOINTS, and pseudopotentials settings.
- **`ase_pseudo/`:** A folder containing the pseudopotentials stored in POTCAR files for each element, necessary for writing VASP input files.

## Results
The output of the code is a folder named `conf_n`, where `n` is the nth configuration generated. This folder contains the following input files:

- `POSCAR`
- `POTCAR`
- `KPOINTS`
- `INCAR`

The `POTCAR` file contains information on the geometry of the system, and it can be visualized using VESTA, a 3D visualization program for structural models, volumetric data such as electron/nuclear densities, and crystal morphologies.

Here is an example of the generated unit cell.

![Unit Cell Image] (./unit_cell.png)