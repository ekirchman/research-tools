import pandas as pd
import pyreadstat
import sys

filename = sys.argv[1]
file_ext = filename[-3:]
#df, meta = pyreadstat.read_por(filename)

if file_ext.lower() == "por":
    #print("por")
    df, meta = pyreadstat.read_por(filename, apply_value_formats=True, formats_as_category=True, formats_as_ordered_category=False)
elif file_ext.lower() == "sav":
    #print("sav")
    df, meta = pyreadstat.read_sav(filename, apply_value_formats=True, formats_as_category=True, formats_as_ordered_category=False)
else:
    print("Not a sav or a por file!")
    exit(1)
# done! let's see what we got
#print(df.head())
#print(meta.column_names)
#print(meta.column_labels)
#print(str(meta.column_names_to_labels))
#print(meta.number_rows)
#print(meta.number_columns)
#print(meta.file_label)
#print(meta.file_encoding)
# there are other metadata pieces extracted. See the documentation for more details.
#print(meta.value_labels)

#should set each cell to the label that is in metadata
#meta.variable_to_label
# You can replace the column names bassign column namesy column labels very easily (but check first that all columns have distinct labels!):
list = []
for key, value in meta.column_names_to_labels.items() :
    mystring = str(key) + ": " + str(value)
    list.append(mystring)

#print(list)
#df.columns = meta.column_names
df.columns = list

# print number of rows in df
print("Number of rows in df: ".format(len(df.index)))

#write to csv
df.to_csv("output_file.csv", index=False)

