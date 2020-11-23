from Operators.CrossoverOperator import CrossoverOperator
from Genome import Genome
import numpy as np


class TwoPointOperator(CrossoverOperator.CrossoverOperator):
    def __init__(self):
        super(TwoPointOperator, self).__init__()

    def apply(self, genomas):
        hijo1 = list()
        hijo2 = list()
        size = len(genomas[0].getSolucion())
        indexp1 = np.random.randint(0, size - 1)
        indexp2 = np.random.randint(indexp1 + 1, size-1)

        for i in range(0, indexp1):
            hijo1.append(genomas[0].getSolucion()[i])
            hijo2.append(genomas[1].getSolucion()[i])

        for i in range(indexp1, indexp2):
            hijo1.append(genomas[1].getSolucion()[i])
            hijo2.append(genomas[0].getSolucion()[i])

        for i in range(indexp2, size):
            hijo1.append(genomas[0].getSolucion()[i])
            hijo2.append(genomas[1].getSolucion()[i])

        hijos = [hijo1, hijo2]
        return hijos


l1 = [2, 3, 4, 5]
l2 = [6, 5, 8, 23]
gen1 = Genome.Genome(l1, 76)
gen2 = Genome.Genome(l2, 75)
cr = TwoPointOperator()
la = cr.apply((gen1, gen2))
print(la[0])
print(la[1])
