#This is a number guessing game with easy [0,3], medium [0,10], and hard mode [0,50].

#Start with import of random package and declaring global variables
import random

maxguess = 0
numbertoguess = 0
winner = 0
invalidinput = 'invalid'

#Welcome the user & request user game name
print('Welcome to BoredGames Guessing Game!')
gname = input('Gamer Name: ')

#Request user's desired game difficulty. Based on difficulty, random generate a number in the appropriate ranges 
# easy (0,3) medium (0,10) hard (0, 50).
#Ensure user inputs a valid value without being case-sensitive. Prompt user to input a valid value in case of
#input errors. 
while invalidinput != '':
    difficulty = input('Choose your difficulty: Easy, Medium, Hard: ')
    difficulty = difficulty.lower()
    def generate_nbr(difficulty):  
        global invalidinput
        global maxguess
        global numbertoguess
        if difficulty == 'easy':
            numbertoguess = random.randint(0,1)
            maxguess = 1
            invalidinput = ''
        elif difficulty == 'medium':
            numbertoguess = random.randint(0,5)
            maxguess = 5
            invalidinput = ''
        elif difficulty == 'hard':
            numbertoguess = random.randint(0,10)
            maxguess = 10
            invalidinput = ''
        else:
            print ('Oops! Please select a valid difficulty')
    generate_nbr(difficulty)
print(numbertoguess)

#Prompt user to guess the random generated number. Provide user with hint of max number to guess. 
guess = input(f'Select a number from 0 to {maxguess}: ')

#Evaluate if user guessed correctly. Convert string guess to integer, compare with random number generated. 
#If comparison evaluates to true/1 then return a trophy ASCII, otherwise, prompt for another guess until user has won. 
while winner != 1:
    converted_guess = int(guess)
    if converted_guess == numbertoguess:
        winner = 1
        print('''
    _______
   |  YOU  |
  (| W O N |)
   |  !!!  |
    \     /
     `---'
     _|_|_
    
        ''')
    else: guess = input('Guess again! :') 
    
