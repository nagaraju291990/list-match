#find and replace words from a tab seperated list into the input file
#how to run:? python3 t1_t2_t3_match_and_replace.py inputfile.txt list.txt(tab seperated)
import sys
import re
from collections import deque
import pandas as pd

#open file using open file mode
fp1 = open(sys.argv[1]) # Open file on read mode -- input file
lines = fp1.read().split("\n") # Create a list containing all lines
fp1.close() # Close file

outfp = open("list_hash.txt","w")

#fp2 = open(sys.argv[2]) # Open file on read mode -- tab seperated list file
#words = fp2.read().split("\n") # Create a list containing all lines
#fp2.close() # Close file

df = pd.read_excel(sys.argv[2])
df1 = df

words = []
for index, row in df.iterrows():
	words.append('#'.join(map(str,row[1:])))
	#for r in row[1:]:
		#print(r, end='#')
	#print("\n")
#print(words)
"""for row in df:
	for r in df[row]:
		print(r)"""

#data_dict = df.to_dict('series') 
"""#df = df.dropna()
data_dict = df.set_index(df.columns[2]).T.to_dict('list')

data_dict.update(df.set_index(df.columns[3]).T.to_dict('list'))
data_dict.update(df.set_index(df.columns[4]).T.to_dict('list'))
data_dict.update(df.set_index(df.columns[5]).T.to_dict('list'))
data_dict.update(df.set_index(df.columns[6]).T.to_dict('list'))

data_dict = {k: '#'.join(map(str, v))  for k,v in data_dict.items()}
#data_dict = df.to_dict('list')
print(data_dict)"""

#with open(sys.argv[2], mode="rU") as infile:
	#reader = csv.reader(infile)  
	#words = list(reader)
	#for row in reader:
		#print(row)
#exit()
six_word_hash = {}
five_word_hash = {}
four_word_hash = {}
three_word_hash = {}
two_word_hash = {}

word_hash = {}
all_hash = {}

for word in words:
	word = re.sub(r'#', '\t', word, 1)
	word = re.sub(r'#', "|", word, 1)
	word = re.sub(r'#', '/', word)
	word = re.sub(r'/nan', "", word)
	word = re.sub(r'nan', "", word)
	#print(word)
	word = re.sub(r'(.*)\t(.*)\|(.*)', r"\1\t\3|\2|\1", word)
	word = re.sub(r'\t/', "\t", word)
	#print(word)
	#word = word.lower()
	if(word != ""):
		t1t2t3 = word.split("\t")[1]	#contians(((T1|T2|T3)))
		t123 = t1t2t3
		t123 = re.sub(r'\(\(|\)\)', '', t123)
		#print(t123)
		tsl = t123.split("|")
		for terms in tsl:
			if(terms == ""):
				terms = "NO###T1###ForThisTeRm###"
			if(re.search(r'/',terms)):
				variant_terms = terms.split("/")
				for vt in variant_terms:
					if(len(re.findall(" ", vt)) == 5 ):
						six_word_hash[terms] = t1t2t3
					elif(len(re.findall(" ", vt)) == 4 ):
						five_word_hash[vt] = t1t2t3
					elif(len(re.findall(" ", vt)) == 3 ):
						four_word_hash[vt] = t1t2t3
					elif(len(re.findall(" ", vt)) == 2 ):
						three_word_hash[vt] = t1t2t3
					elif(len(re.findall(" ", vt)) == 1 ):
						two_word_hash[vt] = t1t2t3
					else:
						word_hash[vt] = t1t2t3
			else:
			#print(terms)
				if(len(re.findall(" ", terms)) == 5 ):
					six_word_hash[terms] = t1t2t3
				elif(len(re.findall(" ", terms)) == 4 ):
					five_word_hash[terms] = t1t2t3
				elif(len(re.findall(" ", terms)) == 3 ):
					four_word_hash[terms] = t1t2t3
				elif(len(re.findall(" ", terms)) == 2 ):
					three_word_hash[terms] = t1t2t3
				elif(len(re.findall(" ", terms)) == 1 ):
					two_word_hash[terms] = t1t2t3
				else:
					word_hash[terms] = t1t2t3

#print(word_hash)
#exit()
for d in (six_word_hash, five_word_hash, four_word_hash, three_word_hash, two_word_hash, word_hash):
	all_hash.update(d)

#keys = word_hash.keys()
keys = all_hash.keys()
for k in keys:
	#print(k, "\t",all_hash[k], sep='')
	outfp.write(k + "\t" + all_hash[k] + "\n")
#skeys = sorted(keys, key=lambda x:x.split(" "),reverse=True)
#print (skeys)
#lines = deque(lines)
#exit()
k = 0
i = 0
#out = []
kl = len(keys)-1
for key in keys:
	i = 0
	#key = re.escape(key)	
	for line in lines:
		if(line != ""  and not re.search(r'\d\d:\d\d:\d\d,\d\d\d --> \d\d:\d\d:\d\d,\d\d\d', line) and not re.search(r'^\d+$', line)):
			#my_regex = key + r"\b"
			my_regex = r"([,\"\'\( \/\|])" + key + r"([ ,\.!\"।\'\/)])"
			#print(my_regex)
			if((re.search(my_regex, line, re.IGNORECASE|re.UNICODE))):
				tgt = all_hash[key] + "2replaced###already"

				#tgt = re.sub(r'\|',"piped###already", tgt, flags = re.IGNORECASE|re.MULTILINE)
				if(re.search(r'/', tgt)):
					tgt_pipes = tgt.split("|")
					t1_slashes = tgt_pipes[0]
					t1 = t1_slashes

					if(re.search(r'/', t1_slashes)):
						t1s = t1_slashes.split("/")
						t1 = t1s[0]
						for t1ss in t1s:
							if(key == t1ss):
								t1 = key
					else:
						t1 = t1_slashes	

					if(re.search(r'/', tgt_pipes[1])):
						t2 = tgt_pipes[1].split("/")[0]
					else:
						t2 = tgt_pipes[1]
					t3 = tgt_pipes[2]
					#final_t123 = "((" + t1 + "|" + t2 + "|" + t3 + "))"
					final_t123 = ''.join(["((" , t1 , "|" , t2 , "|" , t3 , "))"])
				else :
					#final_t123 = "((" + tgt +"))"
					final_t123 = ''.join(["((" , tgt , "))"])
				
				final_t123 = re.sub(r' ', "replaced###already", final_t123, flags=re.IGNORECASE|re.MULTILINE)

				line = re.sub(my_regex, r"\1" + final_t123 +r"\2",line,flags=re.IGNORECASE|re.UNICODE|re.MULTILINE)
				#print("iam :1",line, key, all_hash[key])
			if((re.search(r"([,\"\'\( \/])" + key + r"$", line, re.IGNORECASE|re.UNICODE))):
				tgt = all_hash[key] + "2replaced###already"
				#tgt = re.sub(r' ', "replaced###already", tgt, flags=re.IGNORECASE|re.MULTILINE)
				#tgt = re.sub(r'\|',"piped###already", tgt, flags = re.IGNORECASE|re.MULTILINE)
				if(re.search(r'/', tgt)):
					tgt_pipes = tgt.split("|")
					t1_slashes = tgt_pipes[0]
					t1 = t1_slashes
					if(re.search(r'/', t1_slashes)):
						t1s = t1_slashes.split("/")
						t1 = t1s[0]
						for t1ss in t1s:
							if(key == t1ss):
								t1 = key
					else:
						t1 = t1_slashes	

					if(re.search(r'/', tgt_pipes[1])):
						t2 = tgt_pipes[1].split("/")[0]
					else:
						t2 = tgt_pipes[1]
					t3 = tgt_pipes[2]
					#final_t123 = "((" + t1 + "|" + t2 + "|" + t3 + "))"
					final_t123 = ''.join(["((" , t1 , "|" , t2 , "|" , t3 , "))"])
				else :
					#final_t123 = "((" + tgt +"))"
					final_t123 = ''.join(["((" , tgt , "))"])


				final_t123 = re.sub(r' ', "replaced###already", final_t123, flags=re.IGNORECASE|re.MULTILINE)
				line = re.sub(key+r"$", final_t123 ,line,flags=re.IGNORECASE|re.UNICODE|re.MULTILINE)

				#print("iam :2",line, key)
			if((re.search(r"^" + key + r"([ ,\.!\"।\'\/)])", line, re.IGNORECASE|re.UNICODE))):
				tgt = all_hash[key]+ "2replaced###already"
				#tgt = re.sub(r' ', "replaced###already", tgt, flags=re.IGNORECASE|re.MULTILINE)
				#tgt = re.sub(r'\|',"piped###already", tgt, flags = re.IGNORECASE|re.MULTILINE)
				if(re.search(r'/', tgt)):
					tgt_pipes = tgt.split("|")
					t1_slashes = tgt_pipes[0]
					t1 = t1_slashes

					if(re.search(r'/', t1_slashes)):
						t1s = t1_slashes.split("/")
						t1 = t1s[0]
						for t1ss in t1s:
							if(key == t1ss):
								t1 = key
					else:
						t1 = t1_slashes	

					if(re.search(r'/',  tgt_pipes[1])):
						t2 = tgt_pipes[1].split("/")[0]
					else:
						t2 = tgt_pipes[1]

					t3 = tgt_pipes[2]
					#final_t123 = "((" + t1 + "|" + t2 + "|" + t3 + "))"
					final_t123 = ''.join(["((" , t1 , "|" , t2 , "|" , t3 , "))"])
				else :
					#final_t123 = "((" + tgt +"))"
					final_t123 = ''.join(["((" , tgt , "))"])

				final_t123 = re.sub(r' ', "replaced###already", final_t123, flags=re.IGNORECASE|re.MULTILINE)
				line = re.sub(r"^" + key, final_t123, line,flags=re.IGNORECASE|re.UNICODE|re.MULTILINE)
				#print("iam3 :",line, key, key)
			if((re.search(r"^" + key + r"$", line, re.IGNORECASE|re.UNICODE))):
				#print(line)
				tgt = all_hash[key]+ "2replaced###already"
				#tgt = re.sub(r' ', "replaced###already", tgt, flags=re.IGNORECASE|re.MULTILINE)
				#tgt = re.sub(r'\|',"piped###already", tgt, flags = re.IGNORECASE|re.MULTILINE)
				if(re.search(r'/', tgt)):
					tgt_pipes = tgt.split("|")
					t1_slashes = tgt_pipes[0]
					t1 = t1_slashes

					if(re.search(r'/', t1_slashes)):
						t1s = t1_slashes.split("/")
						t1 = t1s[0]
						for t1ss in t1s:
							if(key == t1ss):
								t1 = key
					else:
						t1 = t1_slashes	

					if(re.search(r'/',  tgt_pipes[1])):
						t2 = tgt_pipes[1].split("/")[0]
					else:
						t2 = tgt_pipes[1]

					t3 = tgt_pipes[2]
					#final_t123 = "((" + t1 + "|" + t2 + "|" + t3 + "))"
					final_t123 = ''.join(["((" , t1 , "|" , t2 , "|" , t3 , "))"])
					#print(final_t123)
				else :
					#	final_t123 = "((" + tgt +"))"
					final_t123 = ''.join(["((" , tgt , "))"])

				final_t123 = re.sub(r' ', "replaced###already", final_t123, flags=re.IGNORECASE|re.MULTILINE)
				line = re.sub(r"^" + key + r"$", final_t123 ,line,flags=re.IGNORECASE|re.UNICODE|re.MULTILINE)
				#print("iam4 :",line, key)
			#line = re.sub(r'2replaced###already', "", line, flags=re.IGNORECASE|re.MULTILINE)
			#line = re.sub(r'replaced###already', " ", line, flags=re.IGNORECASE|re.MULTILINE)
			lines[i] = line
		else:
			lines[i] = line

		i = i + 1
		#print(line, key)
		#if(kl == i):
			#print(line)
		#line = re.sub(r"piped###already", "|", line, flags = re.IGNORECASE|re.MULTILINE)
	
	#print(i, kl)
	
	
	#else:
	#print(line)
for line in lines:
	line = re.sub(r'2replaced###already', "", line, flags=re.IGNORECASE|re.MULTILINE)
	line = re.sub(r'replaced###already', " ", line, flags=re.IGNORECASE|re.MULTILINE)
	print(line)