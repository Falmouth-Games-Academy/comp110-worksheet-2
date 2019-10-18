# COMP110 Worksheet 3: Flowcharts and pseudocode

This is the base repository for COMP110 Worksheet 3.

Fork this repository, and edit `README.md` to show your pseudocode solving the worksheet task. Tip: use triple backticks to preserve spacing, e.g.:

![Flowchart](https://raw.githubusercontent.com/KalvinMalloch/comp110-worksheet-3/master/Worksheet%203%20Flowchart.png)


START

READ letter_length, words, correct_word

guesses = 5
solved = false

WHILE guesses > 0 AND solved == true
      SELECT word from RANDOM
      guess = word_chosen
      IF word_chosen = correct_word THEN
            solved = true
      ELSE
            guesses = guesses - 1
            simularity = amount of matching letters between word_chosen and correct_word
            remove word_chosen from words list
            PRINT word_chosen
            PRINT simularity
END
