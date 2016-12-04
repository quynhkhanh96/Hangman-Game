# Hangman game

import random

WORDLIST_FILENAME = "words.txt"

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

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    check=False
    secret=list(secretWord)
    for i in range(len(secret)):
        if secret[i] in lettersGuessed:
            check=True
        else:
            check=False
        if check==False:
            break
    return check
        
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    secretw=list(secretWord)
    for j in range(len(secretw)):
        if secretw[j] not in lettersGuessed:
            secretw[j]='_ '
    word=''.join(secretw)
    return word

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    alpha=list(string.ascii_lowercase)
    alpha2=alpha[:]
    for c in alpha:
        if c in lettersGuessed:
            alpha2.remove(c)
    s=''.join(alpha2)
    return s
secretWord=chooseWord(wordlist)
  
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    '''
    turn=0
    lettersGuessed=[]
    done=False
    print("Welcome to the game, Hangman!\nI am thinking of a word that is "+str(len(secretWord))+" letters long.\n-------------")
    while 8-turn>0:
       if done==False:
          print("You have "+str(8-turn)+" guesses left.")
          print("Available Letters: "+getAvailableLetters(lettersGuessed))
          guess=input("Please guess a letter: ")
          if guess in lettersGuessed:
             print("Oops! You've already guessed that letter: "+getGuessedWord(secretWord, lettersGuessed))
          elif guess in secretWord:
             lettersGuessed+=[guess,]
             
             print("Good guess: "+getGuessedWord(secretWord, lettersGuessed))
          else: 
             print("Oops! That letter is not in my word: "+getGuessedWord(secretWord, lettersGuessed))
             turn+=1
          print("------------")
          done=isWordGuessed(secretWord,lettersGuessed)
       else:
          print("Congratulations, you won!")
          break
    if done==False:
       print("Sorry, you ran out of guesses. The word was else.")
             
playAgain='yes' 
while playAgain=='yes' or playAgain=='y':
    hangman(secretWord)
    print("Do you want to play again? (yes or no)")
    playAgain=input()
