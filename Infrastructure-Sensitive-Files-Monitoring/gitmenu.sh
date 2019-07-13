#!/bin/bash
cd /
#scriptname=`realpath "$0"`
#cd `dirname $scriptname` 
#prefix=$(dirname $scriptname)
array=$(for i in `git ls-files | tr '\n' ' '`;do echo ""$prefix""/$i""; done)
#array+=( $(for i in `git ls-files | tr '\n' ' '`;do echo ""$prefix""/$i""; done) )


default ()
{
loop=0
while [ $loop -eq 0 ]
do
echo "Invalid input, please enter correct input"
inputfunction
done
}

gitls ()
{
cd /
#scriptname=`realpath "$0"`
#prefix=$(dirname $scriptname)
array1=$(for i in `git ls-files | tr '\n' ' '`
do
echo  ""$prefix""/$i""; done)
echo $array1 |  tr ' ' '\n'

}

gitlist_modified ()
{
echo $array | tr ' ' '\n' | grep -w $(git status | grep -w 'modified' | cut -d ':' -f2) 2> /dev/null
if [ $? != 0 ]
then
printf "No Files Modified\n"
fi
}

gitdiffrence ()
{

echo $array | tr ' ' '\n' | grep -w $(git status | grep -w 'modified' | cut -d ':' -f2) 2> /dev/null
if [ $? != 0 ]
then
echo "No Changes made to show the diffrence"
else
original_content=`git diff | sed -n '/\@.*/,/^+/p' | sed 's/^+.*//;s/@.*//g' | grep -v "^$"`
newly_appended=`git diff  | grep "^+[^+].*"`
echo "<---------------Original Content----------------------->"
echo "$original_content"
echo "<--------------recently updated changes---------------->"
echo "$newly_appended"
fi
}

newline ()
{
printf "\n\n"
}


pushfile ()
{
echo "Absolute path of modified file: "
newline
echo $array | tr ' ' '\n' | grep -w $(git status | grep -w 'modified' | cut -d ':' -f2) 2> /dev/null
if [ $? != 0 ] 
then
echo "No changes to Push"
else
#while [ "x$filepath"  ==  "x"  ] ||  [  "x$comment"  ==  "x" ]
while [ -z "$filepath" ] || [ -z "$comment" ]

do 
    read -p "Enter absolute path of the file to push the changes: " filepath
    read -p "Enter comment" comment

git add $filepath
git commit -m "$comment" || echo "git commit Failed"
git push -u origin master || echo "git push failed";exit

done 
fi
}




inputfunction ()
{
printf "\n\n"
count=1
echo "Sensitive Files Backup Menu---------------------->"
IFS=','
for i in $(echo List Files from Repository,List the modified Files,Print the data diffrence,Push the Updated File to Master,exit)
do
echo "$count) $i"
count=$(($count+1))
done;unset IFS

newline
read -p "Enter option: " input
newline

case $input in 
    
    1) gitls && inputfunction;newline
      ;;
    2) gitlist_modified && inputfunction;newline
      ;;
    3) gitdiffrence && inputfunction;newline
      ;;
    4) pushfile && inputfunction;newline
      ;;
    5) exit && newline
      ;;
    *) default && inputfunction;newline
      ;;
esac
newline
}

inputfunction
