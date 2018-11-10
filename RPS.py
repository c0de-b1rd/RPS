'''
Rock Paper Scissors
'''
import random

choice = ['Rock', 'Paper', 'Scissors']
#for item in choice:
#	choice
# or 
#for i in range(0,len(choice)):
#	choice[i] = choice[1].lower()
# or 
choice = [item.lower() for item in choice]

phrase = ["Rock beats Scissors! ", "Paper beats Rock! ", "Scissors beats Paper! "]
outcome = ["You win!", "You lose."]

maxRounds = 3
nRounds = 0
previousRounds = set()

userScore = 0
cpuScore = 0

print ("Best two out of three! ")

while (nRounds < maxRounds):

	rounds = raw_input ("Rock! Paper! Scissors! GO! ")
	rounds = str(rounds).lower()
		
	if (rounds in choice): #Checks to see if you entered an acceptable term (not case sensative)

		number = random.randint(0,2)
	
		print ("The Computer chose: " + choice[number])

		if (rounds == choice[number]): #if you both choose the same thing
			print ("You both chose " + str(rounds) + "! Nobody wins.")

		else: 
			if (rounds == choice[0]): #you choose rock
				if (choice[number] == choice[1]): #paper
					print (phrase[1] + outcome[1])
					cpuScore = cpuScore + 1
				elif (choice[number] == choice[2]): #scissors
					print (phrase[0] + outcome[0])
					userScore = userScore + 1

			elif (rounds == choice[1]): #you choose paper
				if (choice[number] == choice [0]): #rock
					print (phrase[1] + outcome[0])
					userScore = userScore + 1
				elif (choice[number] == choice[2]): #scissors
					print (phrase[2] + outcome[1])
					cpuScore = cpuScore + 1

			elif (rounds == choice[2]): #you choose scissors
				if (choice[number] == choice[0]): #rock
					print (phrase[0] + outcome[1])
					cpuScore = cpuScore + 1
				elif (choice[number] == choice[1]): #paper
					print (phrase[2] + outcome[0])
					userScore = userScore + 1

			nRounds = nRounds + 1 #moves to the next rounds

		if ((maxRounds - nRounds) == 1): #alerts player how many rounds are left
			print ("There is 1 round left.")
			print ("The current score is: " + str(userScore) + " to " + str(cpuScore))

		elif ((maxRounds - nRounds) == 0):
			print ("There are no rounds left. The final score is: " + str(userScore) + " to " + str(cpuScore))
			if (userScore > cpuScore):
				print ("You won!")
			else:
				print ("You lost.")

		else:
			print ("There are " + str(3 - nRounds) + " rounds left.")
			print ("The current score is: " + str(userScore) + " to " + str(cpuScore))

		print ("")

	else:
		print ("That is not part of the game.")