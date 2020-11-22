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
        indexp1 = np.random(0, size - 1)
        indexp2 = np.random(indexp1, size)
        
        for i in range (0, indexp1):
            hijo1 [i] = genomas[0].getSolucion[i]
            hijo2 [i] = genomas[1].getSolucion[i]

        for i in range (indexp1, indexp2):
            hijo1 [i] = genomas[1].getSolucion [i]
            hijo2 [i] = genomas[0].getSolucion [i]

        for i in range (indexp2, size):
            hijo1 [i] = genomas[0].getSolucion [i]
            hijo2 [i] = genomas[1].getSolucion [i]

        hijos = (hijo1,hijo2)
        return hijos
