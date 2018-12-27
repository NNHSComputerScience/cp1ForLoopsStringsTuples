# Pizza Slicer
# Demonstrates string slicing
#  To slice, use the format [ starting index value : ending index value : step]

word = 'pizza'

# Note: A slice will always include the first index value specified and
#       exclude the second index value specified

print(word[3 : 5]) # forwards slice – za

print(word[-3 : -6 : -1]) # backwards slice - zip

# slicing shorthand
#   we can omit values in a slice to represent the start and end of a word

# slice from index 1 to end of the word - izza
print(word[1 : ])

# slice from the beginning of the word to the second to last character - pizz
print(word[ : -1])

# slice the entire word - pizza
print(word[ : ])


# this is useful for making a copy:
word2 = word[:]
print(word2)


# the step value doesn't have to be +/- 1 - pza
print(word[0 :: 2])

# IndexError: string index out of range
#print(word[5])

# invalid slice returns an empty string
print("**" + word[5:6] + "**")

print(
'''
  Slicing 'Cheat Sheets':
  
  FORWARDS:
     0   1   2   3   4   5
   +---+---+---+---+---+
   | p | i | z | z | a |
   +---+---+---+---+---+
-6  -5  -4  -3  -2  -1

''')
 
# CHALLENGE: Write a program that allows the user to slice the word 'pizza'
#           as many times as they want by getting the beginning and ending 
#           index values for the slice.
word = 'pizza'

print ("Enter the beginning and ending index for your slice of 'pizza'...")
 
        
input('\n\nPress the enter key to exit.')  































