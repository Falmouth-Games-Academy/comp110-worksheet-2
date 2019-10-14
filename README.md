# COMP110 Worksheet 3: Flowcharts and pseudocode

This is the base repository for COMP110 Worksheet 3.

Fork this repository, and edit `README.md` to show your pseudocode solving the worksheet task. Tip: use triple backticks to preserve spacing, e.g.:

```
n = word length
likeness = input likeness
guess = input guess
while likeness != n
	likeness = input likeness
	for letter in guess
		if correctword[letter] != nothing
			guess[letter] = correctword[letter]
		else
			guess[letter] = input
		endif
	loop
	if likeness >= lastlikeness
		for letter1 in guess
			for letter2 in lastguess
				if letter1 = letter2
					correctword[letter1.position] = letter1
				endif
			loop
		loop
	endif
	lastlikeness = likeness
	lastguess = guess
endwhile		
```
