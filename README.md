# comp110-worksheet-B
Base repository for COMP110 worksheet B
![FlowChart](Flowchart.png)

SecretCode ← Generated Random Number;
UserGuess ←  User's Selected Guess;

If (SecretCode == UserGuess)
{
	Output << Correct;
	Output << Terminal Unlocked;
	Unlock Terminal;
	End Program;
}
Else
{
	numberCorrect ← 0;
	numberOfLetters ← 0;
	For each letter in UserGuess { 				► i = letter number
		if (SecretCode[i] == UserGuess[i])
		{
			numberCorrect ++;
		}
		numberOfLetters ++;
	}
	likeness ← (numberCorrect / numberOfLetters);
	Output << likeness (as fraction) Correct; 
}