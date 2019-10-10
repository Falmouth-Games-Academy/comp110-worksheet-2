# COMP110 Worksheet 3: Flowcharts and pseudocode

This is the base repository for COMP110 Worksheet 3.

Fork this repository, and edit `README.md` to show your pseudocode solving the worksheet task. Tip: use triple backticks to preserve spacing, e.g.:



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
