# comp110-worksheet-B
Base repository for COMP110 worksheet B

Cloose a list of words (lists contain words with different word length).
Chooses a secret word from the chosen list of words
Chooses between 8 and 14 other words from the same list.
Display all chosen words randomly within a mess of punctuation.
	This punctuation could all be randomly chosen from a list too.
	
Default remaining guesses to 4 and 'game won' to false.	
While guesses taken < 4
	Prompt the player to select a word (or a punctuation, i guess)
	Provide feedback on their chosen word; how many letters are correct?
	If they win, 
		break and 'game won': true, 
	else 
		Increment 'guesses taken'.
	
Repeat this cycle until they're out of guesses (or if break out of while)
If they've won
	Grant them access to the terminal (with a secret message inside).
If they've lost
	Lock them out of the terminal for exceeding the maximum false attempts.
	Tell them to wait 5 seconds before they can play again
	Sleep (5 seconds)
	Do you want to play again?
