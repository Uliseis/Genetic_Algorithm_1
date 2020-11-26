from group08.Operators.ReplacementOperator import ReplacementOperator


class GenerationalReplacement(ReplacementOperator.ReplacementOperator):

    def __init__(self):
        super().__init__()

    def apply(self, populationActual, populationNueva):
        return populationNueva
