import math

from Genome.Genome import Genome
from Population import Population
from Operators.CrossoverOperator import TwoPointOperator
from Operators.MutationOperator import GaussianOperator
from Operators.SelectionOperator import TournamentSelection
from Operators.ReplacementOperator import GenerationalReplacement

import numpy as np
import random

class EA(object):
	"""docstring for EA"""
	bounds = list ()
	psize = 0
	population = Population(0)
	crossOper = None
	mutOper = None
	replOper = None
	selecOper = None
	minfun = None

	def __init__(self, minfun, bounds, psize):
		super(EA, self).__init__()
		self.minfun = minfun
		self.bounds = bounds
		self.psize = psize
		self.population = Population(len(bounds))
		self.crossOper = TwoPointOperator.TwoPointOperator()
		self.mutOper = GaussianOperator.GaussianOperator()
		self.replOper = GenerationalReplacement.GenerationalReplacement()
		self.selecOper = TournamentSelection.TournamentSelection()
		self.initpopulation()
		
	def run(self,num):
		for i in range(num):
			self.population = self.algorithm(self.population)

	def algorithm(self, popul):
		newpopulation = Population(self.psize)
		for i in range(0, math.floor(self.psize/2)):
			selected = [self.selecOper.apply(popul, 0)[0], self.selecOper.apply(popul, 0)[0]]
			crossed = self.crossOper.apply(selected)
			crossed[0].fitness = self.calcular_fitness(crossed[0].getSolucion())
			crossed[1].fitness = self.calcular_fitness(crossed[1].getSolucion())
			gen1 = self.mutOper.apply([crossed[0]])
			gen1.fitness = self.calcular_fitness(gen1.getSolucion())
			gen2 = self.mutOper.apply([crossed[1]])
			gen2.fitness = self.calcular_fitness(gen2.getSolucion())
			newpopulation.add(gen1)
			newpopulation.add(gen2)
		return self.replOper.apply(popul, newpopulation)

	def initpopulation(self):
		for i in range(self.psize):
			listaVariables = list()
			for j in range(len(self.bounds)):
				listaVariables.append(random.uniform(self.bounds[j][0], self.bounds[j][1]))
			gen = Genome(listaVariables, self.calcular_fitness(listaVariables))
			self.population.add(gen)

	def calcular_fitness(self, variables):
		valorfuncion = self.minfun(variables)
		return (1/(1 + valorfuncion)) * 100

	def best(self):
		return self.population.bestFitness()



def f(l):
	return

ea = EA(f, [[-5,5], [-5,5]], 50)
print(ea.population.getAverageFitness())
print(ea.best().getSolucion())
print (ea.best().getFitness())
ea.run(50000)
print(ea.population.getAverageFitness())
print(ea.best().getSolucion())
print (ea.best().getFitness())