from Genome.Genome import Genome
from Population import Population

import numpy as np

class EA(object):
	"""docstring for EA"""
	bounds = list ()
	psize = 0
	best = 0
	population = Population ()

	def __init__(self, minfun, bounds, psize):
		print(np.random.rand())
		super(EA, self).__init__()
		self.minfun = minfun
		self.bounds = bounds
		self.psize = psize
		
	def run (self,num):
		#for i in range(num):
			#algoritmo (param)
		self.population = Population.sort ()
		self.best = self.population[0]

	def iniciarpoblacion(self):
		for i in range(self.psize):
			listaVariables = list()
			for j in range(len(self.bounds)):
				listaVariables.append(np.random.rand(self.bounds[j][0], self.bounds[j][1]))
			gen = Genome(listaVariables, self.minfun(listaVariables))
			self.population.add(gen)

	@staticmethod
	def calcular_fitness(self, variables):
		return self.minfun(variables)

	def best (self):
		return self.best

