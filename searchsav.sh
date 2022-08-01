#!/bin/bash

if [[ -z $1 ]];
then 
    echo "enter search param"
else
    #gfind ./thearda*/* -depth -iname "*.sav" -exec python3 combined.py $1 {} \;
    gfind . -depth -iname "*.sav" -exec python3 ~/bin/search_spss_contents.py $1 {} \;
    gfind . -depth -iname "*.por" -exec python3 ~/bin/search_spss_contents.py $1 {} \;
fi
