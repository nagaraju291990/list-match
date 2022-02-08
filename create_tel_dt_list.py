#make a xls sheet unique based on eng word and find the terms from parallel file of eng2tel
import sys
import csv
import re
import pandas as pd
from argparse import ArgumentParser

parser = ArgumentParser(description='This script will align Subtitle translation files\n\r'+
						"How to Run?\n" +
						"python3 " + sys.argv[0] + " -i=input.txt" + " -m=master_list.csv"
						)
parser.add_argument("-s", "--source", dest="srcfile",
					help="provide source file name",required=True)
parser.add_argument("-t", "--target", dest="tgtfile",
					help="provide target file name",required=True)
parser.add_argument("-m", "--masterlist", dest="masterlistfile",
					help="provide list file in xlsx",required=True)
#parser.add_argument("-o", "--output", dest="outfile",
#					help="provide outputfilename",required=True)

args = parser.parse_args()

srcfile = args.srcfile
tgtfile = args.tgtfile
masterlistfile = args.masterlistfile
#outfile = args.outfile
outfile = re.sub(r' ', '_', tgtfile)
outfile = re.sub(r'\.[a-z][a-z][a-z]', '_out.xlsx', outfile)

#open file using open file mode
fp1 = open(srcfile) # Open file on read mode -- input file
srclines = fp1.read().split("\n") # Create a list containing all lines
fp1.close() # Close file

#open file using open file mode
fp2 = open(tgtfile) # Open file on read mode -- input file
temp = fp2.read()#.split("\n") # Create a list containing all lines
temp = re.sub(r'$', '\n', temp)
temp = re.sub(r'\n\n$', '', temp)
tgtlines = temp.split("\n")
fp2.close() # Close file

#print(len(srclines), len(tgtlines))
if(len(srclines) != len(tgtlines)):
	print("Source and Target file lines mismatch..")
	exit()

col_names = ["Translation-T1", "Transliteration-T2", "English Source-T3"]
df = pd.read_excel(masterlistfile, names=col_names, na_filter=False)
df1 = df
#print(df)
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
	#print(key)
	i = 0
	for sline, tline in zip(srclines, tgtlines):
		if(sline != ""  and not re.search(r'\d\d:\d\d:\d\d,\d\d\d --> \d\d:\d\d:\d\d,\d\d\d', sline) and not re.search(r'^\d+$', sline)):
			#my_regex = "sss"
			my_regex = r"(^|[,\"\'\( \/\|])" + re.escape(key) + r"([ ,\.!\"।\'\/\;\:\)]|$)"
			#print(my_regex)
			if(re.search(my_regex, sline, re.IGNORECASE|re.UNICODE)):
				#print(my_regex, sline)
				terms = re.findall("(_.*?_)", tline)
				out_hash[key] = "/".join(terms) + "\t" + all_hash[key]
			i = i + 1
#data = [['Translation-T1', 'Translation-T2', 'English Source-T3']]
data = [['Transliteration-T2-Target-File','Translation-T1', 'Transliteration-T2-Sheet', 'English Source-T3']]
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
	arr.append(vals[2])
	arr.append(o)
	data.append(arr)
	#writer.writerow(data)
#print(data)
#exit(1)
df = pd.DataFrame(data=data, columns=['Transliteration-T2-Target-File', 'Translation-T1', 'Transliteration-T2-Sheet', 'English Source-T3'])
df = df.fillna('')
#print(type(df))
print(df)
df.to_excel(outfile, sheet_name='sheet1', index=False, header=False)
