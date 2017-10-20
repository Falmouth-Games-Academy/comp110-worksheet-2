# comp110-worksheet-B
Base repository for COMP110 worksheet B

PROGRAM Terminal
Init Terminal
Guesses = 4
Correct Word = Marks
Words = Starks, Stake, Helps, Empty, Marks

Print “You have 4 guesses”
Guess = Input Guess


If chosen word has no characters right 
guessesTaken = guessesTaken +1
Then 
Print “0/5 characters correct”

If chosen word has 1 characters right 
guessesTaken = guessesTaken +1
Then 
Print “1/5 characters correct”

If chosen word has 2 characters right 
guessesTaken = guessesTaken +1
Then 
Print “2/5 characters correct”

If chosen word has 3 characters right 
guessesTaken = guessesTaken +1
Then 
Print “3/5 characters correct”

If chosen word has 4 characters right 
guessesTaken = guessesTaken +1
Then 
Print “4/5 characters correct”

If chosen word has all characters right 
guessesTaken = guessesTaken +1
Then 
Print “5/5 characters correct”

If Word is correct
Then Print "Correct!"
END

If guessesTaken = 4
Then print “Init Lockout”

END
