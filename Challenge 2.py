#Challenge Exercise 2
class Teacher:
	def __init__(self, name, classRoom, course):
		self.name = name
		self.classRoom = classRoom
		self.course = course

	def GetProfessor(self):
		print("Professor Name is " + self.name)
		print("Professor assigned class is " + self.classRoom)
		print("Professor is teaching " + self.course)

Teacher1 = Teacher("Prof. Sim", "A206", "Python Programming\n")

Teacher2 = Teacher("Prof. Sam", "D109", "English\n")

Teacher1.GetProfessor()
Teacher2.GetProfessor()