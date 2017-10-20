# comp110-worksheet-B
Base repository for COMP110 worksheet B
Attempts = 5
Random_Words = 10
word_length = 5
Answer == 1 Random_Words


Likeness
	Number of correct letters in choosen word
		correct answer compared to choosen word
			letters that are correct = n 
			print(n + " out of " + word_length)

Open Terminal 
	if Attempts > 0 
		display Random_Words
			if guess == Answer
				then print ("Access Granted")
				display next screen
			if else guess != Answer 
				print("wrong answer")
				print Likeness
				Attempts -1 
			else Attempts == 0 
				lock terminal 
				print ("Access Denied")
