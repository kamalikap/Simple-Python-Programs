import csv

# with open ('names.csv','r') as csv_file:
# 	csv_reader = csv.reader(csv_file)

# 	# print(csv_reader)

# 	next(csv_reader)

# 	for line in csv_reader:
# 		# print(line)
# 		print(line[2])



with open ('names.csv','r') as csv_file:
	csv_reader = csv.reader(csv_file)

	with open('new_names',csv','w) as new_file:
		csv_writer = csv.writer(new_file, delimiter='\t')   #\t=tab, '-'
	
		for line in csv_reader:
			csv_writer.writerow(line)



#Only the email from the csv file using Dictreader
# with open ('names.csv','r') as csv_file:
# 	csv_reader = csv.Dictreader(csv_file)
# 		for line in csv_reader:
# 			print(line['email'])





# Dict reader and writer

with open ('names.csv','r') as csv_file:
	csv_reader = csv.Dictreader(csv_file)

	with open('new_names',csv','w) as new_file:
		fieldnames= ['first', 'last', 'email']
		# fieldnames= ['first', 'last']
		csv_writer = csv.Dictwriter(new_file,fieldnames=fieldnames, delimiter='\t')   #\t=tab, '-'
		
		csv_writer.writeheader()

		for line in csv_reader:
			# del line['email']
			csv_writer.writerow(line)








