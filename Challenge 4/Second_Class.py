import First_Class

def main():
	name = (input('enter the name '))
	address = (input('enter the address '))
	phone = (input('enter the phone '))
	city = (input('enter the city '))
	zip = (input('enter the zip code '))
	age = (input('enter the age '))

	v1 = First_Class.Customer.set_name = name
	v2 = First_Class.Customer.set_address = address
	v3 = First_Class.Customer.set_phone = phone
	v4 = First_Class.Customer.set_city = city
	v5 = First_Class.Customer.set_zip = zip
	v6 = First_Class.Customer.set_age = age

	print("Hello " + v1 + ", your address is " + v2 + ", your # is " + v3 + ", your city is " + v4 + ", your zip code is " + v5 + " and your age is " + v6)
main()
