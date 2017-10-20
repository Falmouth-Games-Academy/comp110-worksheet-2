# comp110-worksheet-B
Base repository for COMP110 worksheet B

int MAX_GUESSES = 4
string TO_GUESS = "Word to guess"
bool won = False
print("Guess the " + TO_GUESS.length() + " letter word")
print("_" * TO_GUESS)
for(int y = 0; y < MAX_GUESSES; y++)
{
  int counter = 0
  bool chk = True
  while(chk)
  {
    string ans = input()
    if (ans.length() != TO_GUESS.length())
    {
      print("Please enter a " + TO_GUESS.length() + "word")
      chk = False
    }
  }
  for(int x = 0; x < ans.length(); x++)
  {
    if (ans[x].upper() == TO_GUESS[x].upper())
    {
      counter++
    }
  }
  if (counter==TO_GUESS.length())
  {
    won = True
  }
  else
  {
    print("Bad luck, you got " + counter + " right")
  }
}
if (won)
{
  print("Congratulations you guessed the word: " + TO_GUESS)
}
else
{
  print("Unlucky, maybe next time")
}
