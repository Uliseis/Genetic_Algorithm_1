from group08.TwoPointOperator import TwoPointOperator
from group08.Population import Population
class EA(object):
	"""docstring for EA"""
	bounds = list ()
	psize = 0
	best = 0
	operator = TwoPointOperator ()
	population = Population ()
	def __init__(self,minfun,bounds,psize):
		super(EA, self).__init__()
		self.minfun = minfun
		self.bounds = bounds
		self.psize = psize
		
	def run (self,num):
		for i in range(num):
			algoritmo (param)
		self.population = Population.sort ()
		self.best = population [0]


	def best (self):
		return best

