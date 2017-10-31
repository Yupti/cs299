

def main():
    names = "names.txt"
    codes = "codes.txt"
    compressed = readAndCreate(names, codes)
    #addNew("Samwoo", 12, compressed)
    #verifyName("2amwoo", compressed)
    verifyPW("11111111112", compressed)

def readAndCreate(names, codes):
    L1 = []
    L2 = []
    book = open(names, 'r')
    book2 = open(codes, 'r')

    for line in book:
        row = line.split()
        L1.extend(row)

    for line2 in book2:
        row = line2.split()
        L2.extend(row)

    book.close() # needs confirm
    book2.close() # same as above
    compressed = dict(zip(L1, L2))
    return compressed

#def addNew(name, pw, dBase):
    

def verifyName(name, dBase):
    if name[0].isalpha():
        for i in dBase.keys():
            if i == name:
                print("This username is already being used.")
                return False
    else:
        print("This username does not start with a letter, unable to use.")
        return False
    
    print("This username can be used.")
    return True

def verifyPW(pw, dBase):
    if len(pw) < 8:
        print("Password is too small, unable to use.")
        return False
    else:
        for i in dBase.keys():
            if dBase[i] == pw:
                print("This password already exists.")
                return False
        specials = ['#','$', '^', '*', '+', '=', '-', '_']
    
        
    
if __name__ == "__main__":
    main()
