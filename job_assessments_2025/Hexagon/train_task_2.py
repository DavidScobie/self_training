import numpy as np

class Passenger:
    def __init__(self, p_mass, lug_mass):
        self.p_mass = p_mass
        self.lug_mass = lug_mass

    def p_and_lug_mass(self):
        return self.p_mass + self.lug_mass


class Carriage:
    def __init__(self, letter, c_fixed_mass, shape, dims):
        self.letter = letter
        self.c_fixed_mass = c_fixed_mass
        self.shape = shape
        self.dims = dims
        self.passengers = []

    def add_passenger(self, passenger):
        self.passengers.append(passenger)

    def c_p_and_lug_mass(self):
        p_and_lug_mass_this_c = sum(p.p_and_lug_mass() for p in self.passengers)
        return self.c_fixed_mass + p_and_lug_mass_this_c

    def lug_mass_this_carriage(self):
        lug_mass_this_c = sum(p.lug_mass for p in self.passengers)
        return lug_mass_this_c 

    def v_this_carriage(self):
        if self.shape == "cylinder": # format for specifying "cylinder": [radius,length]
            radius = self.dims[0]
            length = self.dims[1]
            vol_this_c = (np.pi * (radius**2)) * length
        if self.shape == "cuboid": # format for specifying "cuboid": [length,width,height]
            length = self.dims[0]
            width = self.dims[1]
            height = self.dims[2]
            vol_this_c = length * width * height
        if self.shape == "sphere": # format for specifying "sphere": [radius]
            radius = self.dims[0]
            vol_this_c = (4/3)*(np.pi)*(radius**3)
        if self.shape == "cube": # format for specifying "cube": [length]
            length = self.dims[0]
            vol_this_c = (length**3)
        if self.shape == "cone": # format for specifying "cone": [radius,height]
            radius = self.dims[0]
            height = self.dims[1]
            vol_this_c = (1/3)*(np.pi)*(radius**2)*height
        return round(vol_this_c,2)


class Train:
    def __init__(self,e_mass):
        self.e_mass = e_mass
        self.carriages = []

    def add_carriage(self, carriage):
        self.carriages.append(carriage)

    def total_train_mass(self):
        return self.e_mass + sum(c.c_p_and_lug_mass() for c in self.carriages)

    def mass_and_vol_each_c(self):
        #dict comprehension where the coach letter is the key, and the coach mass and volume are made into a string for each coach 
        return {c.letter: f"mass={c.c_p_and_lug_mass()}kg, volume={c.v_this_carriage()}m^3" for c in self.carriages}

    def total_train_lug_mass(self):
        return sum(c.lug_mass_this_carriage() for c in self.carriages)
        

# passenger details (masses in kg)
p1 = Passenger(70,10)
p2 = Passenger(60,5)
p3 = Passenger(80,15)

# carriage details (lengths in metres, mass in kg)
cA = Carriage("A",1000,"cylinder",[3,7])
cB = Carriage("B",1200,"cuboid",[3,6,2])

# Add passengers to carriages
cA.add_passenger(p1)
cA.add_passenger(p2)
cB.add_passenger(p3)

# Make train and add carriages
train = Train(800)
train.add_carriage(cA)
train.add_carriage(cB)

#prints
print("Total luggage mass: ",train.total_train_lug_mass())
print("Total train mass:", train.total_train_mass())

coach_chosen="B" #what coach to find the mass and volume of
print(f"Mass and volume for coach",coach_chosen,':',train.mass_and_vol_each_c()[coach_chosen])

