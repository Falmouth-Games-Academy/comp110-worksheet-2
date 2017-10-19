# comp110-worksheet-B
Base repository for COMP110 worksheet B

<br />var random_words = random words number of which is 8
<br />*random_words have similar beginnings or endings*
<br />var random_characters = randomly generated any characters
var guesses = 0

Display random_words and random_characters on screen 
Give user ability to click on random_words and random_characters
chosen_word = system randomly chooses one word from random_words

while guesses < 4
   if user doesn't click on chosen_word
      guesses = guesses + 1
      display how many characters have the same position as the chosen_word
      user has another chance of choosing a word or character
   else
      display another screen saying something funny or clever
      after clicking any button bring user to main menu where he can try once more
   end if
end while

if guesses == 4
   print "Unfortunately, but you have reached maximum attempts. Try another time"
   display main menu to give the user an opportunity to start again
end if
