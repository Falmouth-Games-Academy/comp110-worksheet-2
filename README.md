# comp110-worksheet-B
Base repository for COMP110 worksheet B

**Pseudocode for Fallout 4 hacking game**

	guesses = 4 # Number of guesses used for loop
	guesses_left = 4 # Used to track guesses left 
	word = random word from database # The word to be checked agaisnt
	word_length = number of characters in chosen word # Length of word

	print 'The password is ' word_length ' characters long, you have ' guesses ' guesses to get it right!'

	for i in range(0, guesses): # Loops as many times as guesses allowed or until broken by the loop
		if i == 4 # If 4 guesses have been done print failure and break loop
			print 'Out of guesses, the auorities have been contacted and will arive shortly'
			break
		print 'What is your guess?'
		get inputed guess
		right = how many characters of the inputed string match against word including position # checks inputed guess with the word to see how many characters match type and position.

		if right == word_length: # if they got the word print well done and break loop
			print 'Well done you have accessed the machine'
			break
		else: # If they didn't get the word print how many they got right and reduce guesses_left by 1
			print 'You got ' right ' characters correct'
			guesses_left -= 1
		

**Flowchart**
![alt text](https://raw.githubusercontent.com/HoaxShark/comp110-worksheet-B/master/HackFlowV2.png "Game flowchart")

