"""This is a short Python cheatsheet.

At the top of the file is a comment that looks like this.

This only exists for humans reading your code. This type of comment is to talk about what your
code is supposed to do.

"""

# This is another type of comment. This type of comment is really more focused on how the code
# works. For instance, this code works by having a bunch of comments and code samples.

# The first thing you learn to do when learning a new programming language is learn how to print
# "Hello World!".
print("Hello World!")

# By the way, you can also use single quotes.
print('Hello World!')

# The next thing you might want to do is ask the user a question, and then respond to them. We're
# going to ask the user their name, store it in a "variable" called name, and then say hello to
# them.
name = input("What's your name? ")
print("Hello", name)
# Note, it'll automatically put a space between "Hello" and name.

# If we want to get more sophisticated with how we output things, we can use the "%" operator.
# The "%" operator replaces "%s" with the name. There are multiple ways to do this sort of thing
# in Python, but this is good enough for now.
print("Hello, %s!" % name)

# When you read data from the user, if you want to treat it as a number, you need to convert it
# to a number. First, I'll show you how to convert it to an "int". An int is a number with no
# decimal point.
age = input("How old are you? ")
age = int(age)
age = age + 1
print("Next year, you'll be %s years old." % age)

# Here are a couple shortcuts.
age = int(input("How old are you? "))  # Call input and then call int with the result.
age += 1  # This is the same as age = age + 1.
print("Next year, you'll be %s years old." % age)

# If you want to work with decimals, you should use a "float".
num = input("Give me a number with a decimal point: ")
num = float(num)
num += 1.5
print("Hmm, I think %s is bigger!" % num)

# Python also has boolean values, True and False. You can use these with if statements.
older_than_12 = input("Are you older than 12 (y or n)? ")
if older_than_12 == "y":  # This results in True or False.
    print("Ah, you are older than 12!")
# Notice, you use "=" when you are assigning a variable. You use "==" when you evaluating whether
# two things are equal.

# Aside from "if", Python also has "elif" (else if) and "else". Aside from ==, there's also
# <, >, <=, and >=.
age = input("How old are you? ")
age = int(age)
if age < 10:
    print("You are less than 10. Wow!")
elif age < 13:
    print("You're older than 10, but less than 13.")
else:
    print("You're 13 or older.")

# If you want the opposite of ==, it's != (not equals).
password = input("What's the password? ")
if password != "3.14":
    print("Nope!")
else:
    print("Oh, you're good!")

# By the way, sometimes when we create variables, we use all upper case in order to say that the
# value isn't going to change.
PI = 3.141592653589793

# Python has a couple different ways of looping. Looping is when you do the same thing over and
# over. The first way is a while statement.
print("I'm going to print your name 5 times!")
i = 0  # This is the setup.
while i < 5:  # This is where we figure out if we want to keep looping.
    print("Hi, %s!" % name)
    i += 1  # This is where we set ourselves up for the next run through the loop.

# You can also write a loop that doesn't stop until the user says so.
while True:  # This is going to loop forever unless something else happens.
    stop = input("Are you ready to stop yet (y or n)? ")
    if stop == "y":
        break  # This is how we break out of a loop.

# There's another kind of loop called a for loop. Here's how to use a for loop to loop over a range
# of numbers. This is easier, but less flexible than using a while loop.
for i in range(10):  # (starts at 0) 0, 1, 2, ..., 9 (but not 10)
    print(i)

# Similarly, if you have a list of things, you can loop over that list of things.
favorite_foods = ["apples", "pears", "oranges", "lasagna"]
for food in favorite_foods:
    print("I like %s." % food)

# If you have a bunch of instructions, you can wrap them up in a function. A function is like
# a recipe. You can use it over and over.
def bake_lasagna():
    print("Adding cheese")
    print("Adding pasta")
    print("Adding pasta sauce")
    print("Baking...")

bake_lasagna()
bake_lasagna()
bake_lasagna()

# You can also use a function to compute something and then return the value.
def which_is_bigger(first, second):
    if first > second:
        return "first"
    elif second > first:
        return "second"
    else:
        return "they're equal"

print("Which is bigger, 5 or 2?")
print(which_is_bigger(5, 2))

print("Which is bigger, 3 or 7?")
print(which_is_bigger(3, 7))

print("Which is bigger, 2 or 2?")
print(which_is_bigger(2, 2))

# Here's a useful function. It can say a message a certain number of times.
def say_message(message, num_times):
    for i in range(num_times):
        print(message)

say_message("Python rules!", 3)
