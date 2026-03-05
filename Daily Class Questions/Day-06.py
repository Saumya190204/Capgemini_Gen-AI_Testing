l = ["p1.py","first.txt","t3.py","tk.txt","tfk.com"]
a = {}
for i in l:
    parts = i.split(".")      
    name = parts[0]
    ext = parts[1]
    if ext in a:
        a[ext].append(name)
    else:
        a[ext] = [name]
print(a)


#----------------------------------------------------------------------------------------------------
a=input("enter a string")
parts = a.split(" ") 
max_len=0
max_ele=parts[0]
for i in parts:
    x=len(i)
    if(x>max_len):
        max_ele=i


print(max_ele)
            


#---------------------------------ques.2--------------------------------------------------------------
a = 'aaabbaabcc'
str1 = ""
i = 0
count = 1
while i < len(a) - 1:
    
    if a[i] == a[i+1]:
        count += 1
    else:
        str1 += a[i] + str(count)
        count = 1
    
    i += 1

# handle last character
str1 += a[i] + str(count)

print(str1)

#----------------------------nested for loop --extract all the vowels from the given list----------------------------------------------
l=["saumya","rahul","tanish","manish"]
v=""
for i in l:
    for j in i:
        if j in "aeiouAEIOU":
            v+=j
print(v)
#----------------------------ques-4()extract all the string values and print the stroing values in dictionary fromat with string as keys and the vowels in it will be key's value
l=[(2+3j),12,"program","python",False,"sky"]
a={}
for i in l:
    if(type(i)== str):
        v=""
        for j in i:
            if j in "AEIOUaeiou":
                v+=j
        a[i]=v
              
           
print(a)      

# ----------------------------------INTERMEDIATE TERMINATION CONDITION---------------------------------------------
# 1.break
# 2.Continue
# 3.pass   

for i in range(1,11):
    if i==5:
        break
    print(i)


for i in range(40,50):
    if i==45:
        continue
    print(i)

for i in range(40,50):
   if i==45:
        pass
   else:
       print(i)

# DEFINITION OF PASS:agar maine kuch nahi likha kisi bloack me and mujhe agar us block ko skip krna h ya execute krna h without error then we use pass