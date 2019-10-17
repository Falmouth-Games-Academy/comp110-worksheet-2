# COMP110 Worksheet 3: Flowcharts and pseudocode

This is the base repository for COMP110 Worksheet 3.

```
#Comp110 Worksheet.

listOfWords = generate random list of words with similar characters and same word length
correctWord = pick random answer from list

userGuesses = 4
done = False

while done == False do
    print listOfWords
    guess = ask user for guess
    if userGuesses = 0 then
	done = True
	print sorry you have no more attempts
    if guess == correctWord then
	done = True
	print correct answer
    elif guess != correctWord then
	print guess is wrong
	likeness = characters in same position within correctWord and guess
	print likeness
	userGuesses = userGuesses - 1
```

Flowchart:
!(Flowchart)[Worksheet3-Comp110 Flowchart.png]
