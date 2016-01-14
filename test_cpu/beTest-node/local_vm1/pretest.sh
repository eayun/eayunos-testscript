#!/bin/sh

for f in `ls`
do
   if [ -f "$f" ] && [ ${f: -3} == 'txt' ]
   then
      rm -rf $f
      echo 'remove:' $f
   fi
done
python test_cpu.py

