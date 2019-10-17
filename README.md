# COMP110 Worksheet 3: Flowcharts and pseudocode

This is the base repository for COMP110 Worksheet 3.

Fork this repository, and edit `README.md` to show your pseudocode solving the worksheet task. Tip: use triple backticks to preserve spacing, e.g.:
## Pseudocode
```
start algorithm

guessed = false
guesses = 0

pick a word
guesses ++
if correct
	guessed = True
else
	while guessed == false and guesses <= 4
		for each (letter in selected word)
			compare with previous guesses
			if not possible match
				ignore letter
			else
				store letter in memory
				
		pick a word with possible matching letters
		guesses ++
		if correct
			guessed = True

if guessed == True
	if guesses == 1
		print "I won with 1 guess!"
	else 
		print "I won with " + guesses + " guesses!"
else
	print "i lost :("
		
end algorithm
```

## Flowchart

![Flowchart](\FalloutMiniGameFlowchart.png)
