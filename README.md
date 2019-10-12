# COMP110 Worksheet 3: Flowcharts and pseudocode

This is the base repository for COMP110 Worksheet 3.

Fork this repository, and edit `README.md` to show your pseudocode solving the worksheet task. Tip: use triple backticks to preserve spacing, e.g.:

```
START

guesses = 4

likeness = 0

list of words = ["words", etc]

list of chosen words = []

winningWord chosen by random from list of words

PRINT list of words


while GUESSES > 0:
	chosenWord = INPUT "Choose a word from the list:"
	IF chosenWord is already in list of chosen words:
		PRINT "this word has been guessed"
	ELSE:
		APPEND chosenWord to list of chosen words
		FOR every character IN chosenWord:
			IF winningWord has same character:
				likeness + 1
	ENDIF

	
	IF chosenWord == winningWord:
		PRINT "You won!"
	ENDIF
	GUESSES - 1
	PRINT "Amount of guesses left" + GUESSES


	IF GUESSES == 0:
		print "GAME OVER"
		print "The word was: " + winningWord
	ENDIF


END
```
