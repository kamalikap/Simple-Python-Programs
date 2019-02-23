

# Sorting

li=[9,3,40,23,4,1,5,6,2,42,8,9,4,5]

# s_li = sorted(li, reverse= True)  #sorted function 
# print ('Sorted:\t', s_li)

# li.sort(reverse= True)           #sort method

# print ('UnSorted:\t', li)



# tup=(9,3,40,23,4,1,5,6,2,42,8,9,4,5)
# s_li = sorted(tup)  #sorted function 
# print ('Sorted:\t', s_li)

# di = {'dsd': 'ddsd', 'erewr': 'ffwefew', 'trr':'tete', 'aaa':'fewfew'}
# s_li = sorted(di)  #sorted function 
# print ('Sorted:\t', s_li)


li= [-3,5,-9,-2,7,-4]
s_li = sorted(li, key = abs)
print(s_li)


# Employee- name, age, salary
# repr- name, age. $ salary

class Employee:

	def __init__(self, name, age, salary):
		self.name = name
		self.age = age
		self.salary = salary

	def __repr__(self):
		return '{} {} ${}'.format(self.name,self.age,self.salary)


# Using attrgetter

from operator import attrgetter

e1 = Employee('cdscs',23,32332)
e2 = Employee('dewdw',32,3155)
e3 = Employee('rtgtrg',42, 324234)
e4 = Employee('hyhr', 88, 34543)


employees= [e1, e2, e3,e4]

# def e_sort(emp):
# 	return (emp.salary)

# s_emp = sorted(employees, key= e_sort, reverse=True)

s_emp = sorted(employees, key= attrgetter('age'))

print(s_emp)

























