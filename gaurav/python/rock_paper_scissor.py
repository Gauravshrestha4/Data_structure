import random
choice=['rock','paper','scissor']
input1=input("Enter player1 choice:")
computer=choice[int(random.randint(0,))]
print("Computer chooses :"+computer)
p1=False
p2=False
if input1==computer:
	print("draw")
else:
	if input1=='rock':
		if computer=='paper':
			p2=True
		elif computer=='scissor':
			p1=True
	elif input1=='paper':
		if computer=='rock':
			p1=True
		elif computer=='scissor':
			p2=True
	else:
		if computer=='paper':
			p1=True
		elif computer=='rock':
			p2=True
	if p1==True:
		print("player 1 wins")
	else:
		print("palyer2 wins")