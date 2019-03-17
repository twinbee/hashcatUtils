from itertools import product
import sys
file1 = sys.argv[1] 
file2 = sys.argv[2] 
print('\n'.join((''.join(elt) 
	for elt in (product(*((line.strip() 
		for line in filehandle) 
			for filehandle in (open(file1,'r'), open(file2,'r'))))))))

