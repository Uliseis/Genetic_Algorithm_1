from Genome import * 
class Population(Genome):
    global population = list()
    psize = 0
    def __init__(self, psize):
        self.psize = psize

    def add(self,Genome):
        if len(population)< self.psize
            if Genome not in population:
                population.append(Genome)
        else:
            return -1
        return 0

    def remove(self,toRemove):
        if len(population) > 1
            population.remove(toRemove)

    def bestFitness(self,elem):
        min = float('inf')
        index = 0
        for i in range(len(population)):
            if(min < population[i].fitness):
                min = population[i].fitness
                index = i
        return population[index]
        
    def sort(self,reverse = False):
        if reverse:
            population.sort(key = bestFitness, reverse = True)
        else:
            population.sort(key = bestFitness)
        return population

    def replaceSol(self, oldSol, newSol):
        i = population.index(oldSol)
        population[i] = newSol
        return i
