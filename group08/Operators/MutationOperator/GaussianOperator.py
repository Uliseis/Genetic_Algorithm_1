from group08 import MutationOperator
import numpy as np

class GaussianOperator (MutationOperator):

    def __init__(self):
        MutationOperator.__init__ (self)

    def apply(self, genoma):
        res = list()
        for i in range (len(res)):
            sigma = sigma * np.exp(tau * N(0, 1))
            res [i] = genoma + sigma * N(0, 1)
        return res