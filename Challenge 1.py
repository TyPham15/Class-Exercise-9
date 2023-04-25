#Challenge Exercise 1

class Students:
	def GetInformation(self):
		print("\nstudent Lastname name is " + self.Lastname)
		print("student Firstname name is " + self.Firstname)
		print("student Address name is " + self.Address)
		print("student City name is " + self.City)
		print("student State name is " + self.State)
		print("student Zipcode name is " + self.Zipcode)

Student1 = Students()
Student1.Lastname = "Doe"
Student1.Firstname = "Jane"
Student1.Address = "111 St"
Student1.City = "Santa Ana"
Student1.State = "CA"
Student1.Zipcode = "12345"

Student2 = Students()
Student2.Lastname = "Cantor"
Student2.Firstname = "Mike"
Student2.Address = "222 St"
Student2.City = "Garden Grove"
Student2.State = "CA"
Student2.Zipcode = "67890"

Student3 = Students()
Student3.Lastname = str(input("Enter Student 3's last name: "))
Student3.Firstname = str(input("Enter Student 3's first name: "))
Student3.Address = str(input("Enter Student 3's address: "))
Student3.City = str(input("Enter Student 3's city: "))
Student3.State = str(input("Enter Student 3's state: "))
Student3.Zipcode = str(input("Enter Student 3's zip code: "))

Student1.GetInformation()
Student2.GetInformation()
Student3.GetInformation()