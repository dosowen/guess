import random
v = int(input ("choose the number you are going to guess from :"))
e = int(input ("choose the number you are going to guess to end :"))
r = random.randint(v, e)
n = int(input("guess a number:"))
c = 0
while True:
	if n == r :
		print('you got it right')
		break
	elif r > n:
		c = c + 1
		print ('You got it wrong!','You guess',c,'time')
		n = int(input('the answer is Bigger! Guess another number:'))
	elif r < n:
		c = c + 1
		print ('You got it wrong!','You guess',c,'time')
		n = int(input('the answer is Smaller! Guess another number:'))