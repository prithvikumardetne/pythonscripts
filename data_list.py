data="""EEID	Full Name	Department	Gender	Ethnicity	Age
E02387	Emily	IT	Female	Black	55
E04105	Theodore	IT	Male	Asian	59
E02572	Luna	Finance	Female	Caucasian	50
E02832	Penelope	IT	Female	Caucasian	26
E01639	Austin	Finance	Male	Asian	55
E00644	Joshua Gupta	Sales	Male	Asian	57
E01550	Ruby Barnes	IT	Female	Caucasian	27
E04332	Luke Martin	Finance	Male	Black	25
E04533	Easton Bailey	Accounting	Male	Caucasian	29
E03838	Madeline Walker	Finance	Female	Caucasian	34
E00591	Savannah Ali	Human Resources	Female	Asian	36
"""

data_lines = data.split("\n")


data_tuples = [tuple(line.split("\t")) for line in data_lines]

print(data_tuples)      
