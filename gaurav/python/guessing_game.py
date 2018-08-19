import random 
randnum=random.randint(1,10)
guess=None
while True:
	guess=int(input("Guess the random no between 1-10: "))
	if guess==randnum:
		print("You won.")
		choice=input("Wanna play again(y/n): ")
		if choice=='y':
			randnum=random.randint(1,10)
		else:
			print("Thank you for playing")
			break
	elif guess>randnum:
		print("too high. try again")
	else:
		print("Too low try again")
	