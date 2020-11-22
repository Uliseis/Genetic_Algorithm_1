from Operators.CrossoverOperator import CrossoverOperator
from Genome import Genome
import numpy as np
class TwoPointOperator(CrossoverOperator):

    def __init__(self):
        CrossoverOperator.__init__ (self)
    
    def apply(self, genomas):
        hijo1 = list()
        hijo2 = list()
        size = len(genomas [0])
        indexp1 = np.rand(1, size - 3)
        indexp2 = np.rand (indexp1, size - 2)
        
        for i in range (0, indexp1):
            hijo1 [i] = genomas[0].solucion[i]
            hijo2 [i] = genomas[1].solucion[i]

        for i in range (indexp1, indexp2):
            hijo1 [i] = genomas[1].solucion [i]
            hijo2 [i] = genomas[0].solucion [i]

        for i in range (indexp2, size):
            hijo1 [i] = genomas[0].solucion [i]
            hijo2 [i] = genomas[1].solucion [i]

        hijos = (hijo1,hijo2)
        return hijos
