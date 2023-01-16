import csv
from operator import itemgetter

NAME = 0
ELEMENT = 1
WEAPON = 2
RARITY = 3
REGION = 4

MENU = "\nWelcome to Genshin Impact Character Directory\n\
        Choose one of below options:\n\
        1. Get all available regions\n\
        2. Filter characters by a certain criteria\n\
        3. Filter characters by element, weapon, and rarity\n\
        4. Quit the program\n\
        Enter option: "

INVALID_INPUT = "\nInvalid input"

CRITERIA_INPUT = "\nChoose the following criteria\n\
                 1. Element\n\
                 2. Weapon\n\
                 3. Rarity\n\
                 4. Region\n\
                 Enter criteria number: "

VALUE_INPUT = "\nEnter value: "

ELEMENT_INPUT = "\nEnter element: "
WEAPON_INPUT = "\nEnter weapon: "
RARITY_INPUT = "\nEnter rarity: "

HEADER_FORMAT = "\n{:20s}{:10s}{:10s}{:<10s}{:25s}"
ROW_FORMAT = "{:20s}{:10s}{:10s}{:<10d}{:25s}"

def open_file():
    try: #stop EOF error
        cont = 1
        while cont != 0: #while we want to keep asking for file
            file_name = input("Enter file name: ") #ask for file name
            try:
                file = open(file_name,"r") #open file
                cont = 0
                return(file) #return file pointer
            except:
                print("\nError opening file. Please try again.") #error message
    except:
        exit() #handle EOF error

def read_file(fp):
    list_of_tuples = [] #main list
    list_line = [] #list for each list in main list
    tuple_line = () #convert list_line to a tuple

    for line in fp: #for each list in main list
        list_line = line.split(",") #turn line into list
        try:
            if list_line[4] != "\n": #test for empty element
                tuple_line = (list_line[0],list_line[2],list_line[3],int(list_line[1]),list_line[4].rstrip("\n"),)
            else:
                tuple_line = (list_line[0],list_line[2],list_line[3],int(list_line[1]),None,)
        except:
            pass
        list_of_tuples.append(tuple_line) #add tuple to main list
    list_of_tuples.pop(0) #remove header
    return(list_of_tuples) #return main list

def get_characters_by_criterion(master_list, criteria, value):
    try: #test if criteria is an int
        criteria = int(criteria)
        if criteria == 3:
            value = int(value) #if criteria is 3 test if value can be converted to int
    except:
        return(None)
    list_true = [] #list of valid characters
    for i in master_list:
        if criteria != 3: #if value isn't an int, avoid lower() error
            try:
                if i[criteria].lower() == value.lower(): #if value at specified place is value we're looking for
                    list_true.append(i)
            except:
                pass
        else:
            try:
                if i[criteria] == value: #if value at specified place is value we're looking for
                    list_true.append(i)
            except:
                pass
    return(list_true) #return final list

        
def get_characters_by_criteria(master_list, element, weapon, rarity):
    narrowed_list = get_characters_by_criterion(master_list,1,element) #narrow by element
    narrowed_list = get_characters_by_criterion(narrowed_list,2,weapon) #narrow by weapon
    narrowed_list = get_characters_by_criterion(narrowed_list,3,rarity) #narrow by rarity
    return(narrowed_list) #return final list

def get_region_list  (master_list):
    list_regions = [] #list of regions
    for i in master_list:
        if list_regions.count(i[4]) == 0: #if the list of regions doesn't contain the region at place in master list
            if i[4] != None: #if the region isn't none
                list_regions.append(i[4])
    return(sorted(list_regions)) #returns final list sorted alphabetically 

def sort_characters (list_of_tuples):
    list_sorted = sorted(list_of_tuples, key = itemgetter(3), reverse = True) #sorts list by rarity, already sorted by name
    return(list_sorted) #return sorted list

def display_characters (list_of_tuples):
    if len(list_of_tuples) != 0: #if list_of_tuples isn't empty
        print(HEADER_FORMAT.format("Character", "Element", "Weapon", "Rarity", "Region")) #prints header
        for i in list_of_tuples:
            if i.count(None) == 0: #if no element of i is None
                print(ROW_FORMAT.format(i[0], i[1], i[2], i[3], i[4]))
            else: #if an element is None, (only last element)
                print(ROW_FORMAT.format(i[0], i[1], i[2], i[3], "N/A"))
    else:
        print("\nNothing to print.") #if list_of_tuples is empty

def get_option():
    user_input = input(MENU)
    try:
        user_input = int(user_input) #if input can be converted to int
        if 1 <= user_input <= 4: #if input is between 1 and 4
            return(user_input)
        else:
            print(INVALID_INPUT)
            get_option() #calls itself to prompt for new input
    except:
        print(INVALID_INPUT)
        get_option()
  
def main():
    cont_main = 1 #for looping
    fp = open_file()
    master_list = read_file(fp)
    while cont_main != 0: #while we want to loop
        user_input = get_option()
        if user_input == 1:
            print("\nRegions:")
            print(", ".join(get_region_list(master_list))) #turns list of regions into correct formatting
        elif user_input == 2:
            cont = 1 #for looping of criteria and value
            while cont != 0:
                criteria = input(CRITERIA_INPUT)
                try:
                    criteria = int(criteria)
                    if criteria < 1 or criteria > 4: #if criteria is not between 1 and 4
                        print(INVALID_INPUT)
                    else:
                        cont = 0 #don't want to loop
                except:
                    print(INVALID_INPUT) #if criteria can't be converted to int
            cont = 1 #allow for looping on value
            while cont != 0:
                value = input(VALUE_INPUT)
                if criteria == 3: #if value should be able to convert to int
                    try:
                        value = int(value)
                        cont = 0
                    except:
                        print(INVALID_INPUT)
                else:
                    cont = 0
            list_of_characters = get_characters_by_criterion(master_list,criteria,value)
            list_of_characters = sort_characters(list_of_characters)
            display_characters(list_of_characters)
        elif user_input == 3:
            cont = 1 #looping for rarity
            element = input(ELEMENT_INPUT)
            weapon = input(WEAPON_INPUT)
            while cont != 0:
                rarity = input(RARITY_INPUT)
                try:
                    rarity = int(rarity) #testing if it can be converted to int
                    cont = 0
                except:
                    print(INVALID_INPUT)
            list_of_characters = get_characters_by_criteria(master_list,element,weapon,rarity)
            list_of_characters = sort_characters(list_of_characters)
            display_characters(list_of_characters)
        elif user_input == 4:
            cont_main = 0 #stop looping





# DO NOT CHANGE THESE TWO LINES
#These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.  
if __name__ == "__main__":
    main()
    
