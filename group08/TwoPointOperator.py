from group08.Genome import CrossoverOperator
import numpy as np
class TwoPointOperator(CrossoverOperator):

    def __init__(self):
        CrossoverOperator.__init__ (self)
    
    def apply(self, genomas):
        index1 = np.rand(0, genomas [0].size)
        index2 = np.rand (0, genomas [0].size)
        hijo1 = 
