# guess number excercise

import random
r = random.randint(1, 100)
count = 1 #number of guess

while True:
	num = input('Please guess a number between 1 and 100:') #string
	num = int(num) #casting
	if num == r:
		print('Congrats! You are right!')
		print('You have guessed', count, 'time(s).')
		break
	elif num > r:
		print('Your guess is larger than the number!')
	else:
		print('Your guess is smaller than the number!')
	print('You have guessed', count, 'time(s).')
	count = count + 1 


