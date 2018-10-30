class Element(object):
	
	def __init__(self, coefficient=1, power=1, next=None):
		self.coefficient = coefficient
		self.power = power
		self.next = next 
	
	def __repr__(self):
		return '%s, %s' % (self.coefficient, self.power)



class List(object):
	
	def __init__(self):
		self.first = None
		self.last = None


	def add(self, coefficient, power):
		if not self.first:
			self.first = Element(coefficient=coefficient, power=power, next=None)
		else:
			self.first.next = Element(coefficient=coefficient, power=power, next=None)

	def __repr__(self):
		pass



		

