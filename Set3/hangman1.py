
def isWordGuessed(secretWord, lettersGuessed):
  '''
  secretWord: string, the word the user is guessing
  lettersGuessed: list, what letters have been guessed so far
  returns: boolean, True if all the letters of secretWord are in lettersGuessed;
  False otherwise
  '''
  if len(lettersGuessed) == 0:
    return False

  for i in range(len(secretWord)):
    if secretWord[i] in lettersGuessed:
      continue
    else:
      return False
  return True

def getGuessedWord(secretWord, lettersGuessed):
  '''
  secretWord: string, the word the user is guessing
  lettersGuessed: list, what letters have been guessed so far
  returns: string, comprised of letters and underscores that represents
  what letters in secretWord have been guessed so far.
  '''
  s = ""
  for i in range (len(secretWord)):
    if secretWord[i] in lettersGuessed:
      s = s + secretWord[i]
    else:
      s = s + '_'
  return s
secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print getGuessedWord(secretWord, lettersGuessed)

import string
def getAvailableLetters(lettersGuessed):
  '''
  lettersGuessed: list, what letters have been guessed so far
  returns: string, comprised of letters that represents what letters have not
  yet been guessed.
  '''
  s = string.ascii_lowercase
  for i in range(len(lettersGuessed)):
    if lettersGuessed[i] in s:
      s = s.replace(lettersGuessed[i], "")
  return s
    
