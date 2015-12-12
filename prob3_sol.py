import sys
import math
import fileinput 
import re 
def main():
	for line in fileinput.input():
		a = line
		a = str.strip(a)
		array_num = re.split('\s',a)  
		array_num_true = [int(num) for num in array_num]
		for i in range(0,len(array_num)):
			num = array_num_true[i]
			if num < 0:
				print 'error'
			else:
				count_holy = 0; 
				for i in xrange(0,num):
					last_num = i % 10  # obtain the last numbera
					if last_num == 3:
						count_holy = count_holy + 1
						# convert the number with the final digit = 3 to a list for manipulation
						lst_num = [int(j) for j in str(i)]
						for k in range(0,len(lst_num)):
							if lst_num[k] == 5:
								count_holy = count_holy-1
							if (lst_num[k-1] == 2 and lst_num[k] !=3):
								count_holy= count_holy -1  
							if (lst_num[k-1] == 3 and lst_num[k] ==4):
								count_holy = count_holy - 1 
		print count_holy 
						
						
if __name__=="__main__":	
	main() 