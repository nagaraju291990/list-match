#find and replace words from a tab seperated list into the input file
#how to run:? python3 t1_t2_t3_match_and_replace.py inputfile.txt list.txt(tab seperated)
import sys
import re
from collections import deque
from argparse import ArgumentParser

parser = ArgumentParser(description='This script will align Subtitle translation files\n\r'+
						"How to Run?\n" +
						"python3 " + sys.argv[0] + " -i=input.srt" + " -s=srctext.txt -t=target.txt"
						)
parser.add_argument("-i", "--input", dest="inputfile",
                    help="provide input file name",required=True)
parser.add_argument("-t", "--terms", dest="listfile",
                    help="provide list file in xlsx",required=True)
parser.add_argument("-l", "--lang", dest="lang",
                    help="provide lang=hin/tel",required=True)
parser.add_argument("-f", "--flag", dest="con_flag",
                    help="choose this option for consistency in lexical items -f=y",required=False)

args = parser.parse_args()

inputfile = args.inputfile
listfile = args.listfile
lang = args.lang
con_flag = args.con_flag

if(con_flag is None):
	con_flag = 'n'
else:
	con_flag = con_flag.lower()

#open file using open file mode
fp1 = open(inputfile) # Open file on read mode -- input file
lines = fp1.read().split("\n") # Create a list containing all lines
fp1.close() # Close file


fp2 = open(listfile) # Open file on read mode -- tab seperated list file
words = fp2.read().split("\n") # Create a list containing all lines
fp2.close() # Close file

six_word_hash = {}
five_word_hash = {}
four_word_hash = {}
three_word_hash = {}
two_word_hash = {}

word_hash = {}
all_hash = {}

for word in words:
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
for d in (six_word_hash, five_word_hash, four_word_hash, three_word_hash, two_word_hash, word_hash):
	all_hash.update(d)

#keys = word_hash.keys()
keys = all_hash.keys()
#for k in keys:
	#print(k, "\t",all_hash[k], sep='')
#exit()
#skeys = sorted(keys, key=lambda x:x.split(" "),reverse=True)
#print (skeys)
#lines = deque(lines)
k = 0
i = 0
kl = len(keys)-1

for key in keys:
	#print(key)
	i = 0
	for line in lines:
		#print(key,line)
		if(line != ""  and not re.search(r'\d\d:\d\d:\d\d,\d\d\d --> \d\d:\d\d:\d\d,\d\d\d', line) and not re.search(r'^\d+', line)):
			#print("iam",line)
			#my_regex = key + r"\b"
			my_regex = r"(^|[,\"\'\( \/\|])" + key + r"([ ,\.!\"।\'\/\;\:)]|$)"
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
							if(key == t1ss and con_flag == 'n'):
								t1 = key
					else:
						t1 = t1_slashes

					if(re.search(r'/', tgt_pipes[1])):
						t2 = tgt_pipes[1].split("/")[0]
						if(lang == "tel"):
							tt = tgt_pipes[1].split("/")
							for t in tt:
								if(t1 != ""):
									if(re.search(r''+t[-1], t1[-1] ) and t1 != ""):
										t2 = t
					else:
						t2 = tgt_pipes[1]
					t3 = tgt_pipes[2]
					final_t123 = "((" + t1 + "|" + t2 + "|" + t3 + "))"
				else :
					final_t123 = "((" + tgt +"))"

				final_t123 = re.sub(r' ', "replaced###already", final_t123, flags=re.IGNORECASE|re.MULTILINE)

				line = re.sub(my_regex, r"\1" + final_t123 +r"\2",line,flags=re.IGNORECASE|re.UNICODE|re.MULTILINE)
				#print("iam :1",line, key, all_hash[key])
			if((re.search(r"([,\"\'\( \/])" + key + r"$", line, re.IGNORECASE|re.UNICODE)) and 0 ):
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
					final_t123 = "((" + t1 + "|" + t2 + "|" + t3 + "))"
				else :
					final_t123 = "((" + tgt +"))"


				final_t123 = re.sub(r' ', "replaced###already", final_t123, flags=re.IGNORECASE|re.MULTILINE)
				line = re.sub(key+r"$", final_t123 ,line,flags=re.IGNORECASE|re.UNICODE|re.MULTILINE)

				#print("iam :2",line, key)
			if((re.search(r"^" + key + r"([ ,\.!\"।\'\/)])", line, re.IGNORECASE|re.UNICODE)) and 0):
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
					final_t123 = "((" + t1 + "|" + t2 + "|" + t3 + "))"
				else :
					final_t123 = "((" + tgt +"))"

				final_t123 = re.sub(r' ', "replaced###already", final_t123, flags=re.IGNORECASE|re.MULTILINE)
				line = re.sub(r"^" + key, final_t123, line,flags=re.IGNORECASE|re.UNICODE|re.MULTILINE)
				#print("iam3 :",line, key, key)
			if((re.search(r"^" + key + r"$", line, re.IGNORECASE|re.UNICODE)) and 0):
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
					final_t123 = "((" + t1 + "|" + t2 + "|" + t3 + "))"
					#print(final_t123)
				else :
					final_t123 = "((" + tgt +"))"

				final_t123 = re.sub(r' ', "replaced###already", final_t123, flags=re.IGNORECASE|re.MULTILINE)
				line = re.sub(r"^" + key + r"$", final_t123 ,line,flags=re.IGNORECASE|re.UNICODE|re.MULTILINE)
				#print("iam4 :",line, key)
			#line = re.sub(r'2replaced###already', "", line, flags=re.IGNORECASE|re.MULTILINE)
			#line = re.sub(r'replaced###already', " ", line, flags=re.IGNORECASE|re.MULTILINE)
			#line = re.sub(r"piped###already", "|", line, flags = re.IGNORECASE|re.MULTILINE)
			#print(line)
			lines[i] = line
		else:
			lines[i] = line

		i = i + 1
			#print(line)
for line in lines: #delete t1 if t1==t2
	line = re.sub(r'\((.*)?\|\1\|', r'(|\1|', line, flags=re.IGNORECASE|re.MULTILINE) #delete t1 if t1==t2
	line = re.sub(r'2replaced###already', "", line, flags=re.IGNORECASE|re.MULTILINE)
	line = re.sub(r'replaced###already', " ", line, flags=re.IGNORECASE|re.MULTILINE)
	print(line)