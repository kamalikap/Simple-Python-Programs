# String formatting

person = {'name': 'Jenn', 'age': 33}

# sentence = 'My name is {} and I am {} years old'. format(person['name'], person['age'])
# print(sentence)

# sentence = 'My name is {0} and I am {1} years old'. format(person['name'], person['age'])
# print(sentence)

# tag ='h1'

# text= 'This is the headline'

# sentence = '<{0}>{1}<{0}>'.format(tag,text)
# print(sentence)



# class Person():

# 	def __init__(self,name,age):
# 		self.name= name
# 		self.age= age

# p1= Person('Jack', '5')

# sentence = 'My name is {0.name} and I am {0.age} years old'.format(p1)
# print(sentence)



# sentence = 'My name is {name} and I am {age} years old'.format(name='Jack', age='55')
# print(sentence)


# sentence = 'My name is {name} and I am {age} years old'.format(**person)
# print(sentence)

# for i in range(1,11):
# 	sentence = 'The value is {:02}'.format(i)
# 	print(sentence)


# for i in range(1,11):
# 	sentence = 'The value is {:03}'.format(i)
# 	print(sentence)

# pi= 3.14576687
# sentence = 'The value is {:.3f}'.format(pi)
# print(sentence)


# sentence = 'My name is {:,.2f} '.format(1000**2)
# print(sentence)

import datetime
my_date =datetime.datetime(2018,9,24,12,30,45)
print(my_date)


sentence = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(my_date)
print(sentence)







