from Operators.MutationOperator import MutationOperator
from Genome import Genome
import numpy as np
from EA import EA


class GaussianOperator (MutationOperator.MutationOperator):

    def __init__(self):
        super(MutationOperator.MutationOperator, self).__init__()

    def apply(self, genoma):
        res = genoma.getSolucion()
        sigma = 0.5
        size = len(genoma.getSolucion())
        for i in range(0, size):
            prob = np.random.rand()
            if prob < 0.15:
                res[i] = np.random.normal(genoma.getSolucion()[i], sigma)
        return Genome.Genome(res, EA.calcular_fitness(res))


gen = Genome.Genome([1.3, 5, 6.7, 34], 0)
g = GaussianOperator()
g1 = g.apply(gen)
print(g1.getSolucion())