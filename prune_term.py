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
		continue
	line = re.sub(r'\[\[\|', '', line)
	#print("1",line)
	line = re.sub(r'\| ?[A-Za-z]+\]\]\|?', '', line)
	#print("2",line)
	terms = re.findall("(\(\(.*?\)\))", line)
	for term in terms:
		#print(term)
		#pipes = len(re.findall("\|", terms))
		tokens =  re.findall("\(\((.*)?\|(.*)?\|(.*)?\)\)", term)
		term = re.escape(term)
		#print(term)

		#print(tokens[0][0], tokens[0][1], sep="####")
		try:
			r = tokens[0][0]
			line = re.sub(rf''+term, tokens[0][1], line)
		except:
			try:
				tokens[0][1]
				line = re.sub(rf''+term, tokens[0][0], line)
			except:
				x = 0


		#if(tokens[0][0] == ""):
			#line = re.sub(rf''+term, tokens[0][1], line)
		#else:
			#line = re.sub(rf''+term, tokens[0][0], line)
	line = re.sub(r'\*?\|\*? ?[A-z]+\*? ?', '', line)
	line = re.sub(r'\(\(|\)\)|\[\[|\]\]', '', line)
	line = re.sub(r'\*', '', line)
	print(line)