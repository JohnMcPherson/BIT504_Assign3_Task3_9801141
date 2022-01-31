# Display menu - direct equivalent of Java - with simplified print syntax
# ";"s removed in many places - unnecessary
print("Calculations")
print("1. Calculate area of a square")
print("2. Calculate area of a circle")
print("3. Display palindromes up to 1,000")

# Get input

# take the input and convert it to an integer
# CHECK OK not to check for int
# No attempt made to recover from the user entering something other than an integer
# This will crash if the user enters a string. But so will the Java code
# I assume this program does not have to do any checking beyond wha the Java does

option = int(input("Enter an option: "))
# Display the chosen option (on the same line as the prompt)
# Note that Python displays >? (unlike Java). I have assumed we are happy to
# keep that, as this is a Python command line program, and it makes sense to run
# with the conventions of the framework
print(option)
# Check validity of option
# Use chained comparison to
# no parentheses required
if 1 <= option <= 3:

    # decide on which path to take based on the input value
    # use "match/case " structural matching; the Python equivalent of Java's switch/case
    match option:
        case 1:
            # confirm the path the user has chosen
            print("\n**** Area of a square ****")

            # Get the width of the square
            # We need both the string and the integer representations because
            # (unlike Java) Python does not automatically convert integer to string
            # when concatenating
            strWidth = input("Enter width of square (cm): ")
            # Again, in doing the conversion to integer we are not checking that the
            # conversion will succeed. The program will crash if it doesn't
            intWidth = int(strWidth)
            # Note the leading "\n"; to get a new line directly after the input statement
            # Note the use of both strWidth and intWidth
            print("\nThe area of a square of " + strWidth + "cm = " + "areaSquare(width)" + "cm squared")


