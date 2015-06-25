def hangman(secretWord):
  '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    At the start of the game, let the user know how many 
    letters the secretWord contains.

    Ask the user to supply one guess (i.e. letter) per round.

    The user should receive feedback immediately after each guess 
    about whether their guess appears in the computers word.

    After each round, you should also display to the user the 
    partially guessed word so far, as well as letters that the 
    user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")
    guesses = 8
    lettersGuessed = []
    while guesses > 0: 
    print("-------------")
    print("You have " + str(guesses) + " guesses left")
    print("Available Letters: " + getAvailableLetters(lettersGuessed))
  s = raw_input("Please guess a letter: ")
s = s.lower()
  if s in lettersGuessed:
  print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
  continue
lettersGuessed.append(s)

  if s in secretWord:
  print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
  else:
  print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
  guesses -= 1
  if isWordGuessed(secretWord, lettersGuessed):
    break


    if guesses <= 0:
    print("-------------")
    print("Sorry, you ran out of guesses. The word was " + secretWord)
    else:
    print("-------------")
    print("Congratulations, you won!")
