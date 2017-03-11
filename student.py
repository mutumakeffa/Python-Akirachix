class Student(object):
	"""docstring for student """
	def __init__(self, first_name, last_name, age, gender):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.gender = gender
		

	def show_name (self):
		fullname = "{} {}".format (self.first_name, self.last_name)
		return fullname

	def year_of_birth(self):
		year = 2017 - self.age
		return year


		