#Python OOPs

# Simple employee class

class Employee:

	def __init__(self,first,last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + "." + last + '@company.com'


	def fullname(self):
		return '{} {}' .format(self.first, self.last)
	


emp_1 = Employee('corey','schraf', 3000)
emp_2 = Employee('test', 'user', 5999)

"""
print(emp_1)
print(emp_2)

emp_1.first = "Corey"
emp_1.last = "Scharaf"
emp_1.email = "corey.Scharaf@compnay.com"
emp_1.pay = 60000

emp_2.first = "Cor"
emp_2.last = "Sch"
emp_2.email = "cory.Sraf@compnay.com"
emp_2.pay = 5500


#emp_1 is an instance 
fullname is a method. 
first,last, pay , email are attributes.
employee- class

"""
print(emp_1.email)
print(emp_2.email)


#print('{} {}' .format(emp_1.first, emp_1.last))

print(Employee.fullname(emp_1))
print(emp_1.fullname()) #method so there should be a paranthesis




