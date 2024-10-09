import random

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.

    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r') # it opens a file with words
    words_list = f.readlines() # it reads all the words
    f.close() # it closes the files
    
    words_list = words_list[0].split(' ') # it splits the words into a list.
    secret_word = random.choice(words_list) # it picks one word from the list randomly.
    return secret_word # it gives you the secret word to play with.

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.

    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed

    for letter in secret_word: # it goes through each letter in the secret word
        if letter not in letters_guessed: # if a letter hasn't been guessed yet
            return False # you haven't guessed the word yet.
    return True # if all letters are guessed, you win. 

    pass

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.

    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
    
    # initialize an empty string to store final result
    guessed_word = ""

    # loop through each letter in the secret_word
    for letter in secret_word:
        if letter in letters_guessed: # if the letter was guessed
            guessed_word += letter # add the guessed letter to the result (show letter)
        else: 
            guessed_word += "_" # if not, add an underscore for unguessed letters.
    return guessed_word

    pass



def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word

    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word

    Returns:
        bool: True if the guess is in the secret_word, False otherwise

    '''
    #TODO: check if the letter guess is in the secret word
    if guess in secret_word:
        return True 
    else:
        return False

    pass




def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.

    Args:
      secret_word (string): the secret word to guess.

    '''
    player = input("Please enter your name: ")
    print(f" Welcome {player}, let's begin Spaceman! Guess the secret word, one letter at a time.")


    #TODO: show the player information about the game according to the project spec
    letters_guessed = [] # you start with no letters guessed
    attempts_left = 7 # you have 7 chance to guess wrong
    game_won = False # you haven't won the game yet

    #TODO: Ask the player to guess one letter per round and check that it is only one letter
    while attempts_left > 0 and not game_won: # the game keeps running until you win or run out of tries
        print(f" You have {attempts_left} attempts_left")
        print(f" Word so far: {get_guessed_word(secret_word, letters_guessed)}") # show what you've guessed so far

        guess = input("Please guess a letter: ").lower() 

    #TODO: Check if the guessed letter is in the secret or not and give the player feedback
        if get_guessed_word in secret_word: # if you already guessed that letter, tell you
            print("You've already guessed that letter!")
        elif is_guess_in_word(guess, secret_word): # if the letter is in the word
            letters_guessed.append(guess) # add it to the list is in the word
            print(f"Good job! {guess} is in the word.")
        else: # if the letter isn't in the word
            letters_guessed.append(guess) # add it to guessed letters
            attempts_left -= 1 # take away one of your attempts
            print(f"{guess} is not in the word.")
    #TODO: show the guessed word so far

    #TODO: check if the game has been won or lost






#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)