def getCommon(word1, word2):
    common = 0
    for i in range(len(word1)):
        if word1[i] == word2[i]:
            common += 1
    return common


wordlist = input("Please input all of the words on the screen: ").split(" ")
wordLength = len(wordlist[0])
guesses = 0
while guesses < 4:
    guess = wordlist[0]
    print(guess)
    if input("Is it correct? [Y/N] ") == "Y":
        break
    guessAmount = int(input("How correct was I? "))
    wordlist = [x for x in wordlist if getCommon(guess, x) == guessAmount]