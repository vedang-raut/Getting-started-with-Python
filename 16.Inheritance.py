class A():
    def a(self):
        self.a=int(input("Enter the number"))
        print("{}".format(self.a))
class B(A):
    def b(self):
        print("It is inherited in second",self.a)
class C(B):
    def c(self):
        self.b="It is your end"
        print(self.b)
        print(self.a)
obj=C()
obj.a()
obj.b()
obj.c()
        
