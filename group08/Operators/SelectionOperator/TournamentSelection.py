from Operators.SelectionOperator import SelectionOperator
from Genome import Genome

import numpy as np


class TournamentSelection(SelectionOperator):
    k = 0

    def __init__(self):
        super.__init__()
        self.k = 2

    def apply(self, genomes, num):
        p = self.select(genomes)
        total = self.total(p)
        props = [None] * self.k
        for i in range(self.k):
            props[i] = p[i].fitness / total
            rand = np.random.rand()
            if rand >= props[i]:
                return p[i]

        return p[self.k - 1]

    def select(self, genomes):
        selected = [None] * self.k
        for i in range(self.k):
            random = np.random.rand(0, len(genomes))
            if genomes[random] not in selected:
                selected[i] = genomes[random]
        return selected

    @staticmethod
    def total(selected):
        total = 0
        for i in selected:
            total += i.fitness
        return total
