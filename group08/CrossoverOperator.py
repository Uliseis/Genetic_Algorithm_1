from abc import ABC, abstractmethod

class CrossoverOperator(ABC):
    @abstractmethod
    def __init__(self):
        super.__init__
        
    @abstractmethod
    def apply(self, genomas):
        pass
