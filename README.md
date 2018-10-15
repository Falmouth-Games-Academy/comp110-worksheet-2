# comp110-worksheet-B
Base repository for COMP110 worksheet B


##basic word similarity guessing pseudocode

##the idea is that one person enters the secret word and then gives the device to someone else to guess

secretWord <- get input
wordLength <- length of 'secretWord'
attempts <- 10
success <- FALSE

print("guess the", wordLength, "letter word")

while attempts is greater than 0 AND success is FALSE:
>	likeness <- 0
>	guess <- get input
>	for i in range wordLength:
>>		if secretWord[i] equal to guess[i]:
>>>			likeness += 1
> 	if likeness equal to wordLength:
>>		success <- TRUE
>	else:
>>		print("you got a likeness of",likeness)
>	attempts -=1

if success == TRUE:
>	print("you win")
else:
>	print("you lose")