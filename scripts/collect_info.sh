#!/bin/zsh

mkdir -p metadata/abstracts
for i in ../../Easychair/Final_VOLUME_ProceedingsIPMU2020/Final_VOLUME/1237????/README_EASYCHAIR; do 
    cp $i metadata/easychair/${i:h:t}.txt
    istex=$(cat $i | grep "Command to create document:" | wc -l )
    if [ $istex -eq 1 ]; then
       texname=$(cat $i | grep "Command to create document:" | awk '{print $NF}')
       if [ $(cat ${i:h}/$texname | grep "begin{abstract}" | wc -l) -ne 1 ]; then
          echo "Warning: abstract may not be ok in ${i:h}/$texname"
       fi
       cat ${i:h}/$texname | ./scripts/tex2meta.py > metadata/abstracts/${i:h:t}.tex
       if [ $? -ne 0 ]; then
            echo "${i:h} $nfiles Error"
       fi
    else
        echo "${i:h} is not latex"
    fi
done

grep "Microsoft Word file" metadata/*.easychair
