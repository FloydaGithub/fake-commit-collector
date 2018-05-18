#!/bin/bash

year=$(date "+%Y")
date=$(date "+%Y-%m-%d")
time=$(date "+%T")
file_name=$year-collector.md

msg="$date $time"
echo $msg >> $file_name
echo $msg > current-msg.md

echo -e "Update $msg" > current-msg.md
msg="cat current-msg.md"
git add .
git commit -m "$($msg)"
git push github master
git push coding master

if [ $(uname) == "Darwin" ]
then
   say "Git is OK"
fi
