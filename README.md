# comp110-worksheet-B
Base repository for COMP110 worksheet B

**Pseudocode for Fallout 4 hacking game**

guesses = 4
guesses_left = 4
word = random word from database
word_length = number of characters in chosen word

print 'The password is ' word_length ' characters long, you have ' guesses ' guesses to get it right!'

for i in range(0, guesses):
	if i == 4
		print 'Out of guesses, the auorities have been contacted and will arive shortly'
		break
	print 'What is your guess?'
	get inputed guess
	right = how many characters of the inputed string match against word including position

	if right == word_length:
		print 'Well done you have accessed the machine'
		break
	else:
		print 'You got ' right ' characters correct'
		guesses -= 1
	


![alt text](https://raw.githubusercontent.com/HoaxShark/comp110-worksheet-B/master/HackFlowV2.png "Game flowchart")

