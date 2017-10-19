# comp110-worksheet-B
Base repository for COMP110 worksheet B

<br />var random_words = random words number of which is 8
<br />*random_words have similar beginnings or endings*
<br />var random_characters = randomly generated any characters
var guesses = 0

<br />Display random_words and random_characters on screen 
<br />Give user ability to click on random_words and random_characters
chosen_word = system randomly chooses one word from random_words

<br />while guesses < 4
   <br />if user doesn't click on chosen_word
      <br />guesses = guesses + 1
      <br />display how many characters have the same position as the chosen_word
      <br />user has another chance of choosing a word or character
  <br /> else
     <br /> display another screen saying something funny or clever
     <br /> after clicking any button bring user to main menu where he can try once more
  <br /> end if
end while

<br />if guesses == 4
  <br /> print "Unfortunately, but you have reached maximum attempts. Try another time"
   <br />display main menu to give the user an opportunity to start again
end if
