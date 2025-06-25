#Dividing 2 integers

#Type this in terminal or console
x = 10/5
print(type(10/5))


print()
print()


#Assignment of variables
# Operations begins: comparing variables
a = 10
b = 20
c = 10

print("comparing (a==b) = " , str(a == b))
print("comparing (a==c) = " , str(a == c))
print("Not equal (a!=b) = " , str(a != b))
print("Less than equal (a<=b) = " , str(a <= b))
print("Greater than equal (a>=b) = ", str(a >= b))


print()
print()


print("Print a, b, c = ", str(a),str(b),str(c) )
a+=b
print("Show agument (a+=b) = " , str(a))


print()
print()


# augmented
x = 10
y = 3
print("The value of x is", str(x))
print("The value of y is", str(y))
x*= y
print("Multiplying x and y (x*=y) = ", str(x))


print()
print()



# Logical Operators
x=20
y=30

print("The value of x is", str(x))
print("The value of y is", str(y))

print ("AND OPERATOR:","x==25 and y==30 is " ,(x==25 and y==30))
print ("OR OPERATOR:","x==25 or y==31 is ",(x==25 or y==31))
print("NOT - OR OPERATOR:","x==25 or y==31 is" ,not(x==25 or y==31))



print()
print()



# This program rounds a number to the hundredth digit
user_input = input("Enter a number: ")
num = float(user_input)
print(f"{num} rounded to 2 decimal places is {round(num, 2)}")


print()
print()



# This program shows the absolute value of a number
user_input = input("Enter a number: ")
num = float(user_input)
print(f"The absolute value of {num} is {abs(num)}")


print()
print()



# The program determines weather the different between the 2 inputed numbers is a float or not
num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
print(
    f"The difference between {num1} and {num2} is an integer? "
    f"{(num1 - num2).is_integer()}!"

# We use .is_integer() to see weather the float can be turned into a int without losing presition


    )



print()
print()

#This program finds the average of 3 numbers
a,b,c=[int(x) for x in input("Enter three integer numbers").split()]
average = (a+b+c)/3
print("Average of the three numbers is:",average)

# For the program to work we need to add spaces between each number
# EX: 1 1 1





print()
print()




# This program solves an exponential problem
base = input("Enter a base: ")
exponent = input("Enter an exponent: ")
result = float(base) ** float(exponent)
print(f"{base} to the power of {exponent} = {result}")








print()
print()



#finds the area of a circle with a given area
import math
r=float(input("Enter the radius"))
area=math.pi*r**2
print(area)
















print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

print(f"Each person should pay: ${final_amount}")