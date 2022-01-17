#find and write to a xls file the matched domain terms from master file against a input file
import sys
import csv
import re
import pandas as pd
from argparse import ArgumentParser

parser = ArgumentParser(description='This script will align Subtitle translation files\n\r'+
						"How to Run?\n" +
						"python3 " + sys.argv[0] + " -i=input.txt" + " -m=master_list.csv -o=out.csv"
						)
parser.add_argument("-i", "--input", dest="inputfile",
					help="provide input file name",required=True)
parser.add_argument("-m", "--masterlist", dest="masterlistfile",
					help="provide list file in xlsx",required=True)
parser.add_argument("-o", "--output", dest="outfile",
					help="provide outputfilename",required=True)

args = parser.parse_args()

inputfile = args.inputfile
masterlistfile = args.masterlistfile
outfile = args.outfile

#open file using open file mode
fp1 = open(inputfile) # Open file on read mode -- input file
lines = fp1.read().split("\n") # Create a list containing all lines
fp1.close() # Close file

df = pd.read_csv(masterlistfile, sep='\t')
df1 = df

words = []
all_hash = {}
for index, row in df.iterrows():
	#words.append('#'.join(map(str,row[1:])))
	try:
		t1_word = str(row["Translation-T1"]).strip()
	except:
		t1_word = ''
	try:
		t2_word = str(row["Transliteration-T2"]).strip()
	except:
		t2_word = ''
	try:
		t3_word = str(row["English Source-T3"]).strip()
	except:
		t3_word = 'None'
	if t3_word in all_hash:
		val = all_hash[t3_word]
		if(t1_word != "" and t2_word != ""):
			all_hash[t3_word] = t1_word + "/" + val + "/" + t2_word
		elif(t1_word != ""):
			all_hash[t3_word] = t1_word + "/" + val
		elif(t2_word != ""):
			all_hash[t3_word] = val + "/" + t2_word
	else:
		all_hash[t3_word] = t1_word + "\t" + t2_word
	
	
i = 0
#out = []
keys = all_hash.keys()
kl = len(keys)-1
out_hash = {}
for key in keys:
	i = 0
	for line in lines:
		if(line != ""  and not re.search(r'\d\d:\d\d:\d\d,\d\d\d --> \d\d:\d\d:\d\d,\d\d\d', line) and not re.search(r'^\d+$', line)):
			#my_regex = key + r"\b"
			my_regex = r"(^|[,\"\'\( \/\|])" + key + r"([ ,\.!\"।\'\/\;\:)]|$)"
			if((re.search(my_regex, line, re.IGNORECASE|re.UNICODE))):
				out_hash[key] = all_hash[key]
			i = i + 1
#data = [['Translation-T1', 'Translation-T2', 'English Source-T3']]
data = [['Translation-T1', 'Transliteration-T2', 'English Source-T3']]
#file = open(outfile, 'w')
#writer = csv.writer(file, delimiter='\t')
#writer.writerow(data)

for o in out_hash:
	#print(o, out_hash[o])
	val = out_hash[o]
	vals = val.split("\t")
	arr = []
	arr.append(vals[0])
	arr.append(vals[1])
	arr.append(o)
	data.append(arr)
	#writer.writerow(data)
#print(data)
#exit(1)
df = pd.DataFrame(data=data, columns=['Translation-T1', 'Transliteration-T2', 'English Source-T3'])
#print(type(df))
#print(df)
df.to_excel('data.xlsx', sheet_name='sheet1', index=False, header=False)
