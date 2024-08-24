import math
import numpy as np
import os
from ase.calculators.vasp import Vasp #ase is a tool used just to create input files that (not here) I run on VASP (Vienna Ab initio Simulation Package)
from ase.build import fcc111
import json



# function that creates all the VASP input files using ase.calculators.vasp
# it takes as input: the chemical species of atoms, their positions and the number of the configuration generated
# it returns the input files
def VASP_input(species, positions, n, path):
    """
    Creates VASP input files using ase.calculators.vasp.

    Args:
    species (list): List of chemical species of atoms.
    positions (list): List of positions of atoms.
    n (int): Number of the configuration generated.
    path of the input settings (json file).

    Returns:
    None
    """
    #load settings from the input path
    with open(path, 'r') as file:
        settings = json.load(file)

    ncol, nrow, nslice= 5, 4, 3

    # lattice parameter, angstrom 
    a_fcc = settings["alat"]["a"]

    # distance between nn in xy-plane, side of equilateral triangle
    a_nn=a_fcc/math.sqrt(2) 

    # lattice vectors a1, a2, a3 #Angstrom
    a1=ncol*a_nn
    a2=nrow*a_nn*math.sqrt(3)/2
    a3=nslice*a_nn*math.sqrt(6)/3
    
    cell = [[a1,0,0], [0,a2,0], [0,0,a3]]
    
    # now define the settings for VASP
    # settings for the INCAR file. The flags must be in lowercase.This dictionary can be empty
    incar_settings = settings.get('incar_settings', {})

    # settings for the KPOINTS file
    kpoints_settings = settings.get('kpoints_settings', {})

    # setup for pseudopotentials
    pseudo_setup = settings.get('pseudo_setup', {})

    # directory where the input files will be written, the input files of the nth conf are saved in "conf_n"
    name='conf_'+str(n)
    outdir = name

    # set the path to the VASP pseudopotentials
    # NOTE: the directory must contain a folder named 'potpaw_PBE' with all the folders with the name of the elements, each containing its POTCAR
    # it simply the folder for PAW PBE provided with VASP
    os.environ["VASP_PP_PATH"] = 'ase_pseudo'

    # create the Vasp calculator
    calculator = Vasp(
                      directory=outdir,         #directory where the files will be written
                      xc='PBE', 
                      setups=pseudo_setup,
                      **incar_settings,
                      **kpoints_settings
                      )
    
    # create the Atoms object
    from ase import Atoms
    atoms = Atoms(symbols=species, 
                  positions=positions, 
                  cell=cell,
                  pbc=True)

    # write the input files INCAR, POSCAR, POTCAR, KPOINTS in the directory specified above
    calculator.write_input(atoms)

# for simplicity when new conf is generated we use numbers, then the following function translates from numbers to elements
def element(x):
    """
    Translates a number to an element symbol.

    Args:
    x (int): Number representing an element.

    Returns:
    element (str): Element symbol.
    """
    if x==1:
        return 'Co'
    if x==2:
        return 'Cr'
    if x==3:
        return 'Fe'
    if x==4:
        return 'Mn'
    if x==5:
        return 'Ni'
    else:
        return 'error' 
    
# function that given as input a (nslice,nrow,ncol) matrix of elements 1,2,3,4,5 returns the corresponding list of elements 
# the index of each element in the list is associated to a certain position (slice,row,col) in the matrix   
def Generate_species(conf):
    """
    Generates a list of chemical species from a matrix of elements.

    Args:
    conf (ndarray): Matrix of elements.

    Returns:
    species (list): List of chemical species.
    """
    
    nz, ny, nx = conf.shape

    #list of string elements
    species=[]

    #loop over conf element that are converted into str by element function           
    for x in np.nditer(conf):
        species.append(element(x))

    return species

# function that outputs a (60,3) np.array writing the lattice sites for each atom in cartesian coordinates [x, y, z] of a (111)-fcc lattice
def Coordinates(path): 
    """
    Generates a numpy array of lattice coordinates for a (111)-fcc lattice.

    Args:
    path of the input settings (json file)

    Returns:
    coord (ndarray): Array of lattice coordinates.
    """
    ncol, nrow, nslice= 5, 4, 3

    #load settings from the input path
    #load settings from the input path
    with open(path, 'r') as file:
        settings = json.load(file)

    # lattice parameter, angstrom 
    a_fcc = settings["alat"]["a"]

    # we are interested only in coordinates, so I use Ni atoms just as en example (I could have used Fe or whatever)
    atoms=fcc111(symbol='Ni', size=(ncol, nrow, nslice), a=a_fcc, vacuum=None, orthogonal=True)
    coord=atoms.get_positions()           
    return coord

# function that checks if m2 is present in m1 (m2 has dimensions < than m1) and returns 1 if matrix is present otherwise returns 0 if not
# in our case, when I call this function in the code, it will be: m1 = 4x(random conf) and m2=saved matrix
def Find(m1,m2): 
    """
    Checks if a matrix is present in another matrix.

    Args:
    m1 (ndarray): Matrix to be searched.
    m2 (ndarray): Matrix to search for.

    Returns:
    result (int): 1 if m2 is present in m1, 0 otherwise.
    """
    nz, ny, nx = m2.shape

    # loop over the increments p,m,n of then indeces nslice,nrow,ncol to sweep all the m1 matrix to find m2
    for p in range(0, nz):             
        for m in range(0,ny):
            for n in range(0,nx):

                # extract submatrix of m1 anche check if it is equal to m2
                submatrix=m1[p:(p+nz),m:(m+ny),n:(n+nx)]
                if np.array_equal(submatrix,m2):
                    return 1
    return 0      


# functions that checks if conf matrix is equivalent to one of the matrices of saved
# returns 1 if matrices are equivalent, otherwise it returns 0
def Equivalent(conf, saved):
    """
    Checks if a matrix is equivalent to any of the matrices in a list.

    Args:
    conf (ndarray): Matrix to be checked.
    saved (list): List of matrices to compare with.

    Returns:
    repeat (int): 1 if an equivalent matrix is found, 0 otherwise.
    """
    # repeat is 1 unless a non-equivalent new conf is generated
    repeat=1

    #matrix that is 8 times bigger than the input matrix
    big_conf=np.tile(conf, (2,2,2))
            
    # check if equivalent matrix is already saved in "saved.npy"

    # check first if saved is empty
    if len(saved)==0:
        repeat=0

    # if saved is not empty, loop over the elements
    else:
        # variable that becomes 1 if an equivalent matrix is found, 
        # it breaks the loop that searches a copy in the saved matrices
        copy=0

        # loop on the saved matrices to find if an equivalent matrix is already present
        for m in saved:
            # if an equivalent matrix is present
            if Find(big_conf,m):
                # copy becomes 1 and exits the loop without saving the new matrix
                copy=1 
                break

        # if at the end of the loop over the saved matrices copy is still zero because no equivalent matrix has been found, 
        # then save the new configuration 
        if(copy==0): 
            # non-equivalent new configuration is found, no need to repeat the loop
            repeat=0
            
    return repeat


# function that generates a new random configuration non-equivalent to the ones in saved
def newConf(saved, nslice, nrow, ncol, n, seed):
    """
    Generates a new random configuration that is non-equivalent to the ones in a list.

    Args:
    saved (list): List of saved matrices, dimensions: nslice, nrow, ncol of the new configuration, n 1-dim np array of the integer elements, random seed

    Returns:
    conf (ndarray): New random configuration.
    """
    
    # variable that iterates the loop if an equivalent configuration is generated (and consequently discarded)
    # set to zero when successfully generate a new conf inequivalent to the ones saved
    repeat=1
    
    while repeat:
        #fix the random seed
        np.random.seed(seed)
        # random permutation of linear array
        n=np.random.permutation(n)
        # then reshap the permutated array with the desired dimensions
        conf=np.reshape(n, (nslice,nrow,ncol))
        # check if conf is equivalente to the matrices of saved
        repeat=Equivalent(conf, saved)
        
    return conf