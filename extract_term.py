#extract ((t1|t2|t3)) , [[t1|t2|t3]] from a file containing t1t2t3 terms
#how to run:? python3 extract_term.py input.txt

import sys
import re

#open file using open file mode
fp1 = open(sys.argv[1]) # Open file on read mode -- input file
lines = fp1.read().split("\n") # Create a list containing all lines
fp1.close() # Close file


for line in lines:
	if(line == ""):
		break
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
			#tokens[0][2]
			print(tokens[0][2].lower(),term, sep="\t")
		except:
			print("Invalid",term, sep="\t")
	terms2 = re.findall("(\[\[.*?\]\])", line)
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
			#tokens[0][2]
			print(tokens[0][2].lower(),term, sep="\t")
		except:
			print("Invalid",term,sep="\t")
		#print(term)

	#print(line)