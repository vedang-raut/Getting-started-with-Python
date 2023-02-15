class person:
    def __init__(self):
        self.name="Vedang"
        self.phone=9022731826
        self.mob="Sam"
    def details(self):
        print("The details",self.name)
        print("NUM",self.phone)

    def mobile(self):
        if self.mob=="Iphone":
            print("The ios ")
        elif self.mob=="Sam":
            
            print("samsung")
obj=person()
obj.details()
obj.mobile()
            
