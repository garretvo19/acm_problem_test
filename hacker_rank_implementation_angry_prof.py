import sys 
from itertools import islice

def read_in_chunks(file_path, n):
    with open(file_path) as fh:
        while True:
            lines = list(islice(fh, n))
            if lines: yield lines
            else:     break

def main():
	for lines in read_in_chunks(sys.argv[1], 3):
		t = lines[0]
		array = lines[1] 
		#-----enter N and K 
		array = array.split()
		N,K = array[0], array[1]
		N,K = int(N), int(K)
		#-----enter the array number a
		a = lines[2]
		a = a.split() 
		a = [int(i) for i in a] 
		#-----now do some condition 
		count = 0 
		for j in a:
			if (j<0) or (j==0):
				count = count + 1
		if (count < K):
			print "YES"
		else:
			print "NO" 
if __name__=="__main__":
    main()