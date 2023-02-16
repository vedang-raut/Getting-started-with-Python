class vedang():
    def num(self):
        self.a=int(input("Enter the first no:"))
        self.b=int(input("Enter the second no:"))
    def add (self):
        self.c=self.a+self.b
    def display(self):
        print("The addition is=",self.c)
obj=vedang()
obj.num()
obj.add()
obj.display()
