from Operators.MutationOperator import MutationOperator
from Genome import Genome
import numpy as np


class GaussianOperator (MutationOperator):

    def __init__(self):
        super(MutationOperator, self).__init__()

    def apply(self, genoma):
        res = genoma.getSolucion
        sigma = 0.7
        size = len(genoma.getSolucion())
        for i in range(0, size):
            prob = np.random.rand(0, 1)
            if prob < 0.15:
                index = np.rand(0, len(genoma.getSolucion()))
                res[index] = np.random.normal(sigma, genoma.getSolucion())
        resgen = Genome(res)
        return res