# hashcatUtils
A few scripts and things that will be useful with hashcat


## crossProductTextFiles.py

A workign implementation of the cross product of two text files. Takes two files as input and produces text to standard out which can be piped to a file. For example, if file1 is
```
apple
banana
```

and file2 is
```
car
truck
```

The output will be 
```
applecar
appletruck
bananacar
bananatruck
```

