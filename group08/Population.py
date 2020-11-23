
from Genome import Genome

class Population():
    global population
    psize = 0

    def __init__(self, psize):
        self.psize = psize
        self.population = list()

    def add(self,genome):
        if len(self.population)< self.psize:
            if genome not in self.population:
                self.population.append(genome)
        else:
            return -1
        return 0

    def remove(self,toremove):
        if len(self.population) > 1:
            self.population.remove(toremove)

    def bestFitness(self):
        minimum = float('inf')
        index = 0
        for i in range(len(self.population)):
            if minimum < self.population[i].fitness:
                minimum = self.population[i].fitness
                index = i
        return self.population[index]
        
    def sort(self,reverse = False):
        if reverse:
            self.population.sort(key = Genome.bestFitness, reverse = True)
        else:
            self.population.sort(key = Genome.bestFitness)
        return self.population

    def replaceSol(self, oldsol, newsol):
        i = self.population.index(oldsol)
        self.population[i] = newsol
        return i
