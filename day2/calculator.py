#calculator:
print(5+6)#addition operator +
print(15-6)#subtraction operator -
print(15*6)#multiplication operator *
print(15/6)#division operator /
print(15//6)#floor division operator //
print(5%2)#modulus operator %
print(2**4)#exponential operator **

#exercise:
"""
creat a calculator capable of performing addition,subtraction,multiplication,division,modulus,floor divisio,exponential operations on two numbers.your program should format the output in a readable manner.
"""
#code:
m=int(input("enter 1st number: "))
n=int(input("enput 2nd number: "))

print("Addition:", m, "+", n, "=", m+n)
print("Subtraction:", m, "-", n, "=", m-n)
print("Multiplication:", m, "*", n,"=", m*n)
print("Division:", m, "/", n, "=", m/n)
print("Floor division:", m, "//", n, "=", m//n)
print("Modulus:",m,"%", n, "=", m%n)
print("Exponential:",m,"**",n, "=", m**n)

#or,
m=15
n=3
print("The value of:",m,"+",n,"=",m+n)
print("The value of:",m,"-",n,"=",m-n)
print("The value of:",m,"*",n,"=",m*n)
print("The value of:",m,"/",n,"=",m/n)
