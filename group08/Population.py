from Genome import Genome


class Population:
    population = None
    psize = 0

    def __init__(self, psize):
        self.psize = psize
        self.population = list()

    def add(self, genome):
        if len(self.population) < self.psize:
            self.population.append(genome)
        else:
            return -1
        return 0

    def remove(self, toremove):
        if len(self.population) > 1:
            self.population.remove(toremove)

    def sortFitness(self):
        minimum = float('inf')
        index = 0
        for i in range(len(self.population)):
            if minimum < self.population[i].fitness:
                minimum = self.population[i].fitness
                index = i
        return self.population[index]

    def sort(self, reverse=False):
        if reverse:
            self.population.sort(key=Genome.sortFitness, reverse=True)
        else:
            self.population.sort(key=Genome.sortFitness)
        return self.population

    def bestFitness (self):
        self.sort()
        return self.population [0]

    def replaceSol(self, oldsol, newsol):
        i = self.population.index(oldsol)
        self.population[i] = newsol
        return i

    def getTotalFitness(self):
        total = 0
        for i in range(self.psize):
            total += self.population[i].getFitness()
        return total

    def getAvergeFitness(self):
        return self.getTotalFitness()/self.psize