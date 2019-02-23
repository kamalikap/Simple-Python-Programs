
#Random numbers

import random

# value = random.uniform(1, 10). #random float value
# print(value)


# value = random.randint(1, 6)   #random value integer for a dice
# print(value)

# value = random.randint(0, 1)
# print(value)

# greetings= ['hello', 'hi', 'hey', 'hola', 'howdy']

# value = random.choice(greetings)
# print(value)


# colors=['red', 'black', 'blue', 'yellow']
# value = random.choices(colors, k=10)
# print(value)

# value = random.choices(colors, weights= [18,18, 2, 4], k=10)
# print(value)


# deck = list(range(1,53))
# random.shuffle(deck)
# print(deck)

# deck = list(range(1,53))
# hand = random.sample(deck, k=5) #sample is used for unique values
# print(hand)


# Random addres and phone number

# Parameters
# first name, last name, rand phone number, 
# rand street number, street name, city, state, rand zipcode, email

# f_name= ['Joey', 'gerth', 'oprah', 'ross', 'phoebe']
# l_name = ['geller','hampsted','beth', 'gary','dunkins']

# street = ['gauh','diuedh','dfui','njdfh','vdhj']
# city= ['dfec','fdefc','dfef','hyhy','gtrgr']
# state = ['F','CS','CA','MN','KN']

# for n in range(20):
# 	first = random.choice(f_name)
# 	last = random.choice(l_name)

# 	ph_num= f'{random.randint(100, 999)}-555-{random.randint(1000, 9999)}'
# 	street_num= random.randint(100,999)
# 	street_name= random.choice(street)
# 	city_name= random.choice(city)
# 	state_name= random.choice(state)
# 	zipcode = random.randint(10000,99999)
# 	email= first.lower() + last.lower() + '@bogusemail.com'

# 	print (f'{first} {last}\n {ph_num}\n {street_num} {street_name} St., {city_name} {state_name} {zipcode}\n{email}\n')



# Prints single number
num = list(range(100,999))
n = random.sample(num, k=3)

my_list= []
for number in num:
	if number%5==0:
		my_list.append(number)
print(number)



# Prints range of number

for num in range(3):
	print(random.randrange(100,999,5), end =',')

li=list(range(100))
random.shuffle(li)

print(li)


# for num in range(100):
n = list(range(10000,99999))
nu =random.sample(n, k=2)
print(nu)

"""
random.uniform
random.randint
random.choice
random.choices
random.shuffle
random.sample
random.randrange
"""