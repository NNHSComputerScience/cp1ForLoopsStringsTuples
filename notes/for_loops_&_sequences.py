# For Loops and Sequences Notes
# for_loops_&_sequences_starter.py

# SEQUENCE = an ordered list of element
#   For example: range(5) is an ordered list of numbers: 0,1,2,3,4

# ELEMENT = a single item in a sequence

# So far we have used range() to make sequences.
#   Another type of sequence is a string,
#   which is a specific order of letters in a sequence.
#       For example: "hello" != "olleh"

# ITERATE = to step through a sequence, in order, and one at a time

# FOR LOOP = iterates through a sequence and executes the body of
#                           loop for each element in the sequence

# So, we can iterate through a string using a for loop just like a range:
for i in "Hello":
    print(i)

word = "World"
for letter in word:
    print(letter)


# CHALLENGE #1: Secret Message - Ask the user for a message and then display
#       the message with each letter displayed twice.
#       Ex) message = "great"  output = "ggrreeaatt"
message = input("\nPlease enter a message: ")
for letter in message:
    print(letter*2, end="")
print()

# Quick Question: What would display?
string = "Ha"
for letter in string:
    print(string,end="")
print()

# ANSWER: HaHa


# The len() function:
#   Used to count the number of elements in a sequence.
word = "Bananas"
print(len(word))


# Practice: Save your first name to the variable 'name', and then display
#   how many letters are in your first name.
name = "Geoff"
print(name, "is", len(name), "elements long")

# Practice 2: Now do the same thing for your first and last name.
#   Be sure to put your first and last in the SAME string.
#   What did you learn about the len() function?
print("\nGeoff Schmit is", len("Geoff Schmit"), "elements long.")
print()

# ANSWER: len() counts the spaces! (It counts *every* character in the string)

# CHALLENGE #2: Ask the user for their last name.
#       Tell the user the number of letters in their last name.
#       Then, determine if the user's name includes the letter "A" or not.
#       If they do, display "Awesome, you have an A!"


# CHALLENGE #3: Password
#       Ask the user for a password. It must be at least 6 characters long,
#       and it must contain a '!' or a '$' sign. If they give a valid password
#       display "Valid Password", otherwise display "Invalid Password".


# Adv. CHALLENGE: Can you use a while loop to keep asking for the password
#       until the user enters it in the correct format?


input("\nPress enter to exit.")
