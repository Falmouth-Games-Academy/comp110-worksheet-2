# COMP110 Worksheet 3: Flowcharts and pseudocode

This is the base repository for COMP110 Worksheet 3.

Fork this repository, and edit `README.md` to show your pseudocode solving the worksheet task. Tip: use triple backticks to preserve spacing, e.g.:

```
//This algorithm relies on eliminating all words that cannot be the correct one
//until only the correct word is left. It does this by taking in all of the words at the start,
//choosing the first word to test, then gets its score, and eliminates all words that dont have that score
//when compared to the chosen word. It usually only takes 3 iterations before the code is solved

function getCommon(word1, word2):
    //checks how many letters there are in common between the two parameters
    common = 0
    for i=0 to word1.length
        if word1[i] == word2[i]:
            common += 1
    return common

wordlist = input("Please input all of the words on the screen: ").split(" ")
wordLength = wordlist[0].length

guesses = 0
while guesses < 4:
    guess = wordlist[0]
    print(guess)
    if input("Is it correct? [Y/N] ") == "Y"
        break
    guessAmount = int(input("How correct was I? "))
    newWordList = []
    for every word in wordlist:
        if getCommon(guess, word) == guessAmount:
            newWordList.append(word)
    wordlist = newWordList
```

Here is the image of the flowchart: ![Flowchart](https://i.imgur.com/ARuv3dh.png)
