# COMP110 Worksheet 3: Flowcharts and pseudocode

This is the base repository for COMP110 Worksheet 3.

Fork this repository, and edit `README.md` to show your pseudocode solving the worksheet task. Tip: use triple backticks to preserve spacing, e.g.:

```
begin

word_list <- list of all the possible passwords on the terminal

guesses <- 4

for word in word_list:
	if likeness == compareLikeness(chosenword, word)
		likeness <- inputWordForLikeness(word)
		chosenword <- word
		guesses --
		if chosenword == word:
			output "Password Accepted."
			end
		endif
		if guesses = 0
			output "Init Terminal Lockout"
			end
		endif
	endif
endfor

end
```
