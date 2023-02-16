class vedang():
    def num(self):
        self.a=int(input("The no to be shown"))
        
    def square(self):
        self.c=self.a*self.a

    def display(self):
        print("the square of number {}".format(self.a), self.c)
obj=vedang()
obj.num()
obj.square()
obj.display()
    
