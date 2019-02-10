

print("Dansku\nEats")       # type \n to line break your string

phrase = "Dansku Eats"      # variable
print(phrase)               # print variable

print(phrase + " is cool.")     # concatenation; print a variable + a string

# strings with various functions
print(phrase.lower())       # will print phrase in console as lower case
print(phrase.upper())       # will print phrase in console in caps
print(phrase.title())       # will print phrase in console title case

# strings and booleans
print(phrase.isupper())     # is not upper, returns false
print(phrase.islower())     # is not lower, returns false
print(phrase.istitle())     # is title case, returns true
print(phrase.upper().isupper())     # use .upper function to return true

print(len(phrase))          # find the length of a variable

print(phrase[0])            # square brackets can access a letter in your phrase
print(phrase[-1])           # type -1 to loop back and grab the last letter in the phrase

print(phrase.index("D"))    # .index function for the location of letter. "D" returns 0

print(phrase.replace("Dansku", "Daniel"))   # replace function
