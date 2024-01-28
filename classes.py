class Vehicule:
    def __init__(self,  make, model):
        self.make = make
        self.model = model
    def moves(self):
        print('Moves along...')

    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}")

my_car = Vehicule('Tesla','Model 3')  #my car is an object
# print(my_car.make)
my_car.get_make_model()
my_car.moves()
print('-------------')
your_car = Vehicule('Cadillac','Escalade 2')
your_car.get_make_model()
your_car.moves()

#inheritance
class Airplane(Vehicule):
    def __init__(self,  make, model, faa_id):
        super().__init__(make, model)
        self.faa_id =  faa_id

    def moves(self):
        print('flies along...')

class Truck(Vehicule):
    def moves(self):
        print('rumbles along')

class Golf_cart(Vehicule):
    pass

print('-------------')
jumbo_jets = Airplane('Dassault', 'Falcon 8x', 211112 )
mack = Truck('Mack', 'Pinnacle' )
golfwagon = Golf_cart('Yamaha ', 'FA400' )

jumbo_jets.get_make_model()
jumbo_jets.moves()
print(jumbo_jets.faa_id)

mack.get_make_model()
mack.moves()

golfwagon.get_make_model()
golfwagon.moves()


print('\n\n')
print('Polymorphism')
# is the ability to behaviur differently and response to the same input messages
print('-------------')

for v in (my_car, your_car, jumbo_jets, mack, golfwagon):
    v.get_make_model()
    v.moves()
    print('******')
