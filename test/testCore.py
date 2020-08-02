import unittest
import sys
sys.path.append('source')
from core import La
import numpy as np

class TestCoreFunctions(unittest.TestCase):
    def testLa(self):
        aValues = np.array([1, 5.0, 10])
        #LaDesired = np.array([1.7627471740390859, 0.3525494348078172, 0.17627471740390859])
        LaDesired = np.array([0.015843117583554896, 0.0031686235167109793, 0.0015843117583554897])
        LaActual = La(aValues)
        np.testing.assert_allclose(LaActual, LaDesired)

