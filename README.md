# Genralized script to replace from list in a input file
## How to run?

```bash
python3 list_match.py input.txt list.txt 
```

## list file format

```bash
Course	((पाठ्यक्रम|कोर्स|Course))
Food Microbiology	((खाद्य सूक्ष्मजीवविज्ञान|फूड माइक्रोबायोलॉजी|Food Microbiology))
Food Safety	((खाद्य सुरक्षा|फूड सेफ़्टी|Food Safety))
```

## To replace as _t2_ in text from input as either t1/t2/t3 as key

List can have many forms for t1 and t2.

Decision is that always first t2 will be used

```bash
python3 domain_term_substitution.py -i=input.txt -t=list.xlsx -l=hin/tel -f=y/n
-f (consistency flag for lexical items is optional default is n)
```

## To replace ((t1|t2|t3)) in text from input as either t1/t2/t3 as key

List can have many forms for t1 and t2.

Decision is that always first t2 will be used and t1 is replaced with the one matched in input

```bash
python3 t1_t2_t3_match_and_replace.py -i=input.txt -t=list.txt -l=hin/tel -f=y/n
-f (consistency flag for lexical items is optional default is n)
```

## To replace ((t1|t2|t3)) in text from input as either t1/t2/t3 as key from xlsx file 
```
python3 t1_t2_t3_match_and_replace-xls.py -t=/home/nagaraju/Downloads/termbase-for-terminology-automation-3.1.xlsx -i=FMFS_Transcription_Module_39_eng_hin-reviewed.txt -l=hin/tel -f=y/n
```
-f (consistency flag for lexical items is optional default is n)
## list file format
```bash
microorganisms	सूक्ष्मजीव|माइक्रोऑर्गनिज़म/माईक्रोऑर्गनिज़म/माइक्रोऑर्गनिजम|microorganisms
contaminate	दूषित|कन्टेमनेट/कंटेमनेट|contaminate
food microbiology	सूक्ष्म जीवविज्ञान|फूड माइक्रोबायोलॉजी/फूड माइक्रोबायलॉजी|food microbiology
food safety	खाद्य सुरक्षा|फूड सेफ़्टी/फूड सेफ्टी|food safety
genera	|जीनस|genera
concept	अवधारणा|कान्सेप्ट/कन्सेप्ट|concept
microbiological risks	सूक्ष्मजैविक खतरों/सूक्ष्मजैविक खतरा/सूक्ष्मजैविक खतरे|माइक्रोबायोलॉजिकल रिस्क्स|microbiological risks
UPSC	संघ लोक सेवा आयोग|यूपीएससी|UPSC
MOOC	मूक|एमओओसी|MOOC
```
## To tag Accronyms

```
python3 mark_accr.py accr_list.txt accr_input.txt > accr_marked_out.txt
```

## To replace ((t1|t2|t3)) in text with either t1/t2 i.e prune terms of format (t1|t2|t3)) to t1 or t2
```bash
python3 prune_term.py input.txt > prune_out.txt
```

## To extract ((t1|t2|t3)) or [[t1|t2|t3]] in text and get a tab seperated file in term format
```bash
python3 extract_term.py input.txt > extract_out.txt
```

## To validate term list file of form t1[TAB]((t1|t2|t3)) 
```bash
python3 term-list-validator.py input.txt 
```

## To convert tab seperated file into t1[TAB]((t1|t2|t3)) format
```bash
python3 make_terms.py input.txt 
```

## To extract ((t1|t2|t3)) or [[t1|t2|t3]] in text and get a tab seperated file into tab seperated meaning and transliteration format
```bash
python3 extract_term_from_marked_list.py term_marked_input.txt > extract_out.txt
```

## Run shell with input and output directory
```bash
sh run_shell.sh input/ termbase-for-terminology-automation-3.4.xlsx output
```

## create terms from master file against input text file
```bash
python3 create_dt_list.py --i=/home/nagaraju/Downloads/10-DL\ C1\ W4\ SV_eng_eng_mar-source.txt --m=/home/nagaraju/Downloads/Digital_Library_Domain_Terms.csv
```
