# COMP110 Worksheet 3: Flowcharts and pseudocode
![flowchart](/Worksheet3.png)

```
password = random word selected from list
attempts = 5
player_guess = users word selection
WHILE attempts > 0
	likeness = 0
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
	player_guess = users guess with similar letter positions equal to likeness
	
```
