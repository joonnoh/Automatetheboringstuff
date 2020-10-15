#!/bin/bash

# backupStuff.sh: Bash script backup tool for directory
# Create cron job to run script automatically

#Directory to be backed up
BACKUP_PATH="/Users/joonn/Scripts/remote/Automatetheboringstuff/"

#Directory to save the new backup
SAVE_PATH="/Users/joonn/backupStuff/"

DATE=`date +%d%m%Y`
BACKUP="backup_"
EXT=".tar"

#File name of new backup
FILE_NAME=$SAVE_PATH$BACKUP$DATE$EXT

echo "Backing up $BACKUP_PATH to $SAVE_PATH"
echo "...."

#Verbosely create archive and compress directory
tar -cvzf $FILE_NAME $BACKUP_PATH

#Check if file name exists and append message to log file
if test -f "$FILE_NAME"; then
	echo "Backup successful on" $DATE
	echo "Backup successful on" $DATE >> $SAVE_PATH/backupStuff.log
else
	echo "Problem with backup on" $DATE
	echo "Problem with backup on" $DATE >> $SAVE_PATH/backupStuff.log
fi

# Create cron job with crontab -e
# 0 7 * * * /path/to/script
