# comp110-worksheet-B
Base repository for COMP110 worksheet B
Attempts = 5
Random_Words = 10
Likeness = number of correct characters in the correct place of choosen word against the correct Answer
Answer == 1 Random_Words

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
