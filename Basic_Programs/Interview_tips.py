# Difference between Python2 and Python3
# a. print i , print (i)
# b. iteritems(), itmes()
# c. xrange(), range()



1. write in whiteboard

2. know control flow

# for i in rsnge(1,11);
# 	print(i)

# i=1
# while i<=10:
# 	print (i)
# 	i+=1



3. Be able to describe how you used python in the past


4. Know how to solve interview questions

# # Fizzbuzz function

# for i in range(1,21):
# 	if ((i%3 == 0) and (i%5 == 0)):
# 		print('Fizzbuzz ' + str(i))
# 	elif (i%3 == 0):
# 		print('Fizz ' + str(i))
# 	elif (i%5 == 0):
# 		print('Buzz ' + str(i))
# 	else:
# 		print(i)
# # Web scraping records weather each day


# run through file system and find the files with image tags enabled in it.

# import os, glob

# os.chdir("/Users/kamalika/Desktop/python/lists-youtube")
# for file in glob.glob("*.jpg"):
# # 	print(file)

# #Fibonacci sequence
def fib(n):
	if (n == 0): 
		return 0
	if (n == 1): 
		return 1
	else: 
		return fib(n-1)+fib(n-2)

def main():
	for i in range(13):
		print(fib(i))

if __name__ == "__main__":
	main()
 
 # or

# def fib(n):
# 	fib = [0]*n
# 	fib[0] = 0
# 	fib[1] = 1
# 	for i in range(2, n):
# 		fib[i] = fib[i-1] + fib[i-2]

# 	return fib

# def main():
# 	print(fib(7))

# if __name__ == "__main__":
# 	main()

# OR	# 


# # Easiest fibonacci
# # a,b =0,1
# # for i in range(0,10):
# # 	print (a)
# # 	a,b=b,a+b




5. Basic python data types and when to use them

# # Lists
a =[10,12,29,39,2]
for i in a:
	print(i)

# # Tuples
my_tup=(1,2,3,4,5,6,6)
for i in my_tup:
	print(i)

# # Dict
my_dict = {'name': 'Bro', 'key': 'whu', 'Depart': 'value', 'value':'number'}
for key,value in my_dict.items():
	print('My {} is {}'. format(key, value))


# # Sets
# #set is a list with no repeated values, declared using {}
# # set is a unique list
my_set = {1,2,34,5,3,1,245,9}  
for i in my_set:
	print(i)

# Tuple vs list
# 1. can't add, remove elements to a tuple. Tuples are immutable and list are not.
# 2. can use 'in' operator to check if the element exists or not




6. how to use list comprehensions- helps you to stand out

my_list= [1,2,34,5,6,7,7,8]

sq= [i*i for i in my_list]
print(sq)



7. know how to use generators


# Fibonacci with generators, 
# yield is the keyword for generators
def fib(num):
	a,b =0,1
	for i in range(0,num):
		yield("{}: {}".format(i+1,a))
		a,b=b, a+b

for item in fib(10):
	print(item)




8.Know the basics of OOP
# class Person():
# 	def __init__(self, name):
# 		self.name= name

# 	def reveal_identity(self):
# 		print('My name is: {}'.format(self.name))

# class SuperHero(Person):
# 	def __init__(self, name, hero):
# 		super(SuperHero, self).__init__(name)
# 		self.hero = hero

# 	def new_identity(self):
# 		super(SuperHero, self).reveal_identity()
# 		print("And there {} was". format(self.hero))


# # new_name= Person('bob')
# # new_name.reveal_identity()

# wade = SuperHero("wade","deadpool")
# wade.new_identity()



 9. Have related questions ready to ask the interviewer
# ans. difference in python2 and Python3
# do you guys use python2 or python3?
# what would you recommend and why?

# What they are using in unit testing?
# what are they using in python database?




10. Basics of other Technologies
# Version control
# # navigate through linux
# basic sql
# how database work

# T-shaped skillset- advanced in certain topic and exposed to other technologies.









