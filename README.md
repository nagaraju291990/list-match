# Genralized script to replace from list in a inpu file
## How to run?

```bash
python3 list_match.py inputfile.txt list.txt 
```

## list file format

```bash
Course	((पाठ्यक्रम|कोर्स|Course))
Food Microbiology	((खाद्य सूक्ष्मजीवविज्ञान|फूड माइक्रोबायोलॉजी|Food Microbiology))
Food Safety	((खाद्य सुरक्षा|फूड सेफ़्टी|Food Safety))
```


## To replace ((t1|t2|t3)) in text from input as either t1/t2/t3 as key

List can have many forms for t1 and t2.

Decision is that always first t2 will be used and t1 is replaced with the one matched in input

```bash
python3 t1_t2_t3_match_and_replace.py inputfile.txt list.txt 
```

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
