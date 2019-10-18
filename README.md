# COMP110 Worksheet 3: Flowcharts and pseudocode

This is the base repository for COMP110 Worksheet 3.

Fork this repository, and edit `README.md` to show your pseudocode solving the worksheet task. Tip: use triple backticks to preserve spacing, e.g.:

![Flowchart](/images/Fallout_4_Terminal_Hacking.png)

```
START

list_of_words = [] #This list of words would be all of the words possible in the program
game_in_progress = True

WHILE game_in_progress = True:
	INPUT player_guess 

	IF likeness = target_word_length: 
		OUTPUT "You Win!"
	ENDIF

	ELSE IF likeness >= 1: 
		Compare player_guess to next item in list_of_words that share letters in the same position,
		player_next_guess should be word with greatest likeness
	ENDIF

	ELSE :
		INPUT player_next_guess
	ENDELSE

ENDWHILE

END

################################################################
			            How the Game Works
################################################################

START

likeness = 0
guesses = 4 
target_word = ""

WHILE guesses > 0

	INPUT player_guess
	guesses - 1
	FOR every character in player_guess:
		IF target_word shares character in same position:
			likeness + 1
	OUTPUT "Likeness: " + likeness
	OUTPUT "Numberof Guesses left: " + guesses
		ENDIF
		IF likeness = 5:
			OUTPUT "You Won!"
		ENDIF

ENDWHILE 

OUTPUT "Game Over!"

END

```
