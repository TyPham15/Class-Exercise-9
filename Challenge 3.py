#Challenge Exercise 3
class PI:
	def GetInformation(self, LN, FN, Age, Addr, City, State, Zip):
		return LN + " , " + FN + " , " + str(Age) + " , " + Addr + " , " + City + " , " + State + " , " + str(Zip)

PersonalInformation = PI()
PersonalInformation.Lastname = input('enter the last name ')
PersonalInformation.Firstname = input('enter the first name ')
PersonalInformation.Age = int(input('enter the age '))
PersonalInformation.Address = str(input('enter the address '))
PersonalInformation.City = str(input('enter the city '))
PersonalInformation.State = str(input('enter the state '))
PersonalInformation.Zipcode = int(input('enter the zip code '))


print(PersonalInformation.GetInformation(PersonalInformation.Lastname,
										 PersonalInformation.Firstname,
										 PersonalInformation.Age,
										 PersonalInformation.Address,
										 PersonalInformation.City,
										 PersonalInformation.State,
										 PersonalInformation.Zipcode))
