# Intro to for loops notes
#   counting with the range() function
 
# counting with while loops:
# CHALLENGE: Print 'Hello, world.' 10 times using a while loop
counter = 0
while counter < 10:
    print("Hello, world.")
    counter += 1

# FOR LOOP - repeats the body of the loop *for* a certain number of times,
#               instead of based on a condition

# Print "Hello World" 10 times using a for loop
input("\nPress enter to begin.")
for num in range(10):   # range(n) creates an n-digit sequence [0-n)
    print("Hello, world.")  # body runs for each element in the sequence

# Display numbers 1-10 using a for loop
input("\nPress enter to begin.")
for num in range(1, 11):    # range(x, y) creates a sequence [x, y);
                            #   includes x, excludes y
    print(num)              # num is a variable whose value is each element
                            #   in the sequence, one at a time
print(num)  # the variable num exists outside the for loop (its value is 10)

# Use i for your counter variable (convention used by many programmers,
#   originating from mathematics)
#   Display numbers 1-20
input("\nPress enter to begin.")
for i in range(1, 21):
    print(i)       # often we use i in the body, but we don't have to

# Controlling range() in more detail
#   Count 11-20
input("\nPress enter to begin.")
numbers = range(11, 21)
for i in numbers:
    print(i)

# Controlling loop increment value
#   Count by 2's
input("\nPress enter to begin.")
# range(x, y, z) creates a sequence [x, y) where each element is incremented
#   by z
for i in range(0, 21, 2):
    print(i)


# Practice Challenges:
#   Increment challenge (3 to 99 by 3s)
input("\nPress enter to begin.")
for i in range(3, 100, 3):
    print(i)

#   Counting Down Challenge (10 to -10 by 2s)
input("\nPress enter to begin.")
for i in range(10, -11, -2):
    print(i)


# Application Challenges:

# Bug Collector Program -
#   A bug collector collects bugs every day for 7 days. Write a program that
#   keeps a running total of the number of bugs collected during the 7 days.
#   The loop should ask for the number of bugs collected for each day,
#   and when the loop is finished, the program should display the total
#   number of bugs collected.


# Calories Burned Program-
#   Running on a treadmill you burn 3.9 calories per minute.
#   Write a program that uses a loop to display the number of
#   calories burned after 10, 15, 20, 25, and 30 minutes.


# Advanced Challenge

# Pennies For Pay Program-
#   Write a program that calculates the amount of money a person would
#   earn over a period of time if their salary is one penny the first day,
#   two pennies the second day, and continues to double each day.
#   The program should ask the user for the number of days worked.
#   Display a table showing what the salary was for each day,
#   and then show the total pay at the end of the period.
