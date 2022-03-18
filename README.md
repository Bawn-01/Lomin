# LOMIN
This is a pro PROgramming language, only for use of pro man

# TODO

- while loops
- if statement functionalities
- for loops (maybe)
- booleans

# What is it intended for?
This language is intended for no industrial use, mainly it was intended for me to learn how to make a programming language and shouldn't
be a big enough project that would take up all my mindspace, but that last intention is not there anymore but I still dont intend it for
industrial use.

# What I hope to have lomin look like
I hope lomin in the future will be used for small projects, I want it to be able to do data and file management in specific but
I dont think it will be a big emphasis. The language I hope though aswell will be able for terminal games and what not, 
maybe graphics, but if so it won't be any good graphics.

# Currently Working on
> if statement functionalities

# Example File

For Example files I would recommend for now trying to do things like this
```
var ansOne = "pro"
var ansTwo = "noob"
var amsThree = "sup"

println("What am I?")
var qOne = input
println("What are you?")
var qTwo = input
println("What should the standard greeting be?")
var qThree = input

if qOne == ansOne
println("Question One, Correct!")
end

if qTwo == ansTwo
println("Question Two, Correct!")
end

if qThree == amsThree
println("Question Three Correct!")
end

```
This teaches you what we have right now.

# Instructions for use.
### STEP ONE
Make a new folder and copy the std.py library into it.

### STEP TWO
Make a new file call it test.ln (.ln being the file extension)

### STEP THREE
go into the std.py file and at the bottom of the file you will see something like:
```
compile("test.ln")
```
Compile is a function containing the lexer and it needs a file to scan, where it says ```test.ln``` is your file (change this if your file isn't test.ln)

### STEP FOUR
Write your lomin code in the ```test.ln``` file you created 

### STEP FIVE
Run the std.py, it is recommended that you run this in the terminal and not run it directly from the file explorer.


