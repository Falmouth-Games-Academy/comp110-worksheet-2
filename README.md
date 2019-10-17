# COMP110 Worksheet 3: Flowcharts and pseudocode

This is the base repository for COMP110 Worksheet 3.

Fork this repository, and edit `README.md` to show your pseudocode solving the worksheet task. Tip: use triple backticks to preserve spacing, e.g.:

![Flowchart](https://github.com/JIMBLYB/comp110-worksheet-3/blob/master/Fallout4MinigameFlowchart.png "Flowchart")

```
guesses = 3
running = True
word = null

list = ALL WORDS
word = FIRST WORD IN list

WHILE True:
   
   IF word IS correct:
      WIN
   
   ELSE IF guesses == 0:
      LOSE
   
   ELSE IF guesses >= 1:
      FOR EACH word IN list:
         IF likeness_of_word IS NOT EQUAL TO likeness:
            REMOVE word FROM list
            
      word  = FIRST WORD IN list
      guesses = guesses - 1     
```
