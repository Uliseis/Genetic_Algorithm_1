from Operators.CrossoverOperator import CrossoverOperator
from Genome import Genome
import numpy as np


class TwoPointOperator(CrossoverOperator.CrossoverOperator):
    def __init__(self):
        super().__init__()

    def apply(self, genomas):
        aux1 = list()
        aux2 = list()
        size = len(genomas[0].getSolucion())
        indexp1 = np.random.randint(0, size / 2)
        indexp2 = np.random.randint(size/2, size)

        for i in range(0, size):
            if i < indexp1 or i > indexp2:
                aux1.append(genomas[0].getSolucion()[i])
                aux2.append(genomas[1].getSolucion()[i])
            else:
                aux1.append(genomas[1].getSolucion()[i])
                aux2.append(genomas[0].getSolucion()[i])

        hijo1 = Genome.Genome(aux1, 0)
        hijo2 = Genome.Genome(aux2, 0)
        hijos = [hijo1, hijo2]
        return hijos

