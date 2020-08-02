import numpy as np
import sys
sys.path.append('source')
from core import *

Nx = 30
Ny = Nx
Nz = 2
plateSeparation = 1e-3
plateDiameter = 1.0
a = plateDiameter / Nx /2

cellCenters = np.mgrid[-plateDiameter/2:plateDiameter/2:plateDiameter/Nx,
    -plateDiameter/2:plateDiameter/2:plateDiameter/Ny,
    0:plateSeparation*2:plateSeparation].T.reshape(-1,3)
cellCenters += np.array([plateDiameter/Nx/2, plateDiameter/Ny/2, -plateSeparation/2])

matrixSize = len(cellCenters)
matrixHalfSize = int(matrixSize/2)
LijMatrix = np.zeros((matrixSize, matrixSize))
for i in range(matrixSize):
    for j in range(matrixSize):
        LijMatrix[i, j] = Lij(a, cellCenters[i], cellCenters[j])


voltages = 0.5*np.ones((matrixSize, 1))
voltages[matrixHalfSize:] *= -1
charges = np.linalg.solve(LijMatrix, voltages)
plate1Charge = np.sum(charges[0:matrixHalfSize])
plate2Charge = np.sum(charges[matrixHalfSize:])
chargeConservation = plate1Charge + plate2Charge
capacitance = plate1Charge
Cpp = epsilon0 * plateDiameter * plateDiameter / plateSeparation
print(cellCenters)
print(charges)
print(capacitance/Cpp)
print(Cpp)
print(chargeConservation)
