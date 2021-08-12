# guess number excercise

import random
r = random.randint(1, 100)

while True:
	num = input('Please guess a number between 1 and 100:') #string
	num = int(num) #casting
	if num == r:
		print('Congrats! You are right!')
		break
	elif num > r:
		print('Your guess is larger than the number!')
		print('Try again...')
	else:
		print('Your guess is smaller than the number!')
		print('Try again...')


