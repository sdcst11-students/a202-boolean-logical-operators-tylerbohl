#! python3
 
"""
Problem 1
Ask the user to enter a number.
The number is considered "frue" if it is
divisible by 6, but not divisible by 8.
State whether the number is "frue" 
(2 marks)

Inputs:
a number

Outputs:
xx is frue
xx is not frue

example:
Enter a number: 48
48 is not frue

Enter a number: 36
36 is frue

Enter a number: 16
16 is not frue
"""

x = input("enter a number: ")
x = float(x)

x6 = x % 6
x8 = x % 8

if x6 == 0 and x8 != 0:
    print(x, "is frue")
else:
    print(x, "is not frue")


