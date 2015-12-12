import sys
import math
import fileinput 
import re 
import sys
from itertools import islice

def read_in_chunks(file_path, n):
    with open(file_path) as fh:
        while True:
            lines = list(islice(fh, n))
            if lines: yield lines
            else:     break


def array_compute(N,a):
	sum = 0
	for i in range(0,N):
		sum = sum + a[i]
	return sum 
    
def main():
	for lines in read_in_chunks(sys.argv[1], 2):
		N, array = lines[0], lines[1]
		array = array.split()
		N, array = int(N),  [int(i) for i in array]
		res = array_compute(N,array)
		print res
if __name__=="__main__":
    main()