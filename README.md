###Flowchart diagram of the game.

![Flowchart](https://github.com/JVFalmouth/comp110-worksheet-3/blob/master/Hacking%20Diagram.png)

###Pseudocode
```
start

word-list <- list of words from terminal

likeness <- 0
lastword <- ""
guesses <- 4

for word in word-list:
    if likeness == compareLikeness(lastword, word):
        likeness <- inputWordAndGetLikeness(word)
        lastword <- word
	guesses --
        if word == correct answer:
	    output "you win!"
            end
	endif
	if guesses = 0
	    output "you lost!"
	    end
	endif
    endif
endfor

end
```
