# Hangman game


import random

WORDLIST_FILENAME = "E:/python/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    
    x = 0
    for l in secretWord:
        for i in range(len(lettersGuessed)):
            if l == lettersGuessed[i]:
                x += 1
    
    
    return x >= len(secretWord)



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    a = ''
    for l in secretWord:
            if l in lettersGuessed:
                a += l
            else:
                a += '- '
    
    return a
    



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    
    import string
    a = string.ascii_lowercase
    
    for i in lettersGuessed:
        if i in a:
            a = a.replace(i,'')
    
    
    return a
    

def hangman(secretWord):
    
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ',len(secretWord),' letters long.')
    print('------------')
    
    m = 8
    lettersGuessed = []
    
    
    while m >= 1 :
        
        print('You have',m,' guesses left.')
        print('Available letters:')
        print( getAvailableLetters(lettersGuessed))
        
        guessedLetter = input('Please guess a letter:').lower()

        if guessedLetter == 'z':
           break
        
        if guessedLetter in lettersGuessed:
            print('Oops! You already choosed that!')
            continue
        else:
            lettersGuessed.append(guessedLetter)
            
        
        if isWordGuessed(secretWord,lettersGuessed) == True: 
            print('Good guess: ',secretWord)
            print('Congratulation, you won!')
            break
        
        
        if guessedLetter in secretWord:     
            print('Good Guess:',getGuessedWord(secretWord,lettersGuessed))  
        else:
            print('Oops! That letter is not in my word:')
            m -= 1
        
        print('---------')
        
        if m == 0:
            print('Sorry, you ran out of guesses. The word was',secretWord)
            

        
     
            



secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
