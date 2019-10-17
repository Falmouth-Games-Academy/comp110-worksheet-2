# COMP110 Worksheet 3: Flowcharts and pseudocode

This is the base repository for COMP110 Worksheet 3.

Fork this repository, and edit `README.md` to show your pseudocode solving the worksheet task. Tip: use triple backticks to preserve spacing, e.g.:

```
your
   pseudocode
      here
	  Pseudocode:
	  import time
	  guesses = 4
	  output 4 words which are similar in spelling along with random characters from the alphabet including special characters(!,",£,$,%,^,&,*,<,>,?,/,;,:,',@,#,~,[,{,],},_,-,+,=,.,¬,`,|,\)
	  allow user to interact with the characters with their mouse
	  
	  define function called mouse_over_event:
		output character hovered over into the guess input box
	
	  define function called mouse_click_event:
		input characters/word clicked on as the player's guess
		reduce guess amount by 1
		
	  define function called likeness_to_password:
		X is a number based on the amount of letters that are in the same order and are the same letter		
		if guess characters were in the same order and the same letter:
			output "likeness_to_password: X"
			
	  define a function called correct_password:
		output "You guessed the password!"
		take player to menu of terminal
	
	  define a function called secret_string:
		deletes 2 incorrect answers
		guesses is reset to 4
	
	  if player hovers over characters/word:
		call function mouse_over_event()
	
	  if player clicks on characters/word and guess is not equal to password:
		call function mouse_click_event()
		call function likeness_to_password()
		
		elif guesses = 0:
			end minigame
			
		elif player clicks on secret_string:
			call function mouse_click_event()
			call function secret_string()
		
	  else:
		call function correct_password()
```
