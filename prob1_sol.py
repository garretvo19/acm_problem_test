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
		# convert all of them into integer 
		#results_num =int(results)
		#number1_num = int(number1)
		#number2_num = int(number2)
		# create an array with these three numbers 
		#array_num = [results,number1, number2]
		#array_num_true = [results_num, number1_num, number2_num]
		# check to see whether the result is correct 	
		if (array_num_true[0] == (array_num_true[1]+array_num_true[2])):
			# check addition 
			print 'Carry on.'
		elif (array_num_true[0] == abs(array_num_true[1]-array_num_true[2])):
			# check subtraction
			print 'Carry on.'
		elif array_num_true[0] == (array_num_true[1]*array_num_true[2]):
			# check multiplication
			print 'Carry on.'
		elif (array_num_true[0] == (array_num_true[1]/array_num_true[2])): 
			# check division one side
			print 'Carry on.'
		elif (array_num_true[0] == (array_num_true[2]/array_num_true[1])): 
			# check the otherside division
			print 'Carry on.'
		elif (array_num_true[0] == array_num_true[1]%array_num_true[2]):
			# check the other modular 
			print 'Carry on.'
		elif (array_num_true[0] == array_num_true[2]%array_num_true[1]):
			# check the other side modular
			print 'Carry on.'
		else:
			for i in xrange(0,len(array_num)):
				number_str = array_num[i]
				l_num = len(number_str)
				if number_str[l_num-1] == '5':
					print 'Three, Sir!'
		
	#for i in range(0,len(operation_array)):
	#	print operation_array[i]
if __name__=="__main__":
	main() 