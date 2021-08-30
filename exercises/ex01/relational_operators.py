"""Exercise 1 part 3."""

_author_ = "730405432"

"""Applied concepts from part 2 to solve True/False equations."""

initialnumber1: str = input("Left-hand side:")
initialnumber2: str = input("Right-hand side:")
number1 = int(initialnumber1) 
number2 = int(initialnumber2)

print(str(number1) + " < " + str(number2) + " is " + str(number1 < number2))
print(str(number1) + " >= " + str(number2) + " is " + str(number1 >= number2))
print(str(number1) + " == " + str(number2) + " is " + str(number1 == number2))
print(str(number1) + " != " + str(number2) + " is " + str(number1 != number2))