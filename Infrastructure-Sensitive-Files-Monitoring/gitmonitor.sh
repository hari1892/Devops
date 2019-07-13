#!/bin/bash
cd /
modified_files=`git status  | grep "modified" | cut -d ':' -f2 | sed 's/\s//g' | tr '\n' ' '`

while [ "`echo "$modified_files"`"  != "" ]
do
git add $modified_files
git commit -m "Change detected, pushing" && echo "git commit success"
git push -u origin master && echo "git files pushed"
done


