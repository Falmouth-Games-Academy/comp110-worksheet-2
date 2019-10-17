# COMP110 Worksheet 3: Flowcharts and pseudocode

![Flowchart](/Flowchart.PNG)

```

START PROGRAM

correctword is set as list

answer = False
numberofguesses = 4

while numberofguesses > 0 AND answer = False
  playeranswer = player input
  compare lists to check if playeranswer is correctword
  difference = the number of letters that are correct to the correctword list

  if playeranswer list != correctword list
    numberofguesses -1 
    output "You did not guess the correct answer, you got " + difference + " letters correct"
  if playeranswer = previous playeranswer
    output "You have chosen and answer that you have already picked before, you will get to pick the answer again"
    numberofguesses +1
  if numberofguesses is 0
    output "You haven't picked the correct answer and you have run out of questions"
    END PROGRAM	
  else
    "You got the answer correct! Well done! You answered it in " + numberofguesses + "!"
    numberofguesses set to 0
    answer set to True
  end if satement

end while

END PROGRAM

```
