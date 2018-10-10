# comp110-worksheet-B


## Pseudocode:

```
Create RWord <- a random word with x number of letters
Create Tries <- 0 (current number of user attempts)

Display list of random words, including RWord

While Tries is <5:
	Allow user to select word from list
	If user's word is the same as RWord:
		Display "success! Well done!" and end program
	Else:
		Add 1 to Tries and calculate identical letters 
	End if
	If Tries is >4:
		Display "Unfortunately, you did not succeed" and end program
	Else:
		Display number of identical letters and number of remaining attempts
	End if
End while
```

## Flowchart:

<img src="https://i.imgur.com/FDLYd78.png" />
