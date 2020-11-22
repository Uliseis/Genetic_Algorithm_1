from Genome import Genome

class Population():
    population = list()
    psize = 0

    def __init__(self, psize):
        self.psize = psize

    def add(self,genome):
        if len(population)< self.psize:
            if genome not in population:
                population.append(genome)
        else:
            return -1
        return 0

    def remove(self,toremove):
        if len(population) > 1:
            population.remove(toremove)

    def bestFitness(self):
        minimum = float('inf')
        index = 0
        for i in range(len(population)):
            if(minimum < population[i].fitness):
                minimum = population[i].fitness
                index = i
        return population[index]
        
    def sort(self,reverse = False):
        if reverse:
            population.sort(key = bestFitness, reverse = True)
        else:
            population.sort(key = bestFitness)
        return population

    def replaceSol(self, oldsol, newsol):
        i = population.index(oldsol)
        population[i] = newsol
        return i
