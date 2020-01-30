#prune t1 or t2 from ((t1|t2|t3))
#how to run:? python3 prune_term.py

import sys
import re

#open file using open file mode
fp1 = open(sys.argv[1]) # Open file on read mode -- input file
lines = fp1.read().split("\n") # Create a list containing all lines
fp1.close() # Close file


for line in lines:
	if(line == ""):
		break
	terms = re.findall("(\(\(.*?\)\))", line)
	for term in terms:
		#print(term)
		#pipes = len(re.findall("\|", terms))
		tokens =  re.findall("\(\((.*)?\|(.*)?\|(.*)?\)\)", term)
		term = re.escape(term)
		#print(term)

		#print(tokens[0][0], tokens[0][1], sep="####")
		if(tokens[0][0] == ""):
			line = re.sub(rf''+term, tokens[0][1], line)
		else:
			line = re.sub(rf''+term, tokens[0][0], line)

	print(line)