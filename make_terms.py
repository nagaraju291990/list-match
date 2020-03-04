#make ((t1|t2|t3)) from a tab seperated file containing source tab meaning tab transliteration
#how to run:? python3 make_terms.py input.txt

import sys
import re

#open file using open file mode
fp1 = open(sys.argv[1]) # Open file on read mode -- input file
lines = fp1.read().split("\n") # Create a list containing all lines
fp1.close() # Close file


terms_hash = {}
for line in lines:
	if(line == ""):
		continue

	words = line.split("\t")
	src = words[1]
	meaning = words[3:-1]
	meaning = '/'.join([str(elem) for elem in meaning if elem])
	transliteration = words[2]
	if(src.lower() in terms_hash):
		tmp = terms_hash[src]
		tmp = re.sub(r'\(\(', '', tmp)
		tmp = re.sub(r'\)\)', '', tmp)
		pipes = tmp.split("|")
		nmeaning = pipes[0] + "/" + meaning
		ntransliteration = pipes[1] + "/" + transliteration
		terms_hash[src.lower()] = nmeaning + "|" + ntransliteration + "|" + src
	else:
		terms_hash[src.lower()] = meaning + "|" + transliteration + "|" + src


for key in terms_hash:
	print(key, terms_hash[key], sep="\t")
