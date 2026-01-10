"""
a=int(input("Enter your age: "))
print("your age is: ",a)

#conditional operators
# <, >, <=,>=,==,!=
print(a>18)
print(a<=18)
print(a==18)
print(a!=18)

if(a>18):
    print("you can drive")
else:
   print("you can not drive")
print("finish")


price=10
budget=200

if(budget-price>50):
    print("Alex can add 1 kg apple to the cart")
else:
    print("Alex do not add 1 kg apple to the cart")
"""

    
#num=int(input("Enter a number: "))
#print("the number is: ", num)

#if(num<0):
 #       print("the number is negative")
#elif(num==0):
 #       print("the number is zero")
#elif(num==999):
 #       print("the number is special")
#else:
 #       print("the number is positive")    
     

num=18
if(num<0):
        print("The number is negative.")
elif(num>0):
        if(num<=10):
              print("The number is between 1-10 ")
        elif(num>10 and num<=20):
               print("the number is between 11-20")
        else:
               print("The number is greater than 20")             
else:
       print("The number is zero")
