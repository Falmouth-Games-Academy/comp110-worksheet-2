# comp110-worksheet-B
Base repository for COMP110 worksheet B

Submission of: Paul Rauca

# Pseudocode

	//Convention: '//' will be used to denote comment lines

	secret_word <- random word
	player_guess <- input word

	//NOTE 1: the following while loop can be safely omitted if we
	//consider both words (secret_word and player_guess) to be 
	//of the same length by default

	while length of player_guess is not equal to length of secret_word do:
		player_guess <- input word
	end while

	attempts <- 1
	word_was_guessed <- false
	similarity <- 0

	while attempts <= 5 or word_was_guessed is false do:
		for each letter in secret_word
			if player_guess[letter] = secret_word[letter] then:
				similarity <- similarity + 1
			end if

		print 'Similarity of words is' + similarity

		if similarity = length of secret_word then:
			word_was_guessed <- true
		end if

		if word_was_guessed = false then:
			player_guess <- input word

			//See NOTE 1 regarding the while loop below

			while length of player_guess is not equal to length of secret_word do:
				player_guess <- input word
			end while

			attempts <- attempts + 1
			similarity <- 0
	end while

	if word_was_guessed = true then:
		print 'Perfect match! Accessing terminal...'
	else
		print 'TERMINAL LOCKED'
		print 'PLEASE CONTACT AN ADMINISTRATOR'
	end if

# Flowchart

![Fallout 4 minigame flowchart](https://github.com/Powll/comp110-worksheet-B/blob/master/F4_minigame.png)


