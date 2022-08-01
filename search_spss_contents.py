#!/opt/homebrew/bin/python3
import sys
import pyreadstat
# import pandas module 
import pandas as pd
import numpy as np
import re
import os
filename = sys.argv[2]
search_term = sys.argv[1]
search_term = search_term.lower()
file_ext = filename[-3:]

if file_ext.lower() == "por":
    try: 
        #many por files are corrupt/don't open, even in pspp                                                                                                                                                                                                                               
        df, meta = pyreadstat.read_por(filename.lstrip(), apply_value_formats=True, formats_as_category=True, formats_as_ordered_category=False)
        exit(1)
    except OSError as error:                                                                                                                                                                                                            
        print(error)
        print(filename)                                                                                                                                                                                                                   
elif file_ext.lower() == "sav":
    #print("sav")
    try:                                                                                                                                                                                                                                
        df, meta = pyreadstat.read_sav(filename.lstrip(), apply_value_formats=True, formats_as_category=True, formats_as_ordered_category=False)
    except OSError as error:                                                                                                                                                                                                            
        print(error)
        print(filename)
else:
    print("Not a sav or a por file!")
    exit()


# output the dataframe
#print(df)
#Print the file name
print(filename)

df.columns = meta.column_labels

#contain_values = df[df.eq("nuclear").any(1)]
#print (type(contain_values))

for col in df.columns:
    #df = df.filter(df[col].contains("nuclear"))
    #df['col'].str.contains(search_term, case=True, flags=0, na=None, regex=false)
    #print(col)
    #search_term_boundary = "\b" + search_term.lower() + "\b"
    if isinstance(col, type(None)): 
        pass
    else:
        if type(search_term) is not None:
            if re.search(search_term.lower(), col.lower()):
                print(col)
