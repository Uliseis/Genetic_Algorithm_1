from group08.Operators.MutationOperator import MutationOperator
from group08.Genome import Genome
import numpy as np


class GaussianOperator (MutationOperator.MutationOperator):

    def __init__(self):
        super().__init__()

    def apply(self, genomas):
        genoma = genomas[0]
        res = genoma.getSolucion()
        sigma = 0.5
        size = len(genoma.getSolucion())
        for i in range(0, size):
            prob = np.random.rand()
            if prob < 0.15:
                res[i] = np.random.normal(genoma.getSolucion()[i], sigma)
        return Genome.Genome(res, 0)


