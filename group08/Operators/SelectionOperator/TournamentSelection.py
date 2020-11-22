from group08.Operators.SelectionOperator import SelectionOperator
import numpy as np
class TournamentSelection(SelectionOperator):
    def __init__(self):
        super.__init__
    
    def apply(self, genomes, num):
        k = 2
        p = list()

        for i in range(k-1):
            random = np.random.rand(0,len(genomes))
            if genomes[random] not in p:
                p.append(genomes[random])
        for i in range(k-1):
            if np.random.rand() =< p[i]:
                return p[i]

        return p[k-1]
            

