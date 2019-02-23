import os
from datetime import datetime

# print(dir(os))
# print(os.getcwd())

# os.chdir('/Users/kamalika/Desktop')
# print(os.getcwd())

# os.chdir('/Users/kamalika/Desktop/python/lists')
# print(os.getcwd())



# os.mkdir('OS-demo')
# os.makedirs('OS-demo/3_sub')
# os.removedirs('OS-demo/3_sub')
# os.rmdirs('OS-demo/3_sub')
# os.rename('test.txt','demo.txt')

# print(os.stat('demo.txt').st_size)
# print(os.stat('demo.txt').st_mtime)


# mod_time = os.stat('demo.txt').st_mtime
# print(datetime.fromtimestap(mod_time))

# print(os.listdir())


#printing directories and files in the whole path
# for dirpath, dirname, filenames in os.walk('/Users/kamalika/Desktop'):
	# print (dirpath, dirname, filenames)

# print(os.environ.get('HOME'))

# file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
# print(file_path)

# with open(file_path, 'w') as f:
# 	f.write

print(os.path.basename('/tmp/test.txt'))
print(os.path.split('/tmp/test.txt'))
print(os.path.exists('/tmp/test.txt'))
print(os.path.isdir('/tmp/test.txt'))
print(os.path.isfile('/tmp/test.txt'))
print(os.path.splitext('/tmp/test.txt'))
print(dir(os.path))











