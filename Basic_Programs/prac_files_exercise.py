

with open ('test.txt', 'r') as f:
	print(f.read())




# #read n lines in python
# with open ('test.txt', 'r') as f:
# 	# n=2
# 	# new= [next(f) for x in range(n)]
# 	# print(new)

# 	#OR

	print(f.readlines()[0:n])





#Apend text to a file and display it
with open ('test.txt', 'a+') as f:
	f.write('Test')
	f.seek(0)
	f.read()




#last n lines
with open('test.txt', 'r') as f:
	f.readlines()[:-n]



# Creating a list and store it into a variable
# with open('test.txt', 'r') as f:
# 	data= f.readlines()
# 	pritn(data)




# # read and store it to an array
# with open('test.txt', 'r') as f:
# 	arr= []
# 	for i in f:
# 		arr.append(i)
# 	print(arr)



# program to find the longest word in a file
with open('test.txt', 'r') as f:
	word= f.read().split()
	max_len= len(max(word, key= len))
	for i in word:
		if len(i)== max_len:
			print(i)



# Count the frequency of the word in a file

from collections import Counter
def freq_wrd(filename):
	with open(filename, 'r') as f:
		word= Counter(f.read().split())
		print (word)

freq_wrd('test.txt')





# get the file size of a plain file
# import os
# stat = os.stat('test.txt')
# print(stat)
# # print(stat.st_size)




#  write a list to a file
# def list_file(f_name, color):
# 	with open(f_name, 'w') as f:
# 		for c in color:
# 			f.write(c)

# color =['e','r','t','gf','fw','dfd']
# list_file('test2.txt',color)





# Copy the  contents of a file
# def copy_file(f_name,new_file):
# 	with open(f_name, 'r') as rf:
# 		with open(new_file, 'w') as wf:
# 			for line in rf:
# 				wf.write(line)

# copy_file('test.txt', 'test3.txt')




# #copy each line from first line with the corresponding line in second line.
with open('test.txt') as f1, open('test3.txt') as f2:
	for l1,l2 in zip(f1,f2):
		print(l1+l2)


# read a random line from a file
import random
with open ('test.txt', 'r') as f:
	data=f.read().splitlines()      #split= will split into words
									#splitlines()= will split into lines
	print(random.choice(data))


# program to asses if a file is closed or not
with open('test.txt', 'r') as f:
	print(f.closed)
	f.close()
	print(f.closed)



#remove newline character from a file
with open('test.txt', 'r') as f:
	data= f.readlines()
	data1= [i.rstrip('\n') for i in data]
	print(data1)




#swaping in python
# x,y = 1,2
# x,y = y,x
# print(x,y)