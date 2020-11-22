from Operators.MutationOperator import MutationOperator
import numpy as np

class GaussianOperator (MutationOperator):

    def __init__(self):
        MutationOperator.__init__ (self)

    def apply(self, genoma):
        res = genoma
        sigma = 0.1
        index = np.rand(0, len(genoma.getSolucion()))
        res [index] = np.random.normal(sigma,genoma.getSolucion())
        return res