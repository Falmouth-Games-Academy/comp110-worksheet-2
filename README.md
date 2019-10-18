# COMP110 Worksheet 3: Flowcharts and pseudocode

This is the base repository for COMP110 Worksheet 3.

Fork this repository, and edit `README.md` to show your pseudocode solving the worksheet task. Tip: use triple backticks to preserve spacing, e.g.:

```
declare guesses as int
declare likeness_score as int
declare number_letters as int

guesses = 4
number_letters = a random number the computer generates
likeness_score = how close your chosen word is to the word chosen by the computer

Open terminal
while guesses > 0:
	Choose a word and click on it
	guesses -= 1
	If chosen word has likeness_score == 0:
		Choose another word completely different to last one
	elif chosen word has likeness_score > 0 and < number_letters:
		Choose another word somewhat similar to last one
	elif chosen word has likeness_score == number_letters:
		You won
	else:
		Pause 10 seconds and open terminal again

```
![Flowchart](minigame_flowchart.png)
