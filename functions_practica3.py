class Carro:
    def __init__ (self, nombreDelC, velocidadDelC):
        self.name = nombreDelC
        self.velocidad = velocidadDelC
    def run_self(self):
        print(f"The car named {self.name} run at {self.velocidad} km/h")
    def name_car(self):
        print(self.name)    
    
c1 = Carro("Honda", 80)
c2 = Carro("Mazda", 85)
c1.run_self()
c2.run_self()
print(c1.name)

class Person:
    def __init__ (self, Name, age, car):
        self.name = Name
        self.age = age
        self.car = car
    def introduce_self(self):
        print(f"Mi nombre es {self.name} mi carro es {p1.car.name}")

p1 = Person("Julia", 24, c2)
p1.introduce_self()
p1.car.name_car()
        
    


    


    
    