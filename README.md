# COMP110 Worksheet 3: Flowcharts and pseudocode

This is the base repository for COMP110 Worksheet 3.

Fork this repository, and edit `README.md` to show your pseudocode solving the worksheet task. Tip: use triple backticks to preserve spacing, e.g.:

```

length = letters per word
count = number of words
guesses = 4

WHILE running
  
  word = first word on list
  
  IF word is correct
    WIN
  
  ELSE
    likeness = number of correct characters
    FOR each word in the list
      IF likeness of current word != likeness of word
        REMOVE current word from list
    REMOVE word from list
    guesses - 1

```

![flowchart](https://github.com/DanielNeale/comp110-worksheet-3/blob/master/Fallout%20Mastermind.png)
