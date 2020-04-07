#extract ((t1|t2|t3)) , [[t1|t2|t3]] from a file containing t1t2t3 terms into tab seperated file
#how to run:? python3 extract_term.py input.txt

import sys
import re

#open file using open file mode
fp1 = open(sys.argv[1]) # Open file on read mode -- input file
lines = fp1.read().split("\n") # Create a list containing all lines
fp1.close() # Close file

term_dict = {}

for line in lines:
	if(line == ""):
		continue
	line2 = line
	terms1 = re.findall("(\(\(.*?\)\))", line)
	for term in terms1:
		#term = re.escape(term)
		term = re.sub(r'\।', "|", term)	#replace danda with pipe
		term = re.sub(r' ?\(\( ?', "((", term)
		term = re.sub(r' ?\)\) ?', "))", term)
		term = re.sub(r' ?\| ?', "|", term)
		term = re.sub(r'^ *', "", term, flags = re.MULTILINE)
		line = re.sub(r' *$', "", term, flags = re.MULTILINE)
		term = re.sub(r' +', " ", term, flags = re.MULTILINE)

		tokens =  re.findall("\(\((.*)?\|(.*)?\|(.*)?\)\)", term)

		try:
			key = tokens[0][2].lower()
			meaning = tokens[0][0]
			trans = tokens[0][1]

			if(key in term_dict):
				tmp = term_dict[key]
				term_dict[key] = meaning + "/" + tmp
			else:
				term_dict[key] = meaning + "\t" + trans
		except:
			print("Invalid",term, sep="\t")
	terms2 = re.findall("(\[\[.*?\]\])", line2)
	#print(line,terms2)
	for term in terms2:
		#term = re.escape(term)
		term = re.sub(r'\।', "|", term)	#replace danda with pipe
		term = re.sub(r' ?\[\[ ?', "[[", term)
		term = re.sub(r' ?\]\] ?', "]]", term)
		term = re.sub(r' ?\| ?', "|", term)
		term = re.sub(r'^ *', "", term, flags = re.MULTILINE)
		line = re.sub(r' *$', "", term, flags = re.MULTILINE)
		term = re.sub(r' +', " ", term, flags = re.MULTILINE)

		tokens =  re.findall("\[\[(.*)?\|(.*)?\|(.*)?\]\]", term)

		try:
			key = tokens[0][2].lower()
			meaning = tokens[0][0]
			trans = tokens[0][1]

			if(key in term_dict):
				tmp = term_dict[key]
				term_dict[key] = meaning + "/" + tmp
			else:
				term_dict[key] = meaning + "\t" + trans
		except:
			print("Invalid",term,sep="\t")
		#print(term)

	#print(line)
for k in term_dict:
	val = term_dict[k]
	vals = val.split("\t")
	meanings = vals[0].split("/")
	meanings = list(set(meanings))
	unique_meanings = "/".join(meanings)
	print(k, unique_meanings, vals[1], sep="\t")