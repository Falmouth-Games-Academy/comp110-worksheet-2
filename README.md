# comp110-worksheet-B
Base repository for COMP110 worksheet B

## The aim of this pseudocode is to show the process of selecting a secret word from a string of other words. Which has been selected by another user. 

 

attemptNo – 4 

wordLength – Number of letter in the word 

secretWord – The secret word input 

success – False 

 

print (“Please guess the”, wordLength, “letter word.”) 

 

while the attempt value is > 0 AND success = False 

 

Likeness <- 0 

guess <- get the user Input 

if secretWord is eqaul to guess [i] 

Likeness += 1 

       if Likeness is == to the wordLength 

              Success <- 

       Else: 

              print(“you got a likeness of”, likeness) 

       Attempts -=1 

       If success == TRUE: 

              print(“you guessed correctly”)