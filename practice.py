#EASY LEVEL ✅
#These are basic problems: input, print, arithmetic, strings, and lists.
#1.Hello Message
#Ask for your name and print: "Hello <name>!"
#code:
name=input("Enter your name: ")
print("Hello", name + "!")


#2.Age Calculator
#Ask for your year of birth and calculate your age (current year = 2026).
#CODE:
birth_Year=int(input("Enter your year of birth: "))
current_Year=2026
age = (current_Year - birth_Year)
print("your age is", age)


#3.Addition of Two Numbers
#Take two numbers from the user and print their sum.
#CODE:
a=int(input("Enter the 1st number: "))
b=int(input("Enter the 2nd number: "))
print(a+b)

#4.Even or Odd Checker
#Take a number and print if it is even or odd.
#CODE:
num=int(input("Enter a number: "))
print("remainder when divided by 2: ",num%2)
#or,
num=int(input("Enter a number: "))
remainder=num%2
print("number:",num)
print("number % 2:",remainder)
print("if remainder is 0: Even")
print("if remaider is 1: Odd")

#5.Simple Multiplication Table
#Take a number and print its table from 1 to 10.
#CODE:
num=int(input("Enter a number"))
print("num:",num,"*",1,"=",num*1)
print("num:",num,"*",2,"=",num*2)
print("num:",num,"*",3,"=",num*3)
print("num:",num,"*",4,"=",num*4)
print("num:",num,"*",5,"=",num*5)
print("num:",num,"*",6,"=",num*6)
print("num:",num,"*",7,"=",num*7)
print("num:",num,"*",8,"=",num*8)
print("num:",num,"*",9,"=",num*9)
print("num:",num,"*",10,"=",num*10)

#6.List Sum
#Create a list [1, 2, 3, 4, 5] and print the sum of all elements.
#CODE:
num=[1,2,3,4,5]
total=sum(num)
print("the number list:",num)
print("the sum of all elements are:",total)

#7.String Length & Reverse
#Ask the user for a string and print its length and reverse.
#CODE:
text=input("Enter a string:")
length=len(text)
reverse_text=text[::-1]
print("the string length is:",length)
print("the reverse string is:",reverse_text)
