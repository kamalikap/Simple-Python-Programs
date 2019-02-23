#Renaming the files and then sort them in order


import os

os.chdir('/Users/kamalika/Desktop/python/lists-youtube')

# print (os.getcwd())

for f in os.listdir():
	filename, file_ext= os.path.splitext(f)
	f_title, f_course, f_num = filename.split('_')
	
	f_title = f_title.strip()
	f_course = 	f_course.strip()
	f_num = 	f_num.strip()[1:].zfill(2)  #stripng the '# ' number sign and putting zero in the number

	new_name= '{}-{}{}'.format(f_num,f_title,file_ext)

	os.rename(f, new_name)
