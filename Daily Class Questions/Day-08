# def greet():
#       return "hello"
# print(greet())

# def hello():
#       print("welcome")
# hello()

# def details(name,age):
#       return name,age

# print(details("rahul",20))


##TYPE1-WITH ARGUMENT AND WITH RETURN VALUE

# def product(val1,val2):
#       return val1*val2
# print(product(5,4))



##YPE-2 WITH ARGUMENT AND WITHOUT RETURN VALUE
# def product(val1,val2):
#       print(val1*val2)
# product(5,4)



##TYPE-3 WITHOUT ARGUMENT AND WITHOUT RETURN VALUE
# def product():
#       a=int(input("enter 1st no." ))
#       b=int(input("enter 2nd no." ))
#       print(a*b)


##TYPE-4 WITHOUT ARGUMENT AND WITH RETURN VALUE
# def product():
#       a=int(input("enter 1st no." ))
#       b=int(input("enter 2nd no." ))
#       return a*b
# print(product())

# def prod(a,b):
#       return a*b

# print(prod(20,10))

# print(prod(int(input()), int(input())))



##question-1 extract all the negative numbers from the list
# def negative(marks):
#       l1=[]
#       for i in marks:
#             if i<0:
#                   l1.append(i)
#       return l1
# print(negative([45,-8,-8,-88,-78,56]))
##_________________________________________________________________________________________________
# x=25
# def show():
#       x=45 
#       print(x)
# show()
# print(x)
# num=1
# for i in range(1,3):
#       x+=num
      
# print(x)

# a=1234
# def fname():
#       a=66
# print(a)

# x=25
# def show():
#       x=45 
#       return x,id(x)
      
# print(show())
# print(x)
# print(id(x))
# a=1425
# def name():
#       global a
#       a=20
#       return a , id(a)
# print(name())
# print(a,id(a))


# #If we want to modify a variable from the outer function inside a nested function, we use the nonlocal keyword.”

# def f_name():
#       global a
#       a=20
#       b=2000
#       print(b)
#       def f2():
#             nonlocal b
#             b=400
#             print(b)
#       print(b)
# a = 40

# def f_name():
#       global a
#       a = 20
#       b = 2000
#       print("Before f2:", b)

#       def f2():
#             nonlocal b
#             b = 400
#             print("Inside f2:", b)

#       f2()

#       print("After f2:", b)

# f_name()
# print("Global a:", a)

# a=500
# def fname():
#       global a 
#       a=700
#       b=50
#       print(a+b)
# fname()
# print(a)

# def f_name():
#       global a
#       a = 20
#       b = 2000
#       print("Before f2:", b)

#       def f2():
#             nonlocal b
#             b = 400
#             print("Inside f2:", b)

#       f2()

#       print("After f2:", b)
# f_name()
# a=200
# def f_name():
#       global a
#       a=100
#       b=50
#       print(a+b)
#       def fname2():
#             nonlocal b
#             b=300
#             print(b)
#       fname2()
#       print(b)
# f_name()
# print(a)

# def prod(marks):
#       prod=1
#       for i in marks:
#             prod=prod*i
#       return prod
# marks=eval(input())
# print(prod(marks))





# wap to print the initial index of a character present in a given string

# def initial_index(str1,character):
#       count=0
#       for i in range(0,len(str1)):
#             if str1[i]==character:
#                   return count
#             else:count+=1
# str1=input("enter the string:")
# character=input("enter the ccharacter:")
# print(initial_index(str1,character))

# def initial_index(str1, character):
#       for i in range(len(str1)):
#             if str1[i] == character:
#                   return i

# str1 = input("Enter the string: ")
# character = input("Enter the character: ")

# print(initial_index(str1,character))


#_____________________________________PACKING AND UNPACKING IN PYTHON
#SINGLE OR TUPLE PACKING
# def in_index(c,*t):
#       for i in range(len(t)):
#             if t[i]==c:
#                   print(t)
#                   print(c)

#                   return i
# print(in_index(10,20,40,60,78,80,90,10))
#__________________________________________________________________

#______________DICTIONARY PAKING OR DOUBLE PACKING


# def dict_packing(**d):
#       return d
# print(dict_packing(a=100,b=20,c="saumya",d=True))


#___________________________UNPACKING IN PYTHON_________________________
def unpack(a,b):
      return a,b
print(unpack(*"saum"))
print(unpack(*["hygf",50,60,7]))