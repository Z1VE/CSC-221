# ===============================================================
# NAME: Matthew Rumph
# DATE: 08/27/26
# COURSE: CSC-221-section number
# ALGORITHM:
# Step 1. Prompt for files & output name
# Step 2. Load and store files
# Step 3. Process file and load tokens
# Step 4. Turn data into readable prompt for user
# Step 5. prompt user for specific tokens and store their input
# Step 6. Replace tokens in text
# Step 7. Store new resulting file
# Step 8. Prompt user if they want to see their new story
# Step 9. Display story
# Step 10. Ask if they want to play again
# REFERENCES: GeeksforGeeks (try & except handling)
# ===============================================================

#------------ Tools ------------

# Manual split function
def split(txt):
    """
    Manually splits all words on spaces or newline characters
    :param txt:
    :return:
    """
    splitText = []
    currentWord = ""
    for char in txt:
        if char == " ":
            splitText.append(currentWord)
            currentWord = ''
        elif char == '\n':
            splitText.append(currentWord)
            splitText.append('\n')
            currentWord = ''
        else:
            currentWord += char
    # clean out words that are 0 chars in length
    for word in splitText:
        if len(word) == 0:
            splitText.remove(word)
    return splitText


#------------------------------------

# Prompt and save output / input

def loadFiles():
    """
    prompts the user and validates for filename and output name then saves and returns the loaded story
    :return: tuple of story and output name
    """
    # Validate and load story
    found = 0
    while found == 0:
        filename = input("What's the name of your file? : ")
        try:
            with open(filename) as file:
                found = 1
                story = split(file.read())

        except FileNotFoundError:
            print("Your file was not found please try again!")
    # stores and
    outputname = input("What would you like to call your finished story? : ")

    return story,outputname


# Function to identify all tokens in text
def findTokens(story):
    """
    Finds & stores tokens in story.
    :param story: str of imported Story
    :return: tuple of tokens
    """
    Tokens = []
    for word in story:
        if word[0] == "<" and word[-1] == ">":
            Tokens.append((word,''))
    return Tokens


# Clean Token function
def CleanToken(Token):
    """
    Cleans the tokens from unnecessary dashes and <> symbols
    :param Token: str Token that is to be cleaned
    :return: str Cleaned token
    """
    NoTag = Token[0][1:-1]
    result = NoTag[0]
    for char in NoTag[1:]:
        if char != "-":
            result += char
        else:
            result += " "
    return result



# function to prompt user for tokens
def TokenRequest(Tokens):
    """
    Requests a word for each token in our story
    :param Tokens: list of tuples of all tokens found in our story
    :return: new list of tuples of our token followed by the user's input [('Name','Cooper'),(...,...)]
    """
    result = []
    print("\n")
    for Token in Tokens:
        CleanedToken = CleanToken(Token)
        result.append((Token[0],input(f"Please Type {"an" if CleanedToken[0] in 'AaEeIiOoUu-' else "a"} {CleanedToken} : ")))
    print('\n\n\n')
    return result

# replace story with tokens
def replaceStory(story, tokens):
    """
    Replaces tokens in our story with the input's we gave
    :param story: list of strings containing our whole story
    :param tokens: list of tuples of (token , input)
    :return: str fully replaced story
    """
    newStory = ''
    count = 0
    isFirstword = True
    for word in story:
        if word[0] == "<" and word[-1] == ">":
            if isFirstword:
                newStory += tokens[count][1]
                count += 1
                isFirstword = False
            else:
                newStory += ' ' + tokens[count][1]
                count += 1
        elif word in '.,!?"\';:\n':
            newStory += word
            if word == "\n":
                isFirstword = True
        else:
            if isFirstword:
                newStory += word
                isFirstword = False
            else:
                newStory += ' ' + word
    return newStory

# Save to File
def saveStory(story,output):
    """
    Saves the story to a file
    :param story: str of finished story
    :param output: name of output filename
    """
    with open(output,'w', encoding='utf-8') as file:
        file.write(story)
# Call main

def main(rerun):
    if not rerun:
        print("Welcome to the game of Mad Libs.\n\nI will ask you to provide multiple words and phrases to fill in a mad lib story.\nThe result will be written to an output file\n")
    # load files
    story,output = loadFiles()

    # find tokens
    Tokens = findTokens(story)

    # Request Tokens
    FilledTokens = TokenRequest(Tokens)

    # Create Finished story
    finalStory = replaceStory(story, FilledTokens)

    # Write the story to text file
    saveStory(finalStory,output)

    printStory = input("Do you want to see the resulting story? (Y to confirm / Any key to exit): ")
    if printStory in "yY":
        print(replaceStory(story,FilledTokens) + '\n\n\n')

    playAgain = input("Do you want to create another madlib? (y|n): ")
    if playAgain in 'yY':
        print('\n\n\n')
        main(True)



if __name__ == '__main__':
    main(False)
