# FILE ENCRYPTION AND/OR DECRYPTION
#### Video Demo: https://youtu.be/GDmiboNJia4
#### Description:
This program encrypts or decrypts a text file to make its content unreadable or readable respectively.
### The Program's working:
The program first asks the user what they would like to choose from a 3-option menu containing *Encrypt a file*, *Decrypt a File*, or *Exit* the
program. If the user chooses option-1, the program enters the encryption stage where it asks the user if they want to create a new *randomly* generated key or want to use an existing key generated some time before through the same program. If the user chooses to generate a new key file, the program does so informing the user that the key file was generated successfully later. If an old key file is to be used, the program asks the user to specify its name. If the extension of the provided filename is `.csv`, then the program movies forward, and if not, then it repromts the user for a valid key-file name; similarily, if the file exists, the program moves forward, else reprompts the user for the file name. Upon key file generation, the program asks the user for a text file to encrypt. If the user provides a file that exists and has a `.txt` extension, the program moves forward and encrypts the text in a format unreadable without the key file, otherwise repromts the user for a valid text file. The program will display a message after successfully encrypting the text file, and then show the 3-option primary menu again.
If the user now wants to decrpyt the file, he can do so by typing *'2'* in. the program will ask for a valid key file and text file to decrypt. Beware the names are valid otherwise the program will repromt the user. Upon succesfull decryption, the program will display a message, and show the primary menu again.
In order to quit the program, the user has to press 3 and the program will exit via `sys.exit()`.

### Functions defined in the program:
#### 1. `key()`:
To generate a random yet unique (both key and values so that none is repeated) [key,value] pairs, append it to a list and return the list
#### 2. `generate_key([sequence with [key,value]], filename)`:
Takes two parameters namely a list and a filename in `.csv` format. Creates a file with the same name and extension, by DictWriter method, given fieldnames "old" and "new". "old" for the original readable characters that make sense to humans and "new" to the characters with which the original characters are to be replaced in the text file so that it doesn't makes sense to humans.
#### 3. `encrypt(textfile, keyfile)`:
encrypts the *textfile* passed in as one of the parameters, by using the *keyfile* passed as the other parameter and makes it from readable to unreadable, hence making the content in it secured.
#### 4. `decrypt(textfile, keyfile)`:
decrypts the *textfile*, passed in as one of the arguments, previously encypted through the program, by using the *keyfile* passed as the other parameter and makes it readable from unreadable, hence making the content reabable to the user when desired.
#### 5. `menu()`:
makes the menu interactive, ensuring all the files passed in are valid and existent, reprompts the user when necessary, and giving proper messages when required.
#### 6. `main()`:
the main function which calls menu(). menu() then calls all the other functions according to the programmer's need.

### Testing of all the functions (except main()):
in the file `test_project.py`, 4 tests are defined testing key(), generate_key(), encrypt(), and decrypt(). There wasn't much to test for key() function as its return value is completely random hence can't be predicted, but I have tried to test if the function returns a list or not, and if the length of the list is 95 or not. Test for generate_key() tests if the `test.csv` file passed in as the 2nd argument has the *test* list of values passed in the 1st argument, and if the function returns `None` or not. Test for encrypt() tests if the *test* file created through the *test* function actually encrypts the *test* file with the help of the *test* key file. And lastly, the test of decrypt() file tests if the *test* encrypted file can be decrypted with the *test* key file to create the desired output.
