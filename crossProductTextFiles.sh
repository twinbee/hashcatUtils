#!/bin/bash

while read line1
do
    sed "s/^/$line1, /" file2
done < file1