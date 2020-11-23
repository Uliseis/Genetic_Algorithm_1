from Operators.ReplacementOperator import ReplacementOperator

class GenerationalReplacement(ReplacementOperator):
    def __init__(self):
        super(GenerationalReplacement, self).__init__()

    def apply(self, population1, population2):
