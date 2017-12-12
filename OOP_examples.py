class Automobile:
  def __init__(self, numberOfWheels, make, model, topSpeed):

    self.numberOfWheels = numberOfWheels
    self.make = make
    self.model = model
    self.topSpeed = topSpeed
  
class Car(Automobile):
  
  def __init__(self, color):
    self.color = color
    super().__init__(4, "Subaru", "Orion", 95)

  def honk(self):
    
    print("Beep Beep!")

  def description(self):
    
    print("Number of Wheels: %d" % self.numberOfWheels)
    print("Make: %s" % self.make)
    print("Model: %s" % self.model)
    print("Color: %s" % self.color)
    print("Top Speed: %d" % self.topSpeed)

class Motorcycle(Automobile):
  
  def __init__(self, color):
    self.color = color
    super().__init__(2, "Beamer", "1290", 99)
    
class SemiTruck(Automobile):
  
  def __init__(self, color):
    self.color = color
    super().__init__(6, "Scion", "12 Omata", 88)

  def printModel(self):
    print(self.model)
    
    
myCar = Car("red")
myCar.description()

mySemiTruck = SemiTruck("black")
mySemiTruck.returnModel()
