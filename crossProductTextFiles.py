from itertools import product
file1 = 'talkEnglishTop1500Nouns.txt'
file2 = 'numbers00To99.txt'
print('\n'.join((''.join(elt) 
	for elt in (product(*((line.strip() 
		for line in filehandle) 
			for filehandle in (open(file1,'r'), open(file2,'r'))))))))

