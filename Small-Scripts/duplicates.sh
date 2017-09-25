#!/bin/bash
##################
DIR=$1
MD5=`find "$DIR" -type f -exec md5sum {} \; > /tmp/out`
MD5SUMS=(`cat /tmp/out|awk '{print $1}'|sort|uniq -d`)

for md5 in "${MD5SUMS[@]}"
   do
   FILES=(`grep $md5 /tmp/out|awk '{print $2}'`)
   echo -e "MD5SUM: $md5\n--------------------------------\n"
   for f in ${FILES[@]}
	do
	echo "$f"
  done
  echo -e "\n"
done
