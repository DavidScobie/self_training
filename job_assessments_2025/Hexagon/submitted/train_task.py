import numpy as np

###inputs for the train: EDIT THESE
engine_mass = 700 #engine coach (coach 1) mass in kg 
num_train_coaches = 6 #the number of coaches of the train (including the engine coach)
passenger_coach_fixed_masses = [400,500,650,350,600] #the fixed masses (in kg) of the passeneger coaches
shapes_of_coaches = ["cylinder","cuboid","sphere","cube","cone"] #the shapes of the passenger coaches 
dimensions_of_coaches = [[3,7],[5,9,8],[6],[5],[8,5]] #the dimensions (in metres) of each passeneger coach. See function volume_and_mass_of_a_given_coach(self,coach_number) for the input format for each shape.
num_passengers_each_coach = [1,2,3,1,2] #the number of passenegers on each of the passenger coaches
mass_each_passenger = [80,60,70,55,93,72,40,37,99] #the masses of the passengers in kg
luggage_masses = [10,5,7,15,10,0,30,10,12] #the luggage masses of the passengers in kg
coach_chosen = 4 #The coach that we want to find the mass and volume of. 1 is the engine coach. 2,3,4... are passenger coaches

def deal_with_missing_inputs(num_train_coaches,passenger_coach_fixed_masses,shapes_of_coaches,num_passengers_each_coach,mass_each_passenger,luggage_masses,coach_chosen):
    """
    what to do if some information about the train is missing
    """
    while len(passenger_coach_fixed_masses) < num_train_coaches - 1: #extend passenger_coach_fixed_masses
        passenger_coach_fixed_masses.append(round(sum(passenger_coach_fixed_masses)/len(passenger_coach_fixed_masses),1)) #append the average
    while len(mass_each_passenger) < sum(num_passengers_each_coach): #extend mass_each_passenger
        mass_each_passenger.append(round(sum(mass_each_passenger)/len(mass_each_passenger),1)) #append the average
    while len(luggage_masses) < sum(num_passengers_each_coach): #extend luggage_masses
        luggage_masses.append(round(sum(luggage_masses)/len(luggage_masses),1)) #append the average
    while len(shapes_of_coaches) < num_train_coaches - 1: #extend shapes_of_coaches
        shapes_of_coaches.append("cube")
    if (coach_chosen < 1) or (coach_chosen > num_train_coaches):
        raise ValueError("The coach selected (for requesting the mass and volume) must be within the range of the train's coaches")

    return num_train_coaches,passenger_coach_fixed_masses,shapes_of_coaches,num_passengers_each_coach,mass_each_passenger,luggage_masses,coach_chosen

num_train_coaches,passenger_coach_fixed_masses,shapes_of_coaches,num_passengers_each_coach,mass_each_passenger,luggage_masses,coach_chosen = deal_with_missing_inputs(num_train_coaches,passenger_coach_fixed_masses,shapes_of_coaches,num_passengers_each_coach,mass_each_passenger,luggage_masses,coach_chosen)

def find_passenger_list_indexes(num_passengers_each_coach,coach_chosen):
    """"
    find the indexes of the passengers for a chosen coach
    """
    if coach_chosen == 1: #first passenger coach (first index for this is 0)
        indexes = list(range(0,num_passengers_each_coach[0]))
    else: #the next passenger coaches (index depends on other indexes)
        indexes = list(range( sum(num_passengers_each_coach[:coach_chosen-1]) , num_passengers_each_coach[coach_chosen-1] + sum(num_passengers_each_coach[:coach_chosen-1] )))
    return indexes


###class for the train
class Train:
    def __init__(self, engine_mass, num_train_coaches, passenger_coach_fixed_masses, shapes_of_coaches, dimensions_of_coaches, num_passengers_each_coach, mass_each_passenger, luggage_masses): #always start with the constructor: __init__
        
        self.engine_mass = engine_mass      # attribute
        self.num_train_coaches = num_train_coaches  # attribute
        self.passenger_coach_fixed_masses = passenger_coach_fixed_masses      # attribute
        self.shapes_of_coaches = shapes_of_coaches  # attribute
        self.dimensions_of_coaches = dimensions_of_coaches  # attribute
        self.num_passengers_each_coach = num_passengers_each_coach  # attribute
        self.mass_each_passenger = mass_each_passenger      # attribute
        self.luggage_masses = luggage_masses      # attribute

        self.total_mass = 0 # attribute
        self.coach_mass = 0  # attribute
        self.coach_volume = 0  # attribute

    def total_luggage_mass(self): #method
        #add together all the luggage masses
        print(f"The total luggage mass in the train is {sum(self.luggage_masses)}kg.")

    def total_train_mass(self): #method
        #add together the masses of the luggage, engine, passengers and passenger coaches to get the total train mass
        self.total_mass += sum(self.luggage_masses)
        self.total_mass += self.engine_mass
        self.total_mass += sum(self.mass_each_passenger)
        self.total_mass += sum(self.passenger_coach_fixed_masses)
        print(f"The total mass of the train is {self.total_mass}kg.")

    def volume_and_mass_of_a_given_coach(self,coach_number): #method
        #find the volume and mass of a chosen coach
        if coach_number == 1: #engine coach
            self.coach_mass = self.engine_mass
            self.coach_volume = "undefined (as shape is not known) "
        else: #one of the passenger coaches
            ######### mass of this coach
            self.coach_mass += self.passenger_coach_fixed_masses[coach_number - 2] #add fixed mass for coach
            
            self.mass_each_passenger = np.array(self.mass_each_passenger) #turn to numpy array to help with the indexing
            self.coach_mass += sum(self.mass_each_passenger[find_passenger_list_indexes(self.num_passengers_each_coach,coach_chosen-1)])#add mass of passengers in this coach. The -1 accounts for the engine coach
            
            self.luggage_masses = np.array(self.luggage_masses) #turn to numpy array to help with the indexing
            self.coach_mass += sum(self.luggage_masses[find_passenger_list_indexes(self.num_passengers_each_coach,coach_chosen-1)])#add mass of the luggage of the passengers in this coach. The -1 accounts for the engine coach

            ########## volume of this coach
            if self.shapes_of_coaches[coach_number - 2] == "cylinder":
                # format for specifying "cylinder" in the dimensions_of_coaches list: [radius,length]
                radius = self.dimensions_of_coaches[coach_number - 2][0]
                length = self.dimensions_of_coaches[coach_number - 2][1]
                self.coach_volume += (np.pi * (radius**2)) * length
            if self.shapes_of_coaches[coach_number - 2] == "cuboid":
                # format for specifying "cuboid" in the dimensions_of_coaches list: [length,width,height]
                length = self.dimensions_of_coaches[coach_number - 2][0]
                width = self.dimensions_of_coaches[coach_number - 2][1]
                height = self.dimensions_of_coaches[coach_number - 2][2]
                self.coach_volume += length * width * height
            if self.shapes_of_coaches[coach_number - 2] == "sphere":
                # format for specifying "sphere" in the dimensions_of_coaches list: [radius]
                radius = self.dimensions_of_coaches[coach_number - 2][0]
                self.coach_volume += (4/3)*(np.pi)*(radius**3)
            if self.shapes_of_coaches[coach_number - 2] == "cube":
                # format for specifying "cube" in the dimensions_of_coaches list: [length]
                length = self.dimensions_of_coaches[coach_number - 2][0]
                self.coach_volume += (length**3)
            if self.shapes_of_coaches[coach_number - 2] == "cone":
                # format for specifying "cone" in the dimensions_of_coaches list: [radius,height]
                radius = self.dimensions_of_coaches[coach_number - 2][0]
                height = self.dimensions_of_coaches[coach_number - 2][1]
                self.coach_volume += (1/3)*(np.pi)*(radius**2)*height
 
        if coach_number == 1: #the engine coach doesnt have a shape specified
            print(f"The total mass and volume of coach {coach_number} are {self.coach_mass}kg and {self.coach_volume}respectively")
        else: #the passenger coaches do have a shape specified
            print(f"The total mass and volume of coach {coach_number} are {self.coach_mass}kg and {round(self.coach_volume,2)}m^3 respectively")

# Create the object
my_train = Train(engine_mass, num_train_coaches, passenger_coach_fixed_masses, shapes_of_coaches, dimensions_of_coaches, num_passengers_each_coach, mass_each_passenger, luggage_masses)   

my_train.total_luggage_mass() #calculate and print the luggage mass
my_train.total_train_mass() #calculate and print the total train mass
my_train.volume_and_mass_of_a_given_coach(coach_chosen) #calculate and print the mass and volume of a specified coach