# Write a program that continuously prompts the user for a 
# temperture (in the scale of your choosing). Every time 
# the user inputs a temperature, the program should report 
# the mean of all the values entered so far. When the user
# types in 'quit' the program should terminate.
#
# An example interaction might look like
# Input a temperature
# >> 42
# The average temperature so far is 42
# Input a temperature
# >> 26
# The average temperature so far is 34.0
# Input a temperature
# >> 52
# The average temperature so far is 40.0
# >> quit
# Goodbye
#
# You can use the sum function to sum all the values in a list
# sum(<list>)

def temperature_calculator():
    # YOUR CODE GOES HERE
    # You can delete the line below when you start adding code
    total_temperature = 0
    count = 0
    while True:
        user_input = input ("Enter a temperature (or 'quit' to stop):")
        if user_input.lower() == 'quit':
            print("Goodbye.")
            break
        try:
            temperature = float(user_input)
            total_temperature += temperature
            count += 1
            mean_temperature = total_temperature / count
            print(f"The average temperature so far is: {mean_temperature:.2f}")
        except ValueError:
            print("Please enter a valid number or 'quit' to stop.")

if __name__ == "__main__":
    temperature_calculator()