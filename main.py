# Create a functoin to set up print guess accuracy
def printGuessAccuracy(guess, actual):
  for index in cycle():
    letter = guess[index]
    secretWord = actual
    if letter in secretWord:
      if(letter == secetWord[index]):
        






# Create function for user guess input
def getUserGuess():
  # Open userGuess to take in a letter
  userGuess = ""
  # Create while loop to take in the input
  while len(userGuess) != 1:
    # Create input to take in user guess
    userGuess = input("Enter a letter: ")
    # Return the user guess lowercase
    return userGuess.lower()

    
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
print("Each player will have five tries to guess the correct answer.")
print("Have fun and good luck!")

# Create secret word
secretWord = "hotwheels"

# Create variable to hold user guess 
guess = ""

# Keep track of attempts
countattempts = 0

# Create a while to keep track of attempts and guesses
while countAttempts <5 and guess != secretWord:

  guess = getUserGuess()
  printGuessAccruacy(guess, secretWord)
  # Finish counting attempts
  countAttempts += 1
  print()
  print()

# Inform player if they have won or lost 
if(guess == secretWord):
  print("You won!")
else:
  print("You Lost")