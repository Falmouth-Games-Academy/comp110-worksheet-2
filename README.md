# COMP110 Worksheet 3: Flowcharts and pseudocode

This is the base repository for COMP110 Worksheet 3.

Fork this repository, and edit `README.md` to show your pseudocode solving the worksheet task. Tip: use triple backticks to preserve spacing, e.g.:

```
program start

tries = 4
previous_guesses = list
word_list = list
correct_letter = list
hacking_interface = text on screen display
likeness = find 'likeness' value in 'hacking_interface'

open 'hacking_interface'
write string values found in 'hacking_interface' to 'word_list'
convert all items in 'word_list' to lists

while tries != 0:

	read 'correct_letter' list
	compare 'correct_letter' list to all items in 'word_list'
	guess = select value with the most items in common.
	read 'hacking_interface'
	if text 'success!' in 'hacking_interface':
		print ("Congratulations!")
		end()

	else:	
		tries = tries - 1
		read 'likeness' value
		if likeness =< 1 
			assign likeness value to 'guess'
			split 'guess' string into list
			add 'guess' to 'previous_guesses' list
			remove 'guess' from 'word_list'
			search 'previous_guesses' for item with likeness > 0
			if items are found:
				compare each item
				for every value that is the same, and in the same position, add this value to 'correct_letter' list in same position. Fill unknown values with a space
			else:
				do not compare.
		if likeness >= 0:
			add 'guess' to 'previous_guesses' list
			remove 'guess' from 'word_list'

```

![Worksheet 3 Flowchart](https://raw.githubusercontent.com/TrainerIsaac/comp110-worksheet-3/eb6defe02125ef300d108522c464e6e41eda4e9f/Worksheet%203%20Flowchart.png)
