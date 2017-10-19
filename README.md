# comp110-worksheet-B (SCOTT CALVERT)
Base repository for COMP110 worksheet B

First level of abstraction

1)select random word
2)prompt the user that they only have a total of 5 guesses 
3)prompt user to input guess

4)match guess with randomly choosen word 

5)if guess matches random word 
	6)print "access granted"
	
7) if guess is incorrect then 
	8) identify which letters are the same in both the guess and random word 
	9) print "you have x out of x correct"
	
	10) also print "you have 4 guess left"
	
11) repeat loop until guess = randon word or no more guess remain#

-------------------------------------------------
Second level of abstraction


import english language dict
import random_get_word ()

int randon_get_word[] #store as an array

print "Please input password"
print "For security reasons you are only allowed 5 password attempts"

password = random_get_word()

for i = (5)
   guess = raw_input
 
   if guess != password 
     print "access denied"
     for letter in password 
	 compare letter(0) == password 
     print number of matching letters
	 print "please input password"
	 
   elif guess = password
      print "Acess Granted"
      end 
	  
	else 
	  print error
