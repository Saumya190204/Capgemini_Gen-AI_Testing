e = [10, 20, 30, 40]
print("List:", e, type(e))

f = (1, 2, 3)
print("Tuple:", f, type(f))

g = {"name": "Saumya", "age": 22}
print("Dictionary:", g, type(g))

h = {1, 2, 3, 4}
print("Set:", h, type(h))


print("\n===== STRING INDEXING =====")

s = "PYTHON"

print("String:", s)

print("First character:", s[0])
print("Second character:", s[1])
print("Last character:", s[5])

print("Last character:", s[-1])
print("Second last:", s[-2])
print("Third last:", s[-3])


print("\n===== STRING SLICING =====")

print("0:3 ->", s[0:3])
print("1:5 ->", s[1:5])
print(":4 ->", s[:4])
print("2: ->", s[2:])
print("Full string ->", s[:])


print("\n===== SLICING WITH STEP =====")

print("0:6:2 ->", s[0:6:2])
print("1:6:2 ->", s[1:6:2])
print("::2 ->", s[::2])


print("\n===== REVERSE STRING =====")

print("Reverse ->", s[::-1])


print("\n===== LIST INDEXING & SLICING =====")

lst = [10, 20, 30, 40, 50, 60]

print("List:", lst)

print("First element:", lst[0])
print("Last element:", lst[-1])

print("0:3 ->", lst[0:3])
print("2:5 ->", lst[2:5])
print("::2 ->", lst[::2])
print("Reverse ->", lst[::-1])


friends=["apple",256,True,"rahul"]

friends[2]=25541

friends.append(False)

friend=[22,55,6,7,1,888,54,202,66]

friend.insert(3,88)
print(friend)

friend.pop(6)
friend.remove(54)
print(friend)


a=(45,"rahul",True,False,4856,"she is",45)
print(a.count(45))
print(a.count(61))
print(a.index(4856))

a=(45,5,6,8,9,6,)
b,c,d,e,f,g=a
print(b,c,d,e,f,g)


marks = {
    "shubham": 46,
    "rahul": 55,
    "mohan": 88,
    "subject": {
        1: "physics",
        2: "Hindi",
    },
    "list":[45,55,6,77],
}

print(marks["shubha"])