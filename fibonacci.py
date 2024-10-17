# Fibonacci Series
# The sum of the first two elements define the next set of elements

first_number, second_number = 0, 1

minimum_number = int(input("Please enter a positive number greater than 1: "))

if minimum_number > 1:

    while second_number < minimum_number:

        print(second_number, end=', ')
        first_number = second_number
        second_number = first_number + second_number
    
    print('Complete!')

else:

    print("Your input was ignored")

# Require a user to enter an integer
print("Let's do something else now.")

user_input = int(input("Please enter a random number:"))

if user_input < 0:

    user_input = 0
    print('The negative number you entered is not allowed')

elif user_input == 0:

    print("The number you have entered is: ", user_input)

elif user_input == 1:

    print("Come on ", user_input ," is so basic!")

else:
    print("That's much better. Anything greater than 1")

# Lets look at iteratig over thing using python
# It's a bit different than other programming languages
# It iterates over items

# Example
words = ['cat', 'window', 'defenestrate']

for word in words:
    # Print something presentatble to the audience.
    print(word , " has ",  len(word), " characters!", end = "\n")
