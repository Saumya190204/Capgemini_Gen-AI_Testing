#copy
import copy


# -------- general copy --------
a = [10,20,30]
b = a
b[0] = 100
print(a)
print(b)
# -------- shallow copy --------
x = [1,2,3]
y = copy.copy(x)
y[0] = 50
print(x)
print(y)
# -------- deep copy --------
m = [5,6,7]
n = copy.deepcopy(m)
n[0] = 99
print(m)
print(n)

#operators
# ---------- arithmetic operators ----------

a = 12
b = 5

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)



# ---------- comparison ----------

x = 10
y = 20

print(x>y)
print(x<y)
print(x==y)
print(x!=y)



# ---------- logical ----------

a = True
b = False

print(a and b)
print(a or b)
print(not a)



# ---------- membership ----------

text = "python"

print("p" in text)
print("z" in text)
