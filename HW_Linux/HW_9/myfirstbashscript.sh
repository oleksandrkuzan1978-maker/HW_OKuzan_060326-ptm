#!/bin/bash

USER="Sasha"

date +"%d-%m-%y"

echo "hello $USER!"
pwd

ps -ef | grep -v "bioset" | wc -l

ls -al /etc/passwd | awk '{ print $1 }'

