# COMP110 Worksheet 3: Flowcharts and pseudocode

This is the base repository for COMP110 Worksheet 3.

Fork this repository, and edit `README.md` to show your pseudocode solving the worksheet task. Tip: use triple backticks to preserve spacing, e.g.:

```
Enter the terminal and wait for the minigame to generate.
Choose a random word from the list.
WHILE chosen word is incorrect AND guesses is not 0:
	Check the likeness score.
	WHILE likeness score is 0 AND guesses is not 0:
		Choose a new random word.
		Lose 1 guess for each time you choose.
	END WHILE
	IF guesses is 0
		BREAK
	END IF
	Choose a new word with as many letters in the same position as the last guess.
	Compare likeness scores and keep track of what letters in what positions seem to affect the likeness score.
	Choose your next guess based on the information gained from previous guesses.
END WHILE
IF chosen word is the same as secret word:
	Congratulations, you win!
ELSE IF guesses is 0
	You lose...
END IF
```
