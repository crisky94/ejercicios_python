# i. Crea una clase Auto y una clase Concesionaria para gestionar autos.
class Auto:
    def __init__(self, brand, model, doors_number):
        self.brand = brand
        self.model = model
        self.doors_number = doors_number
    def __str__(self):
        return f'brand:{self.brand}, model:{self.model}, doors number:{self.doors_number}'

class Concesionaria:
    def __init__(self):
        self.cars = []
    
    def add_cars(self, car):

        self.cars.append(car)
        print(f'Add car {car}')

    def remove_cars(self, model):
        
        for car in self.cars:
            if car.model == model:
               self.cars.remove(model)
               return
        print(f'The model {model}, not found')

    def get_cars(self):
            
            if not self.cars:
                print('Is Empty')
            else:
                for car in self.cars:
                    print(f'-{car}')


car1 = Auto('citroen', 'c5', 5)
car2 = Auto('toyota', 'Land Cruiser', 5)
car3 = Auto('kia', 'sportage', 5)

concesionaria = Concesionaria()

concesionaria.add_cars(car1)
concesionaria.add_cars(car2)
concesionaria.add_cars(car3)

concesionaria.get_cars()
