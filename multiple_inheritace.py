class body:
	def __init__(self, length , breath):
		self.length = length
		self.breath = breath

	def print_length(self):
		print(self.length)

	def print_breath(self):
		print(self.breath)

class tier:
	def __init__(self, front_radius , backradius):
		self.f_radius  = front_radius
		self.b_radius = backradius

	def print_length(self):
		print(self.f_radius)
	
	def backradius(self):
		print(self.b_radius)

class car(tier, body):
	def __init__(self, length, breath, front_radius, backradius, name):
		body.__init__(self, length, breath)
		tier.__init__(self, front_radius, backradius)
		self.name = name

	def print_all(self):
		body.print_length(self)
		self.print_breath()
		tier.print_length(self)
		self.backradius()
		print(self.name)
		print('area', self.length*self.breath)

c = car(1,4,3,2,'temp')
c.print_all()

