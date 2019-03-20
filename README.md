# hashcatUtils
A few scripts and things that will be useful with hashcat

## crossProductTextFiles.sh

An untested implementation of the cross product of two text files

## crossProductTextFiles.py crossProductTextFiles.sh

The python implementation uses for loops and a lot of memory for big files. The .sh version calls sed, which is much more efficient when you have huge files, but also slower for small files.

A working implementation of the cross product of two text files. Takes two files as input and produces text to standard out which can be piped to a file. For example, if file1 is
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

## talkEnglishTop1500Nouns.txt

A dictionary of the 1500 most commonly spoken English language nouns


## google-10000-{xyz}.txt

Dictionaries of subsets the most common 10k words found in google searches in the US. "2to5" means 2 to 5 characters in length. "-lt5" means less than 5 characters with no minimum.

## 4DigitNumbers.txt

All the 4-digit numbers including and excluding leading zeroes.

## makeUnique.sh

uses an awk associative array to remove duplicate lines from a file

## removeLongLines.sh

Removes all lines longer than (arg1)

## removeShortLines.sh

Removes all lines shorter than (arg1)
