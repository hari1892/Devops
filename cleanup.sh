#!/bin/bash
#this script will do clean up files based on the retention policy

if [[ -z $1 || -z $2 ]]
then
echo "script usage:  $0 <Directoryname> <thesholdvalue>   , Ex:  $0 /home/harir 50"
exit
fi

filesdirectory=$1
thershold=$2

function deletefiles ()
    {   
        system_folders=( / /bin  /boot  /dev  /etc  /home  /lib /lib32 /lib64 /lost+found  /media  /mnt  /opt  /proc  /root  /run  /sbin  /srv  /sys  /tmp  /usr  /var )
        if [[ -z $filesdirectory || -z $thershold || $thershold != [0-9]* ]]
        then
        echo "Please specify path and thershold value as integer to delete files"
        exit
        elif [ -d $filesdirectory ]
        then
        echo "Validating input"
            for i in "${system_folders[@]}"
            do
                if [[ $filesdirectory == $i || $filesdirectory == $i/ ]]
                then
                system_linux_folders=`eval echo ${system_folders[@]}  | tr ' ' '\n'`
                echo -e "WARNING - you have selected $filesdirectory folder , you are not allowed to choose these system folders:\n$system_linux_folders"
                exit
                fi
            done
        echo "Files under $filesdirectory older than $thershold days will be deleted"
        find $filesdirectory -type f -iname '*.rar' -mtime +$thershold -exec ls -lh {} \;
#         find $filesdirectory -type f -iname '*.gz' -mtime +$thershold -exec mv -v {} /tmp \; 
         if [ $? != 0 ]
            then
            echo "old files deletion failed, please check"
            else
            echo "Files older than $thershold has been deleted successfully"
            fi
        else
        echo "there is no path as $filesdirectory in filesystem, please check"
        fi

    }
deletefiles
