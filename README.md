# COMP110 Worksheet 3: Flowcharts and pseudocode

This is the base repository for COMP110 Worksheet 3.

Fork this repository, and edit `README.md` to show your pseudocode solving the worksheet task. Tip: use triple backticks to preserve spacing, e.g.:

```
password = random word selected from list
attempts = 5
WHILE attempts > 0
	likeness = 0
	player_guess = users word selection
	for i in password length
		if player_guess == password
			print (Access Granted)
			End while
	
		else if player_guess != password
			if player_guess[i] == password[i]
				likeness = likeness + 1
				i = i + 1
			else 
				likeness = likeness
				i = i + 1
	attempts = attempts - 1
```
