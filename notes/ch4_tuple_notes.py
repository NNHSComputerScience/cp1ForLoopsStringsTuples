# Ch. 4: Notes on Tuples

# TUPLE: a type of sequence, like strings, but can contain ANY type of element. 

# IMMUTABLE: cannot be changed once created

a_string = "howdy"
# this generates an error because a string is immutable
#a_string[0] = "r"
a_string = "rowdy"
print(a_string)
# the value of a varaible is a reference to the string; not the string itself

# Creating a Tuple
a_tuple = ("hello", "hi", "hey")
# tuples, like strings, are immutable
#a_tuple[2] = "howdy"

boys = ("Jim", "John", "Bob", "Alex")
girls = ("Jill", "Stacy", "Sarah", "Gwendolyn", "Alex")
empty_tuple = ()

# printing a tuple
print(boys)
print(girls)


# CHALLENGE 1: display elements in each tuple with for loop (hint: use in)
for name in boys:
    print(name)
for name in girls:
    print(name)
print()


# len()
print(len(boys))
print("There are", len(girls), "girls in the class.")


# tuples can be added together to make a new tuple
class_list = boys + girls
print(len(class_list))

# searching in w/ multiple conditions
if "John" in boys:
    print("Hello John")

# incorrect use of or
#if "Gwen" in boys or girls:
if "Gwen" in boys or "Gwen" in girls:   # cannot find partial values
    print("Hello Gwendolyn")

if "Gwendolyn" in boys or "Gwendolyn" in girls:
    print("Hello Gwendolyn")

# CHALLENGE 2: search tuples to find names that are in both using a for loop
for student in boys:
    if student in girls:
        print(student, "is in both tuples")

for i in boys:
    for j in girls:
        if i == j:
            print(j, "is in both tuples")
        
# concatenating tuples
all_students = boys + girls
print(all_students)

# concatenating a single element to a tuple
new_student = ("Maria",)    # comma indicates a tuple rather than a string
girls += new_student
print(girls)


# CHALLENGE 3: use a while loop to add new names to a tuple (as many as user wants)
all_students = ()
more = "y"
while more == "y":
    new_student = input("Who is the new student: ")
    allstudents += (new_student,)
    more = input("Are there any more students to add? (y on n) ").lower()
print (allstudents)
