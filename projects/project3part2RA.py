def main():
    names = "names.txt"
    codes = "codes.txt"
    
    compressed = readAndCreate(names, codes)
    
    compressed = addNew("Yupti", "asdf123$$", compressed)
    compressed = addNew("gantu06", "strOG#25", compressed)
    compressed = addNew("crazytyler", "__gr3at__", compressed)
    
    login("Yupti", "asdf123$$", compressed)
    login("lisaAn1", "X&122343", compressed)
    login("claskupo", "difj23D*&", compressed)
    login("jimbo", "flags8%", compressed)

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

    book.close() 
    book2.close() 
    compressed = dict(zip(L1, L2))
    return compressed

def addNew(name, pw, dBase):
    print("Attempting to add user:", name, " with password:", pw)
    if verifyName(name, dBase) and verifyPW(pw, dBase):
        print("Requirements met, able to add to dictionary.\n")
        dBase[name] = pw
        return dBase
    else:
        print("Either username or password does not meet a requirement, unable to add new entry.\n")
        return dBase

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
    checker = 0
    if len(pw) < 8:
        print("Password is too small, unable to use.")
        return False
    else:
        for i in dBase.keys():
            if dBase[i] == pw:
                print("This password already exists.")
                return False
        specials = ['#','$', '^', '*', '+', '=', '-', '_']
        for sign in specials:
            if sign in pw:
                checker += 1
                break
        if any(x.isupper() for x in pw):
            checker += 1
        if any(x.islower() for x in pw):
            checker += 1
        if any(x.isdigit() for x in pw):
            checker += 1
            
    if checker < 3:
        print("The new password does not meet at least 3 requirements, unable to use.")
        return False
    else:
        print("The new password can be used.")
        return True

def login(username, password, dBase):
    print("Attempting to log in with user:", username, "password:", password)
    for i,j in dBase.items():
        if i == username and j == password:
            print("Login is successful!\n")
            return
    print("ACCESS DENIED: Username and/or password is not found in the database.\n")
    
if __name__ == "__main__":
    main()
