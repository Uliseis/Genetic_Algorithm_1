from group08.EA import EA
import numpy as np


def _ackley(x):
    dim = len(x)
    sum1 = 0.0
    sum2 = 0.0

    for n in range(0, dim):
        z = np.abs(x[n])
        sum1 += pow(z, 2)
        sum2 += np.cos(2 * np.pi * z)

    return -20 * np.exp(-0.2 * np.sqrt(sum1 / dim)) - np.exp(sum2 / dim) + 20 + np.e


ea = EA(_ackley, [[-10, 10],[-10, 10]], 50)


print(ea.population.getAverageFitness())
print(ea.best().solucion)
print(ea.best().fitness)

ea.run(50000)

print(ea.population.getAverageFitness())
print(ea.best().solucion)
print(ea.best().fitness)
