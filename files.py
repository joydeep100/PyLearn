from os import listdir
from os.path import isfile, join

mypath='./test_data'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print(onlyfiles)

# with open automatically ensures to close the file
# but still try closing it in the most optimum step
with open(join(mypath,'sample.txt'),'r',encoding='utf-8') as f:
	# possible modes :: 'r', 'w'
	
	print(f.readlines())
	# reading
	# .read(size=-1)	This reads from the file based on the number of size bytes. If no argument is passed or None or -1 is passed, then the entire file is read.
	# .readline(size=-1)	This reads at most size number of characters from the line. This continues to the end of the line and then wraps back around. If no argument is passed or None or -1 is passed, then the entire line (or rest of the line) is read.
	# .readlines()	This reads the remaining lines from the file object and returns them as a list.
	
	f.close()

	#writing
	# .write(string)	This writes the string to the file.
	# .writelines(seq)	This writes the sequence to the file. No line endings are appended to each sequence item. It’s up to you to add the appropriate line ending(s).

with open(join(mypath,'sample_write.txt'),'w') as f:
	f.write('hi\nhello\n')
	# f.writelines(['hi\n','hello'])