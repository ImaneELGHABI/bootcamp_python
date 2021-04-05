import random

guesses = 0

print('This is an interactive guessing game!\nYou have to enter a number between 1 and 99 to find out the secret number.\nType exit to end the game.\nGood luck!')

nb=random.randint(1,99)

while(guesses>=0):
	print('What is your guess between 1 and 99?')
	guess=input()
	guesses+=1
	if guess.isdigit():
		if int(guess)<nb:
			print('Too low!')
		if int(guess)>nb:
			print('Too high!')
		if int(guess)==nb:
			print('Congratulations!!\n You won in '+str(guesses)+' attempts!')
			exit()
		if guesses==1 and guess==nb:
			print('The answer to the ultimate question of life, the universe and everything is '+str(nb)+'.\nCongratulations! You got it on your first try!')
			exit()
	if guess=='exit':
		print('Goodbye-_-')
		exit()
	if not guess.isdigit():
		print('That is not a number!!')
	

