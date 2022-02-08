class Car():
    def __init__(self,width,height,color):
        self.width=width
        self.height=height
        self.color=color
    def run (self):
        print ("I like speed") 
    def speed (self):
        print ("Goooooo")




car1=Car(70,10,"red")
car1.run()
car1.speed()