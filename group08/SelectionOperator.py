from abc import ABC, abstractmethod

class SelectionOperator (ABC):
    @abstractmethod
    def __init__ (self):
        super.__init__
    
    @abstractmethod
    def apply (self, genomes, num):
        pass