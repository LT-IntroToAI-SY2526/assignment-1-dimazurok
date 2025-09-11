# Assignment 1: AI-Generated Python Problems
# Name: [Daniel Mazurok]

"""
AI-Generated Problem Set

INSTRUCTIONS:
1. Document your original AI prompt below
2. Copy the problems your AI assistant generated
3. Implement solutions for each problem
4. Include comments explaining your approach
5. Test your solutions with different inputs

Remember: The goal is to LEARN, not just get working code!
"""

# =============================================================================
# PART 1: DOCUMENT YOUR AI COLLABORATION
# =============================================================================

"""
MY ORIGINAL AI PROMPT:
I'm learning Python basics in a high school programming class. I have some experience with Java and Java script. 
Can you create 5 practice problems that cover: 
- Variables and basic data types 
- Conditionals (if/elif/else) 
- For loops and while loops 
- Functions 
- Basic list operations 
Make them progressively more challenging. Make sure each problem has clear instructions and example inputs/outputs.

"""

# =============================================================================
# PART 2: AI-GENERATED PROBLEMS & SOLUTIONS
# =============================================================================

"""
PROBLEM 1: [Simple Calculator (Variables & Data Types)]
Write a program that asks the user to enter two numbers and then prints the result of adding,
subtracting, multiplying, and dividing them.

Enter first number: 10
Enter second number: 5
Should return:
Addition: 15.0
Subtraction: 5.0
Multiplication: 50.0
Division: 2.0

PROBLEM 2: [Grade Checker (Conditonals)]
Write a program that asks the user to enter a test score (0–100) 
and prints the letter grade based on the following:

Enter your score: 85
Should return:
You got a B!

PROBLEM 3: [Multiples of a number (Loops)]
Write a program that asks the user for a number and prints all 
the multiples of that number from 1 to 100.

Enter a number: 25
Should return:
25
50
75
100

PROBLEM 4: [Password Validator (Functions + Loops + Conditionals)]
Write a function is_valid_password(password) that checks if a password 
is valid. A valid password:

Is at least 8 characters long

Contains at least one number

Contains at least one uppercase letter

Then, use a loop to keep asking the user to enter a password until 
they enter a valid one.

Enter a password: hello
Invalid password. Try again.
Enter a password: Hello123
Password accepted!

PROBLEM 5: [List Statistics (Lists + FWrite a program that asks the 
user to enter a series of numbers (separated by spaces), and then:

Converts them into a list of integers

Defines a function to compute the average, maximum, and minimum

Prints the resultsunctions + Loops)]

Enter numbers separated by spaces: 5 10 15 20
Should return:
Average: 12.5
Maximum: 20
Minimum: 5

"""
# PROBLEM 1:
# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract two numbers
def subtract(a, b):
    return a - b

# Function to multiply two numbers
def multiply(a, b):
    return a * b

# Function to divide two numbers
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Cannot divide by zero."

# Function to run the calculator
def simple_calculator():
    # Get input from user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Perform calculations
    print("Addition:", add(num1, num2))
    print("Subtraction:", subtract(num1, num2))
    print("Multiplication:", multiply(num1, num2))
    print("Division:", divide(num1, num2))

# Runs the calculator
simple_calculator()

#PROBLEM 2:
# Ask the user to enter their test score
score = int(input("Enter your score (0-100): "))

# Check the score and assign a letter grade
if score >= 90:
    print("You got an A!")
elif score >= 80:
    print("You got a B!")
elif score >= 70:
    print("You got a C!")
elif score >= 60:
    print("You got a D!")
else:
    print("You got an F!")

# PROBLEM 3:
# Ask the user for a number
num = int(input("Enter a number: "))

# Loop through numbers 1 to 100
for i in range(1, 101):
    # Check if i is a multiple of num
    if i % num == 0:
        print(i)

# PROBLEM 4:
def is_valid_password(password):
    # Check length
    if len(password) < 8:
        return False

    # Check for at least one number
    has_number = False
    # Check for at least one uppercase letter
    has_upper = False

    for char in password:
        if char.isdigit():
            has_number = True
        if char.isupper():
            has_upper = True

    # Return True only if both conditions are met
    return has_number and has_upper


# Main program: keep asking until valid password
while True:
    pwd = input("Enter a password: ")
    if is_valid_password(pwd):
        print("Password accepted!")
        break
    else:
        print("Invalid password. Try again.")

# PROBLEM 5:
def compute_stats(numbers):
    total = 0
    maximum = numbers[0]
    minimum = numbers[0]

    for num in numbers:
        total += num
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num

    average = total / len(numbers)
    return average, maximum, minimum


# Ask user to enter numbers separated by spaces
user_input = input("Enter numbers separated by spaces: ")

# Convert input string to a list of integers
numbers_list = [int(x) for x in user_input.split()]

# Compute average, max, min
avg, max_num, min_num = compute_stats(numbers_list)

# Print results
print(f"Average: {avg}")
print(f"Maximum: {max_num}")
print(f"Minimum: {min_num}")

# =============================================================================
# PART 3: TESTING YOUR SOLUTIONS
# =============================================================================


"""
Test all your solutions with different inputs

Add asserts if you feel comfortable

Example:
print("Testing Problem 1:")
print(f"is_even(4): {is_even(4)}")  # Should print True
print(f"is_even(7): {is_even(7)}")  # Should print False
"""

print("Testing Problem 1:")
# Add your tests here
# Enter first number: 10
# Enter second number: 5
Addition: 15.0
Subtraction: 5.0
Multiplication: 50.0
Division: 2.0

# Enter first number: 6
# Enter second number: 8
Addition: 14.0
Subtraction: -2.0
Multiplication: 48.0
Division: 0.75
""
print("\nTesting Problem 2:")
# Add your tests here
# Enter your score (0-100): 80
# You got a B!

# Enter your score (0-100): 92
# You got a A!

print("\nTesting Problem 3:")
# Add your tests here
# Enter a number: 12
# 12
# 24
# 36
# 48
# 60
# 72
# 84
# 96

# Enter a number: 30
# 30
# 60
# 90

print("\nTesting Problem 4:")
# Add your tests here
# Enter a password: BergClass123@
# Password accepted!

# Enter a password: hlelo2
# Invalid password. Try again.
# Enter a password: hello123!
# Invalid password. Try again.
# Enter a password: Helllo124@
# Password accepted!


print("\nTesting Problem 5:")
# Add your tests here
# Enter numbers separated by spaces: 1 2 5 9
Average: 4.25
Maximum: 9
Minimum: 1

# Enter numbers separated by spaces: 5 12 59 61
Average: 34.25
Maximum: 61
Minimum: 5
