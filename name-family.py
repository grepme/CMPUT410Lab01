

class Student:
	"""This is a very simple Student class"""
	course_marks = {}
	name = ""
	family = ""
	
	def __init__(self, name, family):
		self.name = name
		self.family = family

	def addCourseMark(self, course, mark):
		"""Add the course to the course dictionary,
		this will overide the old mark if one exists."""
		self.course_marks[course] = mark

	def average(self):
		"""Calculates the average grade percentage based on
		all courses added to the studetn with formula: 
		sum(courses)/count(courses)
		
			-Returns: Integer(0 if no courses)
		"""
		mark_sum = 0
		courses_total = 0
		for course, mark in self.course_marks.items():
			mark_sum += mark
			courses_total += 1
		if courses_total != 0:
			return mark_sum/courses_total
		else:
			return 0

#Start
if __name__ == "__main__":
	
	#Make a new student, John Doe	
	student = Student("John", "Doe")
	
	#Add several course grades
	student.addCourseMark("CMPUT 101", 25)
	student.addCourseMark("SCIENCE 101", 50)
	student.addCourseMark("ART 101", 75)
	student.addCourseMark("MUSIC 101", 100)
	student.addCourseMark("DANCE 101", 50)

	#Print the average, the average should be 60%
	print("{0}'s average is: {1}%".format(student.name, student.average()))
	
