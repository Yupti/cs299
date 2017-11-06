import random
import string

def main(): # to call keyGen and substitution encrypt

    print("TEST 1")
    substitutionEncrypt("", "face")
    substitutionEncrypt("", "blow")

    print("TEST 2")
    substitutionEncrypt(keyGen(), "face")
    substitutionEncrypt(keyGen(), "blow")

    print("TEST 3")
    substitutionEncrypt("", "wonderful", "python", "java", "doedlugvusu")

    print("TEST 4")
    substitutionEncrypt(keyGen(), "wonderful", "python", "java", "doedlugvusu")
    

def substitutionEncrypt(key, *args): # for converting word into code word, done
    newWord = ""
    if key == "":
        key = "bpzhgocvjdqswkimlutneryaxf" # default key
    print("Key: ", key + "\n")
    for word in args:
        for i in word:
            newWord += key[(ord(i) - 97)] # converts letter in word with a letter in key
        print("Word: ", word, " Code Word: ", newWord, "\n")
        newWord = ""

def keyGen(): # for random key generator
    defaultKey = "bpzhgocvjdqswkimlutneryaxf"
    randomizedKey = ''.join(random.sample(defaultKey,len(defaultKey))) # randomizes the default key
    if defaultKey == randomizedKey:
        while defaultKey == randomizedKey: # case where default and randomkey happen to be the same
            randomizedKey = ''.join(random.sample(randomizedKey,len(randomizedKey)))
    return randomizedKey

if __name__ == "__main__":
    main()

'''
TEST 1
Key:  bpzhgocvjdqswkimlutneryaxf

Word:  face  Code Word:  obzg 

Key:  bpzhgocvjdqswkimlutneryaxf

Word:  blow  Code Word:  psiy 

TEST 2
Key:  vfyaultcdgrjzbnesihwpqkoxm

Word:  face  Code Word:  lvyu 

Key:  mhyifgxtsjlqcrnobdwkpaveuz

Word:  blow  Code Word:  hqnv 

TEST 3
Key:  bpzhgocvjdqswkimlutneryaxf

Word:  wonderful  Code Word:  yikhguoes 

Word:  python  Code Word:  mxnvik 

Word:  java  Code Word:  dbrb 

Word:  doedlugvusu  Code Word:  highsecrete 

TEST 4
Key:  wofjelxaginzrbqhsyutvkmdpc

Word:  wonderful  Code Word:  mqbjeylvz 

Word:  python  Code Word:  hptaqb 

Word:  java  Code Word:  iwkw 

Word:  doedlugvusu  Code Word:  jqejzvxkvuv
'''
