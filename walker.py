
import os
import sys


if len(sys.argv) != 2:
     exit('usage: %s <dir to walk>' % sys.argv[0])
	
try:
   
	directory = sys.argv[1]
	os.chdir(directory)
	count = 0

	for r,s,f in os.walk("."):
		for files in f:
			remote_path = "%s/%s" % (r,files)
			if remote_path.startswith("."):
			   remote_path = remote_path[1:]
			print directory+remote_path
		        count += 1
		        dirs = open('walker.txt','a')
		        dirs.write(directory+remote_path+'\n')
	print('There are %s files inside '+directory) % count
	print"I've saved the dirs and file names in %s/walker.txt" % directory

except:
   
        print'\n[!]Something went wrong\n[!]Please check if %s exists' % directory
