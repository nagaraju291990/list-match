#This program validates the forms in the list file of form T3[TAB]T1|T2|T3
import re
import sys

with open(sys.argv[1], 'r', encoding='utf-8') as fp:
	lines = fp.read()

f = open('out.txt', 'w', encoding='utf-8')

line_no = 0
flag = 0
for line in lines.split("\n"):
	line_no += 1
	if(line == ""):
		continue
	#line = line.strip()

	try:
		line.split("\t")
	except:
		print("Tab not found at:%s" %(line_no) )

	col1_col2 = line.split("\t")
	#print(col1_col2)
	try:
		col1 = col1_col2[0]
	except:
		print("Invalid line at: %s" %(line_no) )
		col1 = "column1"
	try:
		col2 = col1_col2[1]
	except:
		print("Invalid line at: %s" %(line_no) )
		col2 = "column2"
	#col1 = col1_col2[0]
	#col1 = col1_col2[1]
	pipes = len(re.findall("\|", col2))
	#print(m, pipes)
	if(pipes == 2):
		tokens = re.findall("(.*)\|(.*)\|(.*)?", col2)
		#print("Line no:%s, tokens:%s" %(line_no,tokens))
		for i in tokens:
			if(i[1] == "" or i[2] == ""):
				print("Line no:%s token missing at:%s" %(line_no, col2))
				#f.write("Line no:%s Term missing at:%s\n" %(line_no, col2))
				flag = 1
			elif(re.search("[A-z]",i[0]) or re.search("[A-z]",i[1])):
				print("Line no:%s T1 or T2 has Roman text at:%s" %(line_no,
                    col2))
				#f.write("Line no:%s Term T1 or T2 has Roman text at:%s\n" %(line_no, col2))
				flag = 1
	else:
		#print("Line no:%s pipe count mismatch at :%s" %(line_no, m))
		if(pipes > 2):
			#f.write("Line no:%s Tokens are more than 3 :%s\n" %(line_no, col2))
			print("Line no:%s Tokens are more than 3 :%s" %(line_no, col2))
			flag = 1
		else:
			#f.write("Line no:%s Tokens are less than 3 :%s\n" %(line_no, col2))
			print("Line no:%s Tokens are less than 3 :%s" %(line_no, col2))
			flag = 1

if(flag == 0):
	#print("Input file passed all validation tests!")
	f.write("Input file passed all validation tests!")

