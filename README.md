# comp110-worksheet-B
Base repository for COMP110 worksheet B

First level of abstraction

#select randomly choosen word
prompt the user that they only have a total of 5 guesses 
prompt user to input guess

match guess with randomly choosen word 

if guess matches random word 
	print "access granted"
	
if guess is incorrect then 
	identify which letters are the same in both the guess and random word 
	print "you have x out of x correct"
	
	also print "you have 4 guess left"
	
repeat loop until guess = randon word or no more guess remain#

-------------------------------------------------
Second level of abstraction


import english language dict
import random_get_word ()

int randon_get_word() #store as an array

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
	 print "please re input password"
	 
   elif guess = password
      print "Acess Granted"
      end 
	  
	else 
	  print error
