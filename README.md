# comp110-worksheet-B
Base repository for COMP110 worksheet B

```
enter terminal

wordArray <- List of words
secretWord <- randomly select word form wordArray
attampts <- 4
compleat <- false

Display all words form wordArray and add random charitors inbetween words all as sellectable buttons

while attampts >= 0:

	Wait for user to sellect and submit a word
	guesedWord <- submited word
	
	likeness <- 0
	
	for n <- 0; n < secretWord Length; n++:
		if secretWords letter n == guessedWord letter n:
			likeness <- likeness + 1
		end if
	end for
	
	if matchCount == likeness:
		break while
		compleat <- true
	else
		display likeness
		attampts <- attamps - 1
	end if
		
end while

if compleat == false:
	lock terminal
end if

exit terminal
```

<img src="https://github.com/gizzmo123456/comp110-worksheet-B/blob/master/minigame.png?raw=true" />
