# COMP110 Worksheet 3: Flowcharts and pseudocode

This is the base repository for COMP110 Worksheet 3.

Fork this repository, and edit `README.md` to show your pseudocode solving the worksheet task. Tip: use triple backticks to preserve spacing, e.g.:

```
possibleAnswers = list of words from dictionary
correctAnswer = random word from possibleAnswers	
wrongGuess = 0
likeness = 0

WHILE wrongGuess <=4:
	PRINT "Guess the word"
	INPUT currentAnswer #an answer from possibleAnswers
	possibleAnswersCopy = possibleAnswers #copy of the available answers so we can edit while we loop through the original.
	
	IF(likeness > 0)
		for answer in possibleAnswers:
			currWordLikeness = checkLikeness() 
			if (currWordLikeness < likeness)
				possibleAnswersCopy.remove([answer])
	ENDIF
	
	possibleAnswers = possibleAnswersCopy #after looping through the list we replace it with the updated one.
	
	IF (correctAnswer == currentAnswer)
		PRINT("Player Wins.")
	ELSE
		correctLetters = 0
		for i in correctAnswer:
			for j in currentAnswer:
				if i == j:
				correctLetters++
			break
			
		PRINT("You got " + correctLetters + " letters correct.")
		likeness = correctLetters
		wrongGuess++;
	ENDIF
END
```
