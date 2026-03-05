#-------------------------#1--PRINT NUMBER FROM 50-40 IN REVERSE ORDER---------------------------------
# a=50
# while a>=40:
#       print(a)
#       a-=1



# -----------------------#2--PRINT FIRST TWENTY EVEN NUMBERS-------------------------------------------

# i=0
# count=0
# while(count<10):
#       print(i)
#       count+=1
#       i+=2
# print(count)


#--------------------------------------#3--REVERSE A NUMBER-----------------------------------------------

# num=int(input("enter a number"))
# orig=num
# rev=0
# while(num>0):
#       digit=num%10
#       rev=rev*10+digit
#       num=num//10
# print(rev)


#-----------------------------------#4--REVERSE A STRING----------------------------------------------------------------------------
# str=input("enter a string:")
# i=len(str)-1
# while i>=0:
#       print(str[i],end="")
#       i=i-1


#APPROACH-2
# str=input("enter a string:")
# i=len(str)-1
# rev=""
# while i>=0:
#       rev+=str[i]
#       i=i-1
# print(rev)

#---------------------------------#5--sum of first 10 even numbers----------------------------------------
# count=1
# i=0
# sum=0
# while count<=10:
#       sum+=i
#       count+=1
#       i+=2
# print(sum)

#--------------------------------#6--PRINT TABLE OF ANY NUMBER -------------------------------------------

# n=int(input("enter a number"))
# i=1
# while i<=10:
#       m=n*i
#       print(n,"*",i,"=",m)
#       i+=1


#FOR LOOP
# s={"hello",45,True,5+2j,55.0}
# for i in s:
#       print(i)
# print(range(1,10))

# for i in range(10,0,-1):
#       print(i)

# wap to replace space by a underscore inside a string taken by input
# s = input("Enter a string: ")
# new_str = ""

# for i in range(len(s)):
#     if s[i] == " ":
#         new_str += "_"
#     else:
#         new_str += s[i]

# print(new_str)