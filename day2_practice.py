a=5
print(a)
##how to write input code
name = input("Enter your name: ")
print("Hello,", name)

##how to take integer input for a for loop asking for voting age 
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

    ##write a nested if else to check if a number is positive, negative or zero
num = float(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

##write a program using elif with 3 input to check the largest number among 3 numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3
print("The largest number is:", largest)

##type casting 

x = "10"
y = int(x)
print(y)
print(type(y))
z = float(x)
print(z)
print(type(z))
print(bool("Hello"))
print(bool(""))  
x = complex(2,3)
print(x)
print(ord("A"))
print(chr(65))

#convert a to A using ascii values
ch = 'a'
ascii_val = ord(ch)
new_ascii_val = ascii_val - 32  # Subtract 32 to convert lowercase to uppercase
new_ch = chr(new_ascii_val)
print("Original character:", ch)
print("New character:", new_ch)


## typecasting errors
int("a")

int("3.5")

int("")

float("hello")

int([1,2,3])

ord("AB")

set([[1,2]])

int("12a")

int(None)

int({1:2})

int(" ")

int([])

float((1,2))

int(str({1,2}))

int(3+4j)

float(5+2j)

bool("False")

int("0x12")

int("1010b")

float(None)
str({1:2, 3:4})
dict([[1,2],[3,4]])

## note: The above errors will raise exceptions when executed.
## the reason being is that the input values are not in a format that can be converted to the specified type. For example, trying to convert a non-numeric string to an integer or float will raise a ValueError. Similarly, attempting to convert complex numbers or incompatible data structures will also result in errors.
## Python caches integers from -5 to 256
# int() accepts only whole numbers
# float() accepts only numeric values
# ord() accepts only ONE character
# complex() cannot be converted to int or float
# None cannot be typecasted
# Collections cannot be converted to numbers
# Empty string cannot be converted to number
# Mixed characters cause error
# Invalid format throws error
# Python is strict in conversion



####control statements and loops practice

#for loop examples
for i in range(5):
    print(i)

for i in range(2, 10, 2):
    print(i)


    i=0
    while i<=10:
        print(i,end='')
        i+=2