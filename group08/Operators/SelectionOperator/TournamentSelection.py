from Operators.SelectionOperator import SelectionOperator
from Population import Population
from Genome import Genome
import numpy as np
import random as rd


class TournamentSelection(SelectionOperator.SelectionOperator):
    k = 0

    def __init__(self):
        super(TournamentSelection, self).__init__()
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


g1 = Genome.Genome([1, 4, 5, 6], 100)
g2 = Genome.Genome([2, 3, 41, 41], 50)
g3 = Genome.Genome([5, 79, 767, 342], 1)
pop = Population(3)
pop.add(g1)
pop.add(g2)
pop.add(g3)
tour = TournamentSelection()
l = tour.apply(pop, 0)
print(l[0].getSolucion())