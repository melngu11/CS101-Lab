print('Welcome to the Flarsheim Guesser!\n')
print('Please think of a number between and including 1 and 100')
print()
game = True
while game == True:
  #User number input and analuzed by dividing by 3 and considering remainder
  user_div_3 = int(input('What is the remainder when your number is divided by 3? '))
  print()

  if user_div_3 < 0:
    print('The value entered must be 0 or greater')
  if user_div_3 >= 3:
    print('The value entered must be less than 3')

  #User number analyzed with division of 5 and considering remainder
  user_div_5 = int(input('What is the remainder when your number is divided by 5? '))
  print()
  user_div_7 = int(input('What is the remainder when your number is divided by 7? '))
  print()
  #Loop through 1-100 to find number that follows the parameters
  for i in range (0,101):
    if i%3 == user_div_3 and i%5 == user_div_5 and i%7 == user_div_7:
      print('Your number was {}'.format(i),'\nHow amazing was that?')
      print()

  #Option to restart the game
  #play_again = input('Do you want to play again? Y to continue, N to quit 1==>')
  play_again = ""
  while play_again != 'Y' or play_again != 'N':
    play_again = input('Do you want to play again? Y to continue, N to quit 2==>')
    print(play_again)
    if play_again == 'N':
      game = False
      break
    elif play_again == 'Y':
      break