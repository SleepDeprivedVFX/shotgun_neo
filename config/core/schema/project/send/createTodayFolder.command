#!/bin/sh

#  janCreateTodayFolder.sh
#  
#
#  Created by Janimation on 1/18/16.
#
a=$(date "+%Y-%m-%d")
b=`dirname $0`
mkdir "$b/$a"

osascript -e 'tell application "Terminal" to close window 1' & exit 0