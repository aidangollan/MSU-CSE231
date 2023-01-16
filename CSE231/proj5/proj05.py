
import math

#Constants
PI = math.pi   
EARTH_MASS =  5.972E+24    # kg
EARTH_RADIUS = 6.371E+6    # meters
SOLAR_RADIUS = 6.975E+8    # radius of star in meters
AU = 1.496E+11             # distance earth to sun in meters
PARSEC_LY = 3.262

def open_file(): #open file function
    cont = 1
    file_name = input("Input data to open: ") + ".csv" #takes file name and appends .csv
    while cont == 1: #checks if it needs to repromt
        try:
            file = open(file_name,"r") #opens file
            return(file) #returns name for use
            cont = 0 #don't continue
        except FileNotFoundError: #if wrong file name
            print('\nError: file not found.  Please try again.')
            file_name = input("Enter a file name: ") + ".csv" #repromts for new file name

def make_float(s): #makes s a float, or returns -1 if doesn't work
    try: #if no errors are found return float(s)
        s = float(s)
        return(s)
    except ValueError: #if can't convert to float returns -1
        return(-1)

def get_density(mass, radius): #returns density
    if radius > 0 and mass > 0: #checks that radius and mass are non 0
        mass_kg = mass * EARTH_MASS #converts to correct units
        radius_m = radius * EARTH_RADIUS #converts to correct units
        return(mass_kg / ((4*math.pi*(radius_m**3))/3)) #returns density
    else:
        return(-1) #if radius or mass < 0 then returns -1

def temp_in_range(axis, star_temp, star_radius, albedo, low_bound, upp_bound): #finds if temp is in habitable range
    if axis > 0 and star_radius > 0: #if variables are >0 continue
        axis_m = axis * AU #converts to correct units
        star_radius_m = star_radius * SOLAR_RADIUS #converts to correct units
        planet_temp = star_temp * ((star_radius_m/(2*axis_m))**.5) * ((1-albedo)**.25) #finds planet temp
        if low_bound < planet_temp < upp_bound: #if in range
            return(True)
        else:
            return(False)
    else:
        return(False) #if axis or radius < 0

def get_dist_range(): #prompts for max distance and repromts until valid distance
    cont = 1
    while cont == 1: #checks if you need to reprompt
        distance = input("\nEnter maximum distance from Earth (light years): ") #input distance
        try: #checks if you can convert to float
            distance = float(distance) 
            if distance < 0: #checks if distance is <0
                print("\nError: Distance needs to be greater than 0.")
            else:
                return(distance / PARSEC_LY) #converts to correct units
                cont = 0
        except ValueError: #if can't convert to float
            print("\nError: Distance needs to be a float.")

def main(): #main function
    print('''Welcome to program that finds nearby exoplanets '''\
          '''in circumstellar habitable zone.''')
    file_name = open_file() #file name for reference
    distance_par = get_dist_range() #gets max distance
    low_bound = 200 #initializing variables
    upp_bound = 350
    albedo = .5
    total_mass = 0
    planet_count = 0
    max_planets = 0
    max_stars = 0
    habitable_planet_count = 0
    distance_min_gas = 1000000
    distance_min_rock = 1000000
    gas_plnt_count = 0
    rock_plnt_count = 0
    min_gas_name = ""
    min_rock_name = ""
    for line in file_name: #for each line in the file
        distance = make_float(line[slice(114,127)]) #converts planet distance to float
        if distance < 0 or distance > distance_par: #if distance = -1 or is bigger than max continue
            continue
        else:
            plnt_name = line[slice(25)].strip() #initialize variables
            num_star = make_float(line[slice(50,57)])
            num_plnt = make_float(line[slice(58,65)])
            axis_p = make_float(line[slice(66,77)])
            radius_p = make_float(line[slice(78,85)])
            mass_p = make_float(line[slice(86,96)])
            star_temp_p = make_float(line[slice(97,105)])
            star_radis_p = make_float(line[slice(106,113)])
            if mass_p != -1: #if mass = -1 don't count it towards total
                total_mass += mass_p
                planet_count += 1
            if num_plnt > max_planets: #calculates max planets
                max_planets = num_plnt
            if num_star > max_stars: #calculates max stars
                max_stars = num_star
            density_p = get_density(mass_p, radius_p) #gets density for planet
            in_range = temp_in_range(axis_p, star_temp_p, star_radis_p, albedo, low_bound, upp_bound) #check if planet is in range
            if in_range == True: #if in range
                habitable_planet_count += 1 #adds to count of habitable planets
                if 0 < mass_p < 10 or 0 < radius_p < 1.5 or density_p > 2000: #checks if rocky
                    rock_plnt_count += 1 #adds to rocky count
                    if distance * PARSEC_LY < distance_min_rock: #if distance is less than previous min distance
                        distance_min_rock = distance * PARSEC_LY
                        min_rock_name = plnt_name
                else: #if not rocky must be gassy
                    if distance * PARSEC_LY < distance_min_gas: #if distance is less than previous min distance
                        gas_plnt_count += 1 #adds to gassy count
                        distance_min_gas = distance * PARSEC_LY 
                        min_gas_name = plnt_name
    print("\nNumber of stars in systems with the most stars: {:d}.".format(int(max_stars))) #format output
    print("Number of planets in systems with the most planets: {:d}.".format(int(max_planets)))
    print("Average mass of the planets: {:.2f} Earth masses.".format(total_mass/planet_count))
    print("Number of planets in circumstellar habitable zone: {:d}.".format(int(habitable_planet_count)))
    if rock_plnt_count != 0: #if there are rocky planets
        print("Closest rocky planet in the circumstellar habitable zone {} is {:.2f} light years away.".format(min_rock_name,distance_min_rock))
    else: #if there are no rocky planets
        print("No rocky planet in circumstellar habitable zone.")
    if gas_plnt_count != 0: #if there are gassy planets
        print("Closest gaseous planet in the circumstellar habitable zone {} is {:.2f} light years away.".format(min_gas_name,distance_min_gas))
    else: #if there are no gassy planets
        print("No gaseous planet in circumstellar habitable zone.")
            

        
if __name__ == "__main__":
    main()