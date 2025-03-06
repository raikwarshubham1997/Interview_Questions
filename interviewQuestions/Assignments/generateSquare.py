"""
Generate Square Numbers in Range

Write a  Python program to generate and print a list of the first and last 5 elements where the values are square numbers between 1 and 30 (both included).

"""
# Define a function named printValues
def printValues():
    # Create an empty list 'l'
    l = list()
    # Loop from 1 to 20 (inclusive)
    for i in range(1, 21):
        # Calculate the square of 'i' and append it to the list 'l'
        l.append(i**2)
    # Print the first 5 elements of the list 'l'
    print(l[:5])
    # Print the last 5 elements of the list 'l'
    print(l[-5:])

# Call the printValues function to execute it
printValues()