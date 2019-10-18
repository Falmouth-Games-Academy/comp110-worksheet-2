# COMP110 Worksheet 3: Flowcharts and pseudocode

This is the base repository for COMP110 Worksheet 3.

Fork this repository, and edit `README.md` to show your pseudocode solving the worksheet task. Tip: use triple backticks to preserve spacing, e.g.:

```
has_completed_game = false

chosen_word = choose first word
remove chosen_word from possible answers

while has_completed_game == false	
	if(chosen_word == secret answer)
		has_completed_game = true
	else
		list(chosen_word)
		if(amount of matching letters == 0)
			remove possible answers which have any of the same matching letters as chosen_word
		else
			remove possible answers which have less matching letters that match chosen_word
		
		chosen_word = choose next word from remaining possible answers

//game complete		
```
