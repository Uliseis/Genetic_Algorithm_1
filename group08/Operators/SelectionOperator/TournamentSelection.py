from Operators.SelectionOperator import SelectionOperator
from Population import Population
from Genome import Genome
import numpy as np
import random as rd


class TournamentSelection(SelectionOperator.SelectionOperator):
    k = 0

    def __init__(self):
        super().__init__()
        self.k = 2

    def apply(self, genomes, num):
        p = self.select(genomes.population)
        total = self.total(p)
        props = [None] * self.k
        for i in range(self.k):
            props[i] = p[i].fitness / total
            rand = np.random.rand()
            if rand <= props[i]:
                return [p[i]]

        return [p[self.k - 1]]

    def select(self, genomes):
        selected = list()
        for i in range(self.k):
            random = rd.randint(0, len(genomes)-1)
            if genomes[random] not in selected:
                selected.append(genomes[random])
            else:
                i = i - 1
        return selected

    @staticmethod
    def total(selected):
        total = 0
        for i in selected:
            total += i.fitness
        return total

