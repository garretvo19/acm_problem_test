import fileinput 
import sys 
import re
testinput = sys
#while testinput:
#	in1 = sys.argv[1]
#	print in1 

for line in fileinput.input():
	a = line
	a = str.strip(a)
	nums = re.split('\s',a)  
	nums_list = [int(num) for num in nums]
	print nums_list 
#a = sys.argv[1:]
#print a 