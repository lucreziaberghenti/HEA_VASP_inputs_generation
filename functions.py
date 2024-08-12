import math
import numpy as np
import os
from ase.calculators.vasp import Vasp #ase is a tool used just to create input files that (not here) I run on VASP (Vienna Ab initio Simulation Package)
from ase.build import fcc111

#global variables
a_fcc=3.6 #lattice parameter, angstrom 
a_nn=a_fcc/math.sqrt(2) #distance between nn in xy-plane, side of equilateral triangle

ncol, nrow, nslice= 5, 4, 3
#np arrays that contains the number of atoms for each element labeled by 1,2,3,4,5: n=[n1,n2,n3,n4,n5]
n=np.array([12, 12, 12, 12, 12],dtype=int)
n_tot=np.sum(n)


#function that creates all the VASP input files using ase.calculators.vasp
#it takes as input: the chemical species of atoms, their positions and the number of the configuration generated
#it returns the input files
def VASP_input(species, positions, n):
    #lattice vectors a1, a2, a3 #Angstrom
    a1=ncol*a_nn
    a2=nrow*a_nn*math.sqrt(3)/2
    a3=nslice*a_nn*math.sqrt(6)/3
    
    cell = [[a1,0,0], [0,a2,0], [0,0,a3]]
    
    #Now define the settings for VASP
    #settings for the INCAR file. The flags must be in lowercase.This dictionary can be empty
    incar_settings = {
        'istart': 0,
        'icharg':2,
        'encut': 400,
        'algo': 'Normal',
        'nelm': 60,
        'ediff': 1E-06,
        'ismear': 1,
        'sigma': 0.1,
        'ispin': 2,
        'ediffg': -5E-02,
        'nsw': 20,
        'ibrion': 1,
    }

    #settings for the KPOINTS file
    kpoints_settings = {
        'kpts': (2, 3, 4), # grid
        'gamma': True     
    }
    
    #setup for pseudopotentials
    pseudo_setup = {'base': 'recommended'}

    #directory where the input files will be written, the input files of the nth conf are saved in "conf_n"
    name='conf_'+str(n)
    outdir = name

    #set the path to the VASP pseudopotentials
    #NOTE: the directory must contain a folder named 'potpaw_PBE' with all the folders with the name of the elements, each containing its POTCAR
    #it simply the folder for PAW PBE provided with VASP
    os.environ["VASP_PP_PATH"] = 'ase_pseudo'

    # Create the Vasp calculator
    calculator = Vasp(
                      directory=outdir,         #directory where the files will be written
                      xc='PBE', 
                      setups=pseudo_setup,
                      **incar_settings,
                      **kpoints_settings
                      )
    
    #Create the Atoms object
    from ase import Atoms
    atoms = Atoms(symbols=species, 
                  positions=positions, 
                  cell=cell,
                  pbc=True)

    # Write the input files INCAR, POSCAR, POTCAR, KPOINTS in the directory specified above
    calculator.write_input(atoms)

#for simplicity when new conf is generated we use numbers, then the following function translates from numbers to elements
def element(x):
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

#function that outputs a (60,3) np.array writing the lattice sites for each atom in cartesian coordinates [x, y, z] of a (111)-fcc lattice
def Coordinates(): 
    #we are interested only in coordinates so I use Ni atoms just as en example (I could have used Fe or whatever)
    atoms=fcc111(symbol='Ni', size=(5,4,3), a=a_fcc, vacuum=None, orthogonal=True)
    coord=atoms.get_positions()           
    return coord

#function that checks if m2 is present in m1 (m2 has dimensions < than m1) and returns 1 if matrix is present otherwise returns 0 if not
#in our case m1 = 4x(random conf) and m2=saved matrix
def Find(m1,m2): 
    #np array that will be used to sweep the bigger matrix
    temp=np.zeros((nslice, nrow,ncol),dtype=int)
    
    #loop over the increments p,m,n of then indeces nslice,nrow,ncol to sweep all the m1 matrix to find m2
    for p in range(0, nslice):             
        for m in range(0,nrow):
            for n in range(0,ncol):
                #for each pair of increments m,n
                #create the sub-matrix temp of dimension of m2 but equal to the row+m and column+n of m1
                for sl in range(0, nslice):
                    for row in range(0,nrow):
                        for col in range(0,ncol):
                            temp[sl,row,col]=m1[sl+p,row+m,col+n]

                #check if temp is equal to m2
                if np.array_equal(temp,m2):
                    return 1
    return 0      

#function that takes as input a conf of dim (nslice,nrow,ncol) and returns a matrix 8-times bigger
def Big_conf(conf):
    #dimensions of 8x conf matrix 
    Nslice=2*nslice
    Nrow=2*nrow
    Ncol=2*ncol

    big_conf=np.zeros((nslice,Nrow,Ncol),dtype=int)

    for sl in range(0,nslice):
        for row in range(0,nrow):
            big_conf[sl,row]=np.concatenate((conf[sl,row],conf[sl,row]))

        for col in range(0,Ncol):
            big_conf[sl,:,col]=np.concatenate((conf[sl,:,(col%ncol)],conf[sl,:,(col%ncol)]))   #%ncol modulo ncol because conf has half columns of new_conf

    big_conf=np.concatenate((big_conf, big_conf))
    return big_conf

#functions that checks if the input matrix is equivalent to the matrix saved in "saved.npy"
def Equivalent(conf):

#function that generates a new random configuration non equivalent to the ones saved
def newConf(saved):