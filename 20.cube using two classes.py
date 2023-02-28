class square():
    def number(self):
        self.a=int(input("The number to be find cube of="))
        print("THE input number is=",self.a)
class display():
    def cube(self):
        self.cube=self.a*self.a*self.a
        print("The cube of number is =",self.cube)
class output(square,display):
    def final(self):
        print("Hurray we got {} ".format(self.a))

obj=output()
obj.number()
obj.cube()
obj.final()
        
