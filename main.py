# Create secret word
secretWord = "hotwheels"

# Create a list for the user guesses
userGuesses = []

# Create function for user guess input
def getUserGuess():
  
  # Open userGuess to take in a letter
  userGuess = ""
  
  # Create while loop to take in the input
  while len(userGuess) != 1:
    
    # Create input to take in user guess
    userGuess = input("Enter a letter: ")
    print()
    
    # Return the user guess lowercase
    return userGuess.lower()

    
# Create a function to displey letter or underscore
def displaySecretWord(secretWord, userGuess):
  letter = userGuesses
  
  # Search through each letter of secret word 
  for letter in userGuess:
    
    # Create if statement for letter in word 
    if(letter in secretWord):
      print(letter, end="")
    
      # Else, letter not in word display "_"
    else:
      print("_", end="")
  print()
  
# Create function if the user has won or not 
def userWinOrLose(userGuesses, secretWord):
  
  # Create true variable 
  win = True 
  
  # Create for loop to search word
  for letter in secretWord:
    
    # Create if statement to check letter in guesses
    if letter not in userGuesses:
      
      # Create false variable
      win = False
      break
      
# return the variable
  return win
  
# Create a game header
print(r"""
__    __       ___      .__   __.   _______ .___  ___.      ___      .__   __. 
|  |  |  |     /   \     |  \ |  |  /  _____||   \/   |     /   \     |  \ |  | 
|  |__|  |    /  ^  \    |   \|  | |  |  __  |  \  /  |    /  ^  \    |   \|  | 
|   __   |   /  /_\  \   |  . `  | |  | |_ | |  |\/|  |   /  /_\  \   |  . `  | 
|  |  |  |  /  _____  \  |  |\   | |  |__| | |  |  |  |  /  _____  \  |  |\   | 
|__|  |__| /__/     \__\ |__| \__|  \______| |__|  |__| /__/     \__\ |__| \__| 
                                                                                

""")
# Space
print()

# Print a welcome
print("Welcome to Hangman!!")

# Space 
print()

# Print Directions
print("The player must enter in only a one letter guess. If they do not they will be re-prompted to do so.")
print("Each player will have five incorrect tries to guess the correct answer.")
print("Have fun and good luck!")
# Space
print()

# Keep track of attempts
countAttempts = 0

# Create a while loop game to keep track of attempts and guesses
while countAttempts < 5 and not userWinOrLose(userGuesses, secretWord):

  # Calls the players input
  userGuess = getUserGuess()
  if userGuess in secretWord:
  
    # Add the user guesses together 
    userGuesses.append(userGuess)
    print("Correct guess!")
    print()
  
    # if user guess incorrect
  else:
    print("Incorrect guess!")
    print()
    
    # Count the incorrect attempts
    countAttempts += 1
    
    # print statement for counting strikes 
    print(f"{countAttempts} strike(s), you only get 5")
  
    # Calls the players input and compares to secret word
  displaySecretWord(userGuesses, secretWord)
  print()

# Let the player know if they have won or lost
if userWinOrLose(userGuesses, secretWord):
  print("Congrats! You Won!")
else:
  print("You Lose! You have ran out of guesses.")
