#File Objects

# f= open('test.txt', 'r')        #read
# # f= open('test.txt', 'w')        #write
# # f= open('test.txt', 'a')      #append
# # f= open('test.txt', 'r+')       #read and write

# # print(f.name)
# print(f.mode)

# f.close()


# with open('test.txt', 'r') as f:
	# f_contents=f.read()
	# f_contents=f.readlines()     #creates a list
	# f_contents=f.readline()     #reads first line
	# print(f_contents, end='')
	
	# for line in f:
	# 	print(line, end='')

	# f_contents=f.read(100)     #prints out 100 characters of the file
	# print(f_contents, end='')

	# siz_read= 10
	# f_contents=f.read(siz_read)
	# print(f_contents, end='')


	# f.seek(0)   #starts with the beginning of the file

	# f_contents=f.read(siz_read)
	# print(f_contents, end='')


	# print(f.tell())
	# while len(f_contents) > 0:
	# 	print(f_contents, end='*')
	# 	f_contents=f.read(siz_read) 


# with open('test2.txt', 'w') as f:
# 	f.write('Test\n')
# 	f.seek(0)
# 	f.write('zr=est\n')
# 	f.write('Test')
# 	# pass




#reading from one file and writing to another
with open('test.txt', 'r') as rf:
	with open('test_copy.txt', 'w') as wf:
		for line in rf:
			wf.write(line)


# working with images we have to use binary mode

with open('bro.JPG', 'rb') as rf:
	with open('bro_copy.jpg', 'wb') as wf:
		for line in rf:
			wf.write(line)


# with open('bro.JPG', 'rb') as rf:
# 	with open('bro_copy2.jpg', 'wb') as wf:
# 		chunk_size = 4096
# 		rf_chunk = rf.read(chunk_size)
# 		while len(rf_chunk) > 0:
# 			wf.write (rf_chunk)
# 			rf_chunk = rf.read(chunk_size)


















