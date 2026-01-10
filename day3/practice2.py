user=input("Enter your name: ")
print("hello",user)

age=int(input("Enter your age: "))
future_age=age + 5
print("age wiil be: ",future_age)

a=int(input("The 1st number: "))
b=int(input("The 2nd number: "))
print("addition:",a,"+",b,"=",a+b)
print("subtraction:",a,"-",b,"=",a-b)
print("multiplication:",a,"*",b,"=",a*b)

#convert celsius to fahrenheit
#formula=(C*9/5)+32
celcius=float(input("Enter the temparature: "))
fahrenheit=(celcius*9/5)+32
print(fahrenheit)

num=int(input("Enter the number: "))
square=(num**2)
print("square of a number:",square)

g=int(input("Enter marks: "))
h=int(input("Enter marks: "))
i=int(input("Enter marks: "))
total=(g+h+i)
average=total/3
print(total)
print(average)

u=int(input("Enter: "))
v=int(input("Enter: "))
temp=u
u=v
v=temp
print("After swapping: ")
print("u =",u)
print("v =",v)
