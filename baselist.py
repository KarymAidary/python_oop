class Element(object):
	"""docstring for Element"""
	def __init__(self, coefficient, power, nexxt):
		self.coefficient = coefficient
		self.power = power
		self.next = nexxt 
		
	def add(self, coefficient, power):
		if not self.first:
			self.first = Element(coefficient=coefficient, power=power, next=None)
		else:
			self.first.next = Element(coefficient=coefficient, power=power, next=None)

	def __str__(self):
		pass