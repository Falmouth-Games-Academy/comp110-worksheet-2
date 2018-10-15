attemps <- Set to 0
likeness <- Set to 0
correct <- Set to False
wordList <- store a list of words for the player to guess
answer <- get a random word from the list
while correct is False or attempts is less than 4
	playerInput <- request input from user (and check if it's a valid input)
	attempts <- add one
	if playerInput is equal to answer
		correct <- set to True
	else if playerInput is not equal to answer
		for each letter from playerInput at position i that is in answer at position i
			likeness <- add one
		end for loop
		print likeness to the screen
	end if statement
	likeness <- Set to 0
end While
if correct is equal to True
	print "congratulations" message
else
	print "failure" message
end if
end program