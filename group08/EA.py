class EA(object):
	"""docstring for EA"""
	bounds = list ()
	psize = 0
	best = 0
	def __init__(self,minfun,bounds,psize):
		super(EA, self).__init__()
		self.minfun = minfun
		self.bounds = bounds
		self.psize = psize
		
	def run (self,num):
		for i in range(num):
			algoritmo (param)
		self.best = population (loqsea)

	def best ():
		return best

