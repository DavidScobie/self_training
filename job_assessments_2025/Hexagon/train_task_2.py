"""
class Train:
    ##class attributes in here
    def __init__(self,engine_mass,num_carriages):
        self.engine_mass=engine_mass
        self.num_carriages=num_carriages

    def __str__(self):
        return f"This train has an engine mass of {self.engine_mass}kg and there are {self.num_carriages} carriages"

class Carriage(Train):
    ##class attributes in here
    def __init__(self,engine_mass,num_carriages,coach_mass,shape,num_passengers):
        super().__init__(engine_mass,num_carriages)
        self.coach_mass=coach_mass
        self.shape=shape
        self.num_passengers=num_passengers

    def __str__(self):
        return f"This coach is a {self.shape}, with a mass of {self.coach_mass}kg and there are {self.num_passengers} passengers onboard"

# class Passenger(Carriage):
#     ##class attributes in here
#     def __init__(self,passenger_mass,luggage_mass):
#         self.passenger_mass=passenger_mass
#         self.luggage_mass=luggage_mass

#     def __str__(self):
#         return f"This person has mass {self.passenger_mass}kg and their luggage mass is {self.luggage_mass}kg"

engine_mass = 700
num_carriages = 3

the_train = Train(engine_mass,num_carriages)
print(the_train)

carriage_1 = Carriage(engine_mass,num_carriages,coach_mass = 400,shape="cube",num_passengers=2)
print(carriage_1)


# Kev = carriage_1(80,10)
# print(Kev)
"""

class Passenger:
    all_mass = [] #class attribute
    luggage_mass = []
    def __init__(self,passenger_mass,luggage_mass,coach_letter):
        self.passenger_mass=passenger_mass #instance attribute
        self.luggage_mass=luggage_mass #instance attribute
        self.coach_letter=coach_letter #instance attribute
        Passenger.all_mass.append(self.passenger_mass) #append the class attribute with an instance attribute
        Passenger.all_mass.append(self.luggage_mass)
        Passenger.luggage_mass.append(self.luggage_mass)

mark = Passenger(80,10,"A")
abby = Passenger(60,15,"A")
print(sum(Passenger.all_mass))
print(sum(Passenger.luggage_mass))


class Carriage(Passenger):
    all_coach_mass = []
    def __init__(self,passenger_mass,luggage_mass,p_c_letter,c_c_letter,shape,dimensions,coach_mass):
        super().__init__(passenger_mass,luggage_mass,p_c_letter)
        self.p_c_letter=p_c_letter
        self.c_c_letter=c_c_letter
        self.coach_mass=coach_mass
        self.shape=shape
        self.dimensions=dimensions
        Carriage.all_coach_mass.append(self.coach_mass)

    # if self.p_c_letter == self.c_c_letter:
    #     print('Same carriage')

coach_A = Carriage("None","None","None","A","cube",[5],400) #the 3 Nones are because we dont want to override the passenger inputs
print(sum(Carriage.all_coach_mass))

##





