# 1..Check if number is a 3-digit number or not take user input.
# a=int(input("enter a no.:"))
# if len(str(a))==3:
#       print("three digit number")
# else:
#       print("not a three digit number")



# 2------------------# Check if string length is greater than 5.
# str=input("enter a string:")
# if len(str)>5:
#       print("true")
# else:
#       print("false")



#  3------------------Check if number is zero so print ‘zero’ otherwise print ‘Not Zero’.
# a=int(input("enter a no.:"))
# if a==0:
#       print("zero")
# else:
#       print("not zero")



# 4......Check if person can enter club (age + ID check). If yes, print ‘Eligible’.
# a=eval(input("enter the age:"))
# b=eval(input("Have ID:"))
# if a>=18 and b==True:
#       print("eligible")
# else:
#       print("ineligible")



# 5..Check if number is within range 10–50 if yes print ‘In Range’ otherwise ‘Not in Range’.
# a=int(input("enter a number:"))
# if a in range(10,51):
#       print("IN RANGE")
# else:
#       print("NOT IN RANGE")

#---------------------------------------------------------------------------------------------------

# 6..Simple calculator (+ or -) take both number and operator symbol from user.
# a=int(input("enter a number1:"))
# b=int(input("enter a number2:"))
# c=input("enter a symbol:")
# if c=='+':
#       print(a+b)
# elif c=='-':
#       print(a-b)
# elif c=='*':
#       print(a*b)
# else :
#       print(a/b)

#---------------------------------------------------------------------------------------------------


# 7.....Check if username and password are correct if yes, print ‘Login Successful’.
# Username="admin"
# password=1234
# a=input("enter a username:")
# b=int(input("enter the password:"))
# if a==Username and b==password:
#       print("LOGIN SUCCESSFUL")
# else:
#       print("INVALID CREDENTIALS")

#----------------------------------------------------------------------------------------------------------


# 8....Check if temperature is hot or cold.
# a=int(input("ENTER THE TEMPERATURE"))
# if a>20 and a<=40:print("warm")
# elif a>-25 and a<=20:print("cold")
# else:print("hot")

#-------------------------------------------------------------------------------------------------------

# 9..PALINDROME STRING
# s = input("Enter a string: ").lower()
# if s == s[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")



# APPROACH-2 JUST FOR NUMBERS 


# num=int(input("enter a number:"))
# orig=num
# rev=0
# while num>0:
#       digit=num%10
#       rev=rev*10+digit
#       num=num//10

# if rev==orig:
#       print("p")
# else:
#       print("n")


#-------------------------------------------------------------------------------------------------------


#10..... Check if number is greater than 100.
# a=int(input("enter a number1:"))
# if a>100:print("no.is greter than 100")
# else:print("Number is less than 100")


# ----------------------------------NESTED IF-ELSE------------------------------------------------------
  

# marks=int(input("enter marks:"))
# if(marks>200):
#       if(marks>200 and marks<250):
#             print("MNIT")
#       elif(marks>=250 and marks<300):
#             print("Trichy")
#       elif(marks>=300 and marks<350):
#             print("Warangal")
#       elif(marks>=350 and marks<400):
#             print("varanasi")
#       else:
#             print("GREAT")
# else:print("NO IIT")



#---------------------------------------------------------------------------------------------------



# age=int(input("enter the age:"))
# if age>=18:print("eligible to vote")
# else:print("ineligible to vote")
      

# age=int(input("enter the age:"))
# income=int(input("enter the income:"))
# creditscore=int(input("enter the creditscore:"))
# if age>=21:
#       if income>= 25000:
#             if creditscore>=700:
#                   print("loan approved")
#             else:print("Low Credit Score")
#       else:print("LOW INCOME")
# else:print("Age not eligible")



#------------------------------------------------------------------------------------------------





# maths=int(input("enter the maths:"))
# english=int(input("enter the english:"))
# hindi=int(input("enter the hindi:"))
# average=(maths+english+hindi)/3
# if maths>=40:
#       if english>=40:
#             if hindi>=40:
#                   if(average>=75):
#                         print("pass with distinction")
#                   else:print("pass")
#             else:print("fail")
#       else:print("fail")
# else:print("fail")



#---------------------------------------------------------------------------------------------------
 


# income=int(input("enter income"))
# if income>=0 and income<250000:
#       print("no tax")
# if income>=250000 and income<=500000:
#       print("5% tax")
# if(income>500000):
#       if(income <=1000000):
#             print("20% tax")
#       else:print("40% tax")

