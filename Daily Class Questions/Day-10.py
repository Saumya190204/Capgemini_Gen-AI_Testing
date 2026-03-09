class College:
      c_name="JECRC"
      loc="Jaipur"
s1=College()
s2=College()
print(College)
print(s1)
print(s1.loc)
s1.loc="Delhi"
print(s1.loc)
s1.name="rahul"
print(s1.name)
print(s1)
print(s2.name)

class Car:
      Brand="Kia"
      Factory="Chennai"
      BrandOwner="Rahul"

c1=Car()
c1.name="Seltos"
c1.color="Black"
c1.model="Petrol"
print(c1.name)
print(c1.color)
print(c1.model)
print(c1.Brand)
print(c1.Factory)
print(c1.BrandOwner)


#CLASS ATTRIBUTES CAN BE FETCHED USING BOTH CLASSNAME AND OBJECT NAME BUT THE OBJECT ATTRIBUTES CANT BE FETCHED USING THE C;ASS NAME
class College:
      c_name="JECRC"
      loc="Jaipur"

      def __init__(self,name,age,roll_no,school,hometown):
            self.name=name
            self.age=age
            self.roll_no=roll_no
            self.school=school
            self.hometown=hometown
      def display(self):
            # print(self.name,self.age,self.roll_no,self.school,self.hometown,self.c_name,self.loc)
            print(self.name)
            print(self.age)
            print(self.roll_no)
            print(self.school)
            print(self.hometown)
            print(self.c_name)
            print(self.loc)
            
            
s1=College("rahul",25,"22BCON191","St.Anslems","Mumbai")
s2=College("saumya",22,"22bcon195","JV","Alwar")
s3=College("sam",29,"22bcon1978","STEPS","Lucknow")
print(s1.name,s1.age,s1.roll_no,s1.school,s1.hometown,s1.c_name,College.loc)
s2.display()
s3.display()


# TYPES OF METHODS (FUNCTIONS WRITTEN INSIDE A CLASS IS CALLED METHOD)
# THERE ARE THREE TYPES OF METHODS
# 1.OBJECT METHOD:is method ko use krke tum class attributes as well as object attributes dono ko call kr skte ho means jaise isse pehle wale code me humne do class attributes h(c_name="JECRC"
#       loc="Jaipur")  inko bhi hume display method ke thropugh print kiya h object attributes lke saath ..jin bhi method me hum self attribute use krte h wo h object method
# 2.CLASS METHOD: .forthis  we have to used a decorator class method .They can be called either through class  or through object
# 3.STATIC METHOD:


# class method example
class College:
      c_name="JECRC"
      loc="Jaipur"

      @classmethod
      def show(cls,obj):
            print("the college name is:",cls.c_name)
            print("the loaction is",cls.loc)
      
#  College.show()
s1=College()
s1.c_name="SKIT"
College.show(s1)



class Math:

    @staticmethod
    def add(a, b):
        return a + b

print(Math.add(5,3))


class College:
      c_name="JECRC"
      loc="Jaipur"

      @classmethod
      def show(cls):
            print("the class name is",cls.c_name)
            print("the location is",cls.loc)
College.show()
College.c_name="ABDCD"
College.show()