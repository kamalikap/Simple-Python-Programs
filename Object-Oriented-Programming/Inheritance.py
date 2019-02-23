
# Inheritance

class Employee:

	num_of_emps = 0
	raise_amount = 1.04

	def __init__(self,first,last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + "." + last + '@company.com'


		Employee.num_of_emps += 1


	def fullname(self):
		return '{} {}' .format(self.first, self.last)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)


class Developer(Employee):
	raise_amount = 1.10

	def __init__(self,first,last, pay, program):
		super().__init__(first,last, pay)         # super to call the parent class
		# Employee.__init__(self,first,last, pay)      comment-both are same
		self.program = program


class Manager(Employee):
	raise_amount = 1.40

	def __init__(self,first,last, pay, employees= None):
		super().__init__(first,last, pay)
		if employees is None:
			self.employees = []
		else:
			self.employees = employees

	def add_emp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)


	def remove_emp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)

	def print_emp(self):
		for emp in self.employees:
			print('-->', emp.fullname())


emp_1 = Developer('corey','schraf', 3000, 'java')
emp_2 = Developer('test', 'user', 5999, 'Python')


# print(help(Developer))

# print(emp_1.email)
# print(emp_2.program)

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)


mgr_1 = Manager('sudy', 'fdyufuy', 47687, [emp_1])

# print(mgr_1.email)

# mgr_1.add_emp(emp_2)
# mgr_1.remove_emp(emp_1)
# mgr_1.print_emp()

# print(isinstance(mgr_1,Developer))


print(issubclass(Manager, Employee))




# Polymorphism-same function name with different types

# print(len("greek"))
# print(len([10,102,4,3]))


class A:
    def explore(self):
        print("explore() method from class A")
 
class B(A):
    def explore(self):
        print("explore() method from class B")
 
 
b_obj = B()
a_obj = A()
 
b_obj.explore()
a_obj.explore()






# Encapsulation- prevents data being modified accidently

# !/usr/bin/env python
 
class Car:
 
def __init__(self):
	self.__updateSoftware()
 
def drive(self):
	print 'driving'
 
def __updateSoftware(self):
	print 'updating software'
 
redcar = Car()
redcar.drive()
#redcar.__updateSoftware()  not accesible from object.






