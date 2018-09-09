class my_exception(Exception):
	pass

class Vector:
	def __init__(self, coords):
		self.coords = coords
		print coords
	def add(self, another_vec):
		if len(self.coords) != len(another_vec.coords):
			raise my_exception("Error")
		else:
			new_coords = [self.coords[i] + another_vec.coords[i] for i in range(0,len(self.coords))]
			return Vector(new_coords)

	def subtract(self, another_vec):
		if len(self.coords) != len(another_vec.coords):
			raise my_exception("Error")
		else:
			new_coords = [self.coords[i] - another_vec.coords[i] for i in range(0,len(self.coords))]
			return Vector(new_coords)

	def dot(self, another_vec):
		if len(self.coords) != len(another_vec.coords):
			raise my_exception("Error")
		else:
			ele_list = [self.coords[i]*another_vec.coords[i] for i in range(0,len(self.coords))]
			return sum(ele_list)

	def norm(self):
		import math
		ele_list = [self.coords[i]**2 for i in range(0,len(self.coords))]
		return math.sqrt(sum(ele_list))

	def toString(self):
		if '(1,2,3)' == str(tuple([self.coords[i] for i in range(0,len(self.coords))])).replace(' ',''):
			print "ok"
		return str(tuple([self.coords[i] for i in range(0,len(self.coords))])).replace(' ','')

	def __str__(self):
		return str(tuple([self.coords[i] for i in range(0,len(self.coords))])).replace(' ','')

	def equals(self, another_vec):
		if (len(self.coords) != len(another_vec.coords)):
			return False
		for i in range(0,len(another_vec.coords)):
			if self.coords[i] != another_vec.coords[i]:
				return False
		return True


a = Vector([1, 2, 3])
b = Vector([3, 4, 5])
c = Vector([5, 6, 7, 8])
print a.equals(a)
print a.add(b)
print a.subtract(b)
print a.dot(b)
print a.norm()
print str(a)
