# guess number excercise

import random
print('This is a game of guessing numbers. You can define the interval of numbers')
start = input('Please choose your starting number:') #string
end = input('Please choose your ending number:') #string
start = int(start) #casting
end = int(end) #casting
r = random.randint(start, end)
count = 1 #number of guess

while True:
	num = input('Please guess a number:') #string
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
