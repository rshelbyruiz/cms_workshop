"""
Functions and script for geometry analysis.
"""

import numpy
import os
import sys

def calculate_distance(atom1, atom2):
    """
    Calculate the distance between the two atoms.

    Parameters
    ----------
    atom1: list
        A list of coordinates [x, y, z]
    aotm2: list
        A list of coordinates [x, y, z]

    Returns
    ----------
    bond_length: float
        The distance between atoms.

    Examples
    ----------
    >>> calculate_distance([0, 0, 0], [0, 0, 1])
    1.0
    """
    x_distance = atom1[0]-atom2[0]
    y_distance = atom1[1]-atom2[1]
    z_distance = atom1[2]-atom2[2]
    distance = numpy.sqrt(x_distance**2+y_distance**2+z_distance**2)
    return distance

def bond_check(bond_distance, minimum_value=0, maximum_value=1.5):
    """
    Check if distance is a bond.

    Parameters
    ----------
    bond_distance: float
        The distance between the atoms
    minimum_distance: float
        The minimum distance for a bond.
    maximum_distance: float
        The maximum distance for a bond.

    Returns
    ----------
    True if bond
    False if not a bond
    """
    if bond_distance>minimum_value and bond_distance<maximum_value:
        return True
    else:
        return False

def open_xyz(filename):
    xyz_file = numpy.genfromtxt(fname=file_location, skip_header=2, dtype='unicode')
    symbols = xyz_file[:,0]
    coordinates = xyz_file[:,1:]
    coordinates = coordinates.astype(numpy.float)
    return symbols, coord


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise IndexError('No file name given. Script requires an xyz file')


    xyzfilename = sys.argv[1]

    symbols, coord = open_xyz(xyzfilename)

    for numA, atomA in enumerate(coordinates):
        for numB, atomB in enumerate(coordinates):
            if numB<numA:
                distance_AB = calculate_distance(atomA, atomB)
                if bond_check(distance_AB) is True:
                    print(F'{symbols[numA]} to {symbols[numB]} : {distance_AB:.3f}')

    symbols = []
    coordinates = []

    for atom in coord_data:
        atom_data = atom.split()
        symbol = atom_data[0]
        symbols.append(symbol)
        x, y, z = atom_data[1], atom_data[2], atom_data[3]
        coordinates.append([float(x), float(y), float(z)])
