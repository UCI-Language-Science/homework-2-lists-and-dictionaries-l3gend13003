# Write code that calculates the sum of the square of every even 
# number in the list below and prints it (that is, you take each 
# even number, square it, and then add them all together).
# 
# You can use a list comprehension or a regular loop. You can also
# use the sum function to sum the values in a list if it's helpful.
# sum(<list>)
# 
# For the list below, your code should print 44984
#
def even_square_sum():
    numbers = [1, 62, 3, 57, 26, 8, 101, 200, 43, 20, 11]

    # YOUR CODE GOES HERE
    even_squares_sum = sum([x**2 for x in numbers if x % 2 == 0])
    print("The sum of the square of even numbers is:", even_squares_sum)

if __name__ == "__main__":
    even_square_sum()