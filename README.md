# COMP110 Worksheet 3: Flowcharts and pseudocode

This is the base repository for COMP110 Worksheet 3.

Fork this repository, and edit `README.md` to show your pseudocode solving the worksheet task. Tip: use triple backticks to preserve spacing, e.g.:

```

length = letters per word
count = number of words
guesses = 4

WHILE running
  
  IF guesses > 0

    list = remaining words
    word = first word in list
  
    IF word is correct
      WIN
  
    ELSE
      likeness = number of correct characters
      FOR each word in list
        IF likeness of word in list != likeness of word
          REMOVE current word from list
      REMOVE word from list
      guesses - 1

  ELSE
    LOSE

```

![flowchart](https://github.com/DanielNeale/comp110-worksheet-3/blob/master/Fallout%20Mastermind.png)
