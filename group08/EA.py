from Population import Population
from Genome import Genome

import numpy as np

class EA(object):
	"""docstring for EA"""
	bounds = list ()
	psize = 0
	best = 0
	population = Population ()

	def __init__(self,minfun,bounds,psize):
		print(np.random.rand())
		super(EA, self).__init__()
		self.minfun = minfun
		self.bounds = bounds
		self.psize = psize
		
	def run (self,num):
		#for i in range(num):
			#algoritmo (param)
		self.population = Population.sort ()
		self.best = population [0]

	def iniciarPoblacion(self):
		for i in range(psize):
			listaVariables = list()
			for j in range(len(self.bounds)):
				listaVariables.append(np.random.rand(bounds[j][0], bounds[j][1]))
			gen = Genome(listaVariables, self.minfun(listaVariables))
			self.population.add(gen)

	def best (self):
		return best

ej = EA()
