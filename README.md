# COMP110 Worksheet 3: Flowcharts and pseudocode

![The flowchart](https://raw.githubusercontent.com/JD233113/comp110-worksheet-3/master/flowchart.PNG)

```
previouslyGuessed[]

x = 1
while x == 1:
   select word
   
   if likeness > 0:
      closestGuess = word
      closestGuessLikeness = likeness
      add word to previouslyGuessed[]
      x = 0
   else:
      select next word
      
for word in available words:
   if word is in previouslyGuessed[]:
      skip word
   else:
      chance = 0
      split word into letters
      split closestGuess into letters
   
      for letter in word:
         if letter(n) in word == letter(n) in closestGuess:
            chance += 1
         
      if chance >= closestGuessLikeness:
         select word
         if likeness > closestGuessLikeness:
            closestGuess = word
            closestGuessLikeness = likeness
            add word to previouslyGuessed[]
         else:
            chance = 0
```
