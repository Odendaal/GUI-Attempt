def readfile():                         #creates the function which will be used to read compressed files.
    sentencelist = []                   #creates a blank array which will be added to later.
    attempt = "no"                      #creates a variable witht he value of "no" to be used for a while loop
    while attempt == "no":              #creates a loop so if an invalid input has been entered by the user, it loops back to the begining
        filename = input("Enter file name or type cancel. If you used this program to create the file, the filename will be whatever you called it plus 'words' on the end of it. (leave out the txt): ") #user enters the name of the file they wish to read here
        if filename == "cancel":        #if the user enters cancel it takes them back to the starting screen
            menu()                      #starting screen where user enters what they wish to do (read, write or compress)
        elif filename == "Cancel":      #again the cancel option but with a captiol C to support case senstivity
            menu()
        try:                            #runs this peice of code within an error exception
            with open(filename + '.txt', 'r') as f:         #opens the file that the user identified previously in the filename variable
                words = f.readlines()                       #sets the varaible words to have all the data in the file
                for word in words:                          #for each word in the file
                    if word not in sentencelist:            #if any of the words it goes through is not in the empty array sentencelist
                        word = word.strip('\n')             #removes the newline from the word to prevent logical errors
                        sentencelist.append(word)           #adds the word to the previously empty array
                        attempt = "yes"                     #ends the while loop so the code continues to the user being takent to the menu screen
        except FileNotFoundError:                           #if this error occurs, do the following
            print("Oops! Doesn't look like there's a file with that name (not locally anyway).")    #prints that a file was not found
            attempt = "no"                                                                          #attempt remains "no" so it loops back to asking for the file name until they enter a valid response or cancel and return to the main menu
    sentencestring = " ".join(sentencelist)                                                         #assigns a space character and the the sentence in the sentence list to this variable
    print("The following sentence has been constucted: \n \n" + sentencestring)                     #outputs the sentence that was put together
    menu()                                                                                          #returns user to main screen
    
def compressfile():                                                                                 #the following code will make the compress file function
    sentence = input("Enter sentence to compress or type cancel \n > ")                             #user enters the sentence they wish to compress or returns to the main menu
    sentencename = input("Enter the sentences' name or type cancel \n > ")                          #user enters the name they wish to assign to the sentence, this will later be used for the written file name
    if sentence == "cancel" or sentencename == "cancel":                                            #if the user enters cancel in either of the entries, take the user back to the main screen
        menu()
    elif sentence == "Cancel" or sentencename == "Cancel":                                          #added capitol C's to help non-case senstivity
        menu()
    sentencelist = sentence.split()                         #creates a list that contains each induvidual word from the sentence that the user inputed
    words = {}                                              #refer to task 2 from line 5 for information on this commentary
    index = 0
    for word in sentencelist:
        if word not in words:
            words[word] = index
            index += 1

    with open(sentencename + 'index.txt', 'w') as f:
        for word in sentencelist:
            f.write('%d\n' % words[word])

    with open(sentencename + 'words.txt', 'w') as f:
        for word in sentencelist:
            f.write(word)
            f.write('\n')
    print("File successfully compressed!")
    menu()

def menu():                                                 #the following code will be the functioning for the main menu
    print("Hello welcome to my controlled assessement task 3. What do you want to do? \n 1) Read file \n 2) Compress sentence into file \n 3) Exit") #give the user multiple choices for what they want to do
    optionloop = int(0)                                     #had to make sure the program new that this is an integer at 0.
    while optionloop == 0:                                  #while the option loop is 0 do the following code
        try:
            choice = int(input("> "))                       #user enters the number choice they wish to do
            while choice not in (1, 2, 3):                  #another while loop so if the user enters an invalid option it loops them to line 58 until they enter a valid choice
                choice = int(input("Enter a valid choice (1 to 3). \n >  "))
            if choice == 1:                                 #if the user enters 1 it take them to readfile function
                optionloop == 1                             #ends the while loop allowing the code to continue to the correct function
                readfile()
            elif choice == 2:
                optionloop == 1
                compressfile()
            elif choice == 3:
                optionloop == 1
                print("Cya!")                               #a goodbye message for the user if they decide to quit the program
                exit                                        #ends the program
        except ValueError:                                  #if the program recieves the value error (can be caused by using a string in the integer input), the optionloop variable takes them back to line 56
            optionloop == 0
menu()                                                      #the first peace of code the program actually runs is this. Shows the user the menu function, refer to line 52 to see what will appear.
