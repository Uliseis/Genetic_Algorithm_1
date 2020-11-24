from abc import ABC, abstractmethod

class CrossoverOperator(ABC):
    
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def apply(self, genomas):
        pass
