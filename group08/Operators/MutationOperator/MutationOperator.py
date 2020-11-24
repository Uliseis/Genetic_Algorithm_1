from abc import ABC, abstractmethod

class MutationOperator (ABC):
    @abstractmethod
    def __init__(self):
        pass
    
    @abstractmethod
    def apply(self, genomes):
        pass