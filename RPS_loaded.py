'''
Rock Paper Scissors. but like a broken version
'''
choice = ['Rock', 'Paper', 'Scissors']
choice = [item.lower() for item in choice]

phrase = ["Rock beats Scissors! ", "Paper beats Rock! ", "Scissors beats Paper! "]
outcome = ["You lose."]

maxRounds = 3
nRounds = 0
previousRounds = set()

userScore = 0
cpuScore = 0

print ("Best two out of three! ")

while (nRounds < maxRounds):

	rounds = raw_input ("Rock! Paper! Scissors! GO! ")
	rounds = str(rounds).lower()
		
	if (rounds in choice): #Checks to see if you entered an acceptable term (not case sensative

		if (rounds == choice[0]): #you choose rock
			print ("The Computer chose: " + choice[1]) #paper
			print (phrase[1] + outcome[0])

		elif (rounds == choice[1]): #you choose paper
			print ("The Computer chose: " + choice[2]) #scissors
			print (phrase[2] + outcome[0])

		elif (rounds == choice[2]): #you choose scissors
			print ("The Computer chose: " + choice[0]) #rock
			print (phrase[0] + outcome[0])

		nRounds = nRounds + 1 #moves to the next rounds

		cpuScore = cpuScore + 1 #computer always wins

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