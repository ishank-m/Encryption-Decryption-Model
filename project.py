#Importing all the necessary modules (random, csv, os, sys).
import random
import csv
import os
import sys

#Defining main().
def main():
    menu() #Calling menu() function in main().



#Defining a custom function 'key()' to generate alphabets, numbers, symbols paired with
#randomly generated alphabets, numbers, symbols so that each character is used only once.
def key():
    list = [] #Initializing an empty list
    for i in range(32,127): #Generating a corresponding value for all characters in ASCII table.
        old = chr(i)
        while True:
            new = chr(random.randint(32,127))
            if new not in [pair[1] for pair in list]:  #To ensure all the new characters are unique and not already assigned to some other character.
                break
        list.append([old, new]) #Adding the pair to the previously initialized list.
    return list #returning the list when all the characters are successfully paired with some other unique character.


#Generates a keyfile in csv format
def generate_key(list, filename):
    with open(filename, "w", newline='') as file:
        fieldnames = ["old", "new"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(len(list)):
            writer.writerow({"old": list[i][0], "new": list[i][1]})


#Encryptes a txt file by replacing each character("old") with the new character ("new") of the "old":"new" pair
#in the key file and then saving the txt file.
def encrypt(textfile, keyfile):
    dict = {}
    with open(textfile, "r") as text, open(keyfile, "r", newline='') as key, open("temp.txt", "w") as temp:
        csvreader = csv.DictReader(key)
        for row in csvreader:
            dict[row["old"]] = row["new"]
        line = text.readlines()
        for word in line:
            for letter in word:
                if letter != "\n":
                    temp.write(dict[letter])
                if letter == "\n":
                    temp.write("\n")
        text.close()
        temp.close()
        key.close()
        os.remove(textfile)
        os.rename('temp.txt', textfile)


#Decrypts a text file with the help of a key file, by first reverting the "old":"new" pair to "new":"old" pair
#and then substituting each character("new") with the original character("old") and saving the txt file.
def decrypt(textfile, keyfile):
    dict = {}
    with open(textfile, "r") as text, open(keyfile, "r", newline='') as key, open("temp.txt", "w") as temp:
        csvreader = csv.DictReader(key)
        for row in csvreader:
            dict[row["new"]] = row["old"]
        line = text.readlines()
        for word in line:
            for letter in word:
                if letter != "\n":
                    temp.write(dict[letter])
                if letter == "\n":
                    temp.write("\n")
        text.close()
        temp.close()
        key.close()
        os.remove(textfile)
        os.rename('temp.txt', textfile)


#Menu for making the program more appealing and interactive.
def menu():
    while True:
        print("============================")
        print("1. Encrypt a File")
        print("2. Decrypt a File")
        print("3. Exit")
        print("============================")
        q1 = input("Your choice (1/2/3): ")
        if q1 == '1':
            while True:
                print("============================")
                print("1. Do you want to create a new key?")
                print("2. Do you want to use an existing key?")
                print("============================")
                q2 = input("Enter choice (1/2): ")
                if q2 == '1':
                    while True:
                        print("============================")
                        keyfilename = input("Enter your desired name for key file, with (.csv) extension: ")
                        if keyfilename.endswith(".csv"):
                            break
                        else:
                            print("============================")
                            print("Invalid filename")
                            continue
                    generate_key(key(), keyfilename)
                    print("============================")
                    print(f"Your encryption key was generated and stored as {keyfilename}")
                    print("============================")
                    while True:
                        textfilename = input("Enter name of you text file, with (.txt) extension: ")
                        if textfilename.endswith(".txt") and os.path.exists(textfilename):
                            pass
                        else:
                            print("============================")
                            print("Invalid filename or File does not exists")
                            print("============================")
                            continue
                        encrypt(textfilename, keyfilename)
                        print("============================")
                        print("Your file is successfully encrypted!")
                        print("============================")
                        break
                    break
                elif q2 == '2':
                    while True:
                        print("============================")
                        keyfilename = input("Enter name of your key file, with (.csv) extension: ")
                        print("============================")
                        if keyfilename.endswith(".csv") and os.path.exists(keyfilename):
                            break
                        else:
                            print("Invalid filename or File does not exists")
                            continue
                    while True:
                        textfilename = input("Enter name of you text file, with (.txt) extension: ")
                        print("============================")
                        if textfilename.endswith(".txt") and os.path.exists(textfilename):
                            pass
                        else:
                            print("Invalid filename or File does not exists")
                            print("============================")
                            continue
                        encrypt(textfilename, keyfilename)
                        print("Your file is successfully encrypted!")
                        print("============================")
                        break
                    break
                else:
                    print("============================")
                    print("Invaid Choice")
                    print("============================")
                    continue
        if q1 == '2':
            while True:
                print("============================")
                keyfilename = input("Enter name of your key file, with (.csv) extension: ")
                print("============================")
                if keyfilename.endswith(".csv") and os.path.exists(keyfilename):
                    break
                else:
                    print("Invalid filename or File does not exist")
                    continue
            while True:
                textfilename = input("Enter name of you text file, with (.txt) extension: ")
                print("============================")
                if textfilename.endswith(".txt") and os.path.exists(textfilename):
                    pass
                else:
                    print("Invalid filename or File does not exists")
                    print("============================")
                    continue
                decrypt(textfilename, keyfilename)
                print("Your file is successfully decrypted!")
                print("============================")
                break
        if q1 == '3':
            print("============================")
            print("Exiting the program...")
            print("============================")
            sys.exit()
        elif q1 not in '123' and q1 != None:
            print("============================")
            print('Invalid Choice')
            print("============================")
            continue


#Calling main().
if __name__=="__main__":
    main()


