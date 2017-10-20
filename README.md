# comp110-worksheet-B
Base repository for COMP110 worksheet B

# Psuedocode for minigame word comparison section
```
# Snippet info: Checks similarity between a user-selected word and a preset secret word
# Ignores characters beyond the length of the shorter word.
# Todo: What should happen if user_word is longer than secret_word, but still equal up to that point?
# Todo: Request clarification from contractor

# Obtain minigame strings
variable user_word = get_minigame_user_word()
variable secret_word = get_minigame_secret_word()

# Use the length of the shortest string, to avoid overflowing one of them in our loop
variable shortest_num_characters = get_minimum(user_word.length(), secret_word.length())

# Check both strings for matching characters until the length of the shortest string(s) is reached
variable likeness = 0

for index in range(0, shortest_num_characters):
    if user_word.get_character(index) == secret_word.get_character(index):
        likeness = likeness + 1
    endif
endfor

# Display result to user
if likeness == secret_word.length():
    display_message("Success! Likeness: " + to_string(likeness))
else:
    display_message("Failure! Likeness: " + to_string(likeness))
endif
```

# Flowchart
![alt text](https://i.imgur.com/n3U34es.png "I just realised 'swimlanes' exist because it's a 'flow'chart")
