class Genome(solucion, fitness):
    #Solucion candidata
    solucion = list()
    #Fitness de la solucion
    fitness = 0
    def __init__(self, solucion, fitness):
        self.solucion = solucion
        self.fitness = fitness

