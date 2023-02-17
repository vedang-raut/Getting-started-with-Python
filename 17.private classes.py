class a():
    def __init__(self):
        self.a=input("Enter a string")
        print(self.a)

class b(a):
    def __init__(self):
        print("It is private ")
        super().__init__()



obj=b()
