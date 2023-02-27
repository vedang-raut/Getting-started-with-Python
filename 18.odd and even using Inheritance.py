class Vedang():
    def No(self):
        self.a=int(input("The Number to be checked"))
        print("The accepted Number is=",self.a)

class condition():
    def check(self):
        if self.a%2==0:
            print("The is even")
        else:
            print("Odd")

class final(Vedang,condition):
    def display(self):
        print("Hurray!! your condition is successfully checked")
obj=final()
obj.No()
obj.check()
obj.display()
