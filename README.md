# comp110-worksheet-B
Base repository for COMP110 worksheet B


![It's a FLOWCHART! Beware the ED! :D](https://github.com/TMGilchrist/comp110-worksheet-B/blob/master/Fallout%20minigame%20flowchart.png)


```

wordLength = 5

guesses = 0
score = 0

secretWord = get random word where characters = wordLength

#Player has four attempts to guess the word
while guesses < 4
	
  userGuess = get user input

  #Game finishes if user guess word correctly
  if userGuess == secretWord
    print "you win"
    break

  #For each letter in the secret word, compare with the player's guess	
  else
    for i in range 0 .. length of secretWord
      if secretWord(i) == userGuess(i)
        increment score

    print "Likeness score is" + score
    score = 0
    increment guesses
		
```
