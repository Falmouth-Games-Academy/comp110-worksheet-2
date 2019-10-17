# COMP110 Worksheet 3: Flowcharts and pseudocode
## Flowchart

![Flowchart](/Fallout_Hacking_Manager.png)


## Pseudocode
```
# get_random_word() is an external aspect 
# of the program and is supplied to this one

random_word = get_random_word()
word_length = length(randomWord)
word_attempt = []

alphabet = ["a", "b", "c", ...]

correct_counter = 0
crash_counter = 0
is_solved = false

for i in range(0, word_length)
    word_attempt[i] = (alphabet[0], 0, false)

while is_solved is false
    for x in range(word_length)
        if crash_counter equals word_length:
            is_solved = true
            output "Error, random word given does not contain a letter of the phonetic lower case alphabet"
            continue

        if word_attempt[x][0] equals alphabet[25]:
            crash_counter += 1
            continue

        if correct_counter equals word_length:
            is_solved = True

        if word_attempt[x][2] is true:
            continue

        if word_attempt[x][0] equals random_word[x]:
            word_attempt[x] = (alphabet[word_attempt[x][1]], word_attempt[x][1], true)
            correct_counter += 1

        else:
            word_attempt[x] = (alphabet[word_attempt[x][1] + 1], word_attempt[x][1] + 1, false)
```
