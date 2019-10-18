# COMP110 Worksheet 3: Flowcharts and pseudocode

https://raw.githubusercontent.com/Miguel-M-Oliveira/comp110-worksheet-3/master/flowchart.png

```
likeness = 0
solved = false
x = 1
y = 1

def compare(a,b)
   while x = 1 to n
      if a.letter(x) = b.letter(x) then
         likeness = likeness + 1
      endif
      x = x + 1
   endwhile
print "likeness: " & likeness

while y = 1 to 4
   print "enter guess"
   read guess
   if guess = answer then
      solved = true
      break
   else compare(guess, answer)
   endif
   y = y + 1
   print "you have " & 5 - y & " guesses remaining"
endwhile

if solved = true then
   print "Congratulations! You got it right!"
else print "No more tries available. Game over."
endif
```
