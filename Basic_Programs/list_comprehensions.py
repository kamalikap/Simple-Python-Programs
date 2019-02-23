#list comprehensions


nums = [1,2,3,4,5,6,7,8,9,10]

my_list = []
for n in nums:
	my_list.append(n)
print (my_list)

my_list = [n for n in nums]
print (my_list)

my_list = []
for n in nums:
	my_list.append(n*n)
print (my_list)

my_list = [n*n for n in nums]
print (my_list)


Using map and lambda
my_list = map(lambda n: n*n, nums)
print (my_list)

my_list = []
for n in nums:
	if n%2 ==0 :
		my_list.append(n)
print (my_list)

my_list = [n for n in nums if n%2 == 0]
print (my_list)

# Using map and lambda
my_list = filter(lambda n: n%2 == 0, nums)
print (my_list)


my_list = []
for letter in 'abcd':
	for n in range(4):
		my_list.append((letter,n))
print (my_list)

my_list = [(letter, n) for letter in 'abcd' for n in range(4)]
print (my_list)

letter = 'abcd'
n = [1,2,3,4]
y=zip(letter, n)
print (y)



# Dictionary
names= ['a', 'b', 'c', 'd']
heroes = ['1', '2', '3', '4']

my_dict = {}
for names, heroes in zip(names, heroes):
	my_dict[names]= heroes
print(my_dict)



my_dict = {names: heroes for names, heroes in zip(names,heroes)}
print (my_dict)

my_dict = {names: heroes for names, heroes in zip(names,heroes) if names != 'a'}
print (my_dict)




# Set comprehensions


n = [1,1,2,1,3,4,23,5,5,7,4,9,9,8,4]

my_set = set()
for i in n:
	my_set.add(i)
print (my_set)


my_set = {i for i in n}
print(my_set)




# generator expression

def gen_func(nums):
	for n in nums:
		yield n*n

my_gen = gen_func(nums)

my_gen = (n*n for n in nums)

for i in my_gen:
	print (i)
	








