def main():
    names = "names.txt"
    codes = "codes.txt"
    compressed = readAndCreate(names, codes)
    compressed = addNew("sefds","22a#22222222", compressed)
    #login(compressed)

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
    if verifyName(name, dBase) and verifyPW(pw, dBase):
        print("Requirements met, able to add to dictionary.")
        dBase[name] = pw
        return dBase
    else:
        print("Either username or password does not meet a requirement, unable to add new entry.")

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

def login(dBase):
    username = input("Enter a username to login: ")
    password = input("Enter the password for the username: ")

    for i,j in dBase.items():
        if i == username and j == password:
            print("Login is successful!")
            return
    print("Username and/or password is not found in the database.")
    
if __name__ == "__main__":
    main()
