import math
cost_int = 0
class_cd = 0
days_int = 0
od_strt_int = 0
od_end_int = 0
cont = 0
od_end_int_real = 0
od_total_int = 0
weeks_int = 0
print("Welcome to Horizons car rentals.")
print()
print("At the prompts, please enter the following: ")
print("Customer's classification code (a character: BD, D, W) ")
print("Number of days the vehicle was rented (int)")
print("Odometer reading at the start of the rental period (int)")
print("Odometer reading at the end of the rental period (int)")
print()
cont = input("Would you like to continue? (A/B) ")
print()
while not(cont == "A" or cont == "done"): #intial check for cont
    if cont == "B":
        print("Thank you for your loyalty.")
        exit()
    else:
        print("Invalid entry, please try again")
        cont = input("Would you like to continue? (A/B) ")


while cont == "A":
    class_cd = input("Customer code (BD, D, W): ")
    while not (class_cd == "BD" or class_cd == "D" or class_cd == "W"):
        print("*** Invalid customer code. Try again. ***")
        class_cd = input("Customer code (BD, D, W): ")
    days_int = input("Number of days: ")
    while not days_int.isdigit():
        print("Please enter an integer")
        days_int = input("Number of days: ")
    days_int = int(days_int)
    weeks_int = int(math.ceil(days_int/7))
    od_strt_int = int(input("Odometer reading at the start: "))
    od_end_int = int(input("Odometer reading at the end: "))
    if od_end_int < od_strt_int: #assigns a variable with od reading that is usable for math purposes
        od_end_int_real = od_end_int + 1000000
        od_total_int = od_end_int_real - od_strt_int
    else:
        od_total_int = od_end_int - od_strt_int
    if class_cd == "BD":
        cost_int = 40*days_int + od_total_int*.025
    elif class_cd == "D":
        if od_total_int / days_int > 1000:
            cost_int = (60*days_int) + (.025*((od_total_int)-(days_int*1000))) 
        else:
            cost_int = 60*days_int
    elif class_cd == "W":
        if od_total_int / weeks_int <= 9000:
            cost_int = 190*weeks_int
        elif od_total_int / weeks_int <= 15000:
            cost_int = 290*weeks_int
        else:
            cost_int = 390*weeks_int + .025*((od_total_int)-(15000*weeks_int))
    else:
        print("*** Invalid customer code. Try again. ***")
    print("Customer Summary: ")
    print("classification code:" + str(class_cd))
    print("rental period (days):" + str(days_int))
    print("odometer reading at start:" + str(od_strt_int))
    print("odometer reading at end:" + str(od_end_int))
    print("number of miles driven:" + str(od_total_int/10))
    print("amount due: $" + str(cost_int))
    print()
    cont = input("Would you like to continue? (A/B) ")
    print()
    while not(cont == "A" or cont == "done"):
        if cont == "B":
            print("Thank you for your loyalty.")
            cont = "done"
        else:
            print("*** Invalid customer code. Try again. ***")
            cont = input("Would you like to continue? (A/B) ")

"\nWelcome to Horizons car rentals. \
\n\nAt the prompts, please enter the following: \
\n\tCustomer's classification code (a character: BD, D, W) \
\n\tNumber of days the vehicle was rented (int)\
\n\tOdometer reading at the start of the rental period (int)\
\n\tOdometer reading at the end of the rental period (int)" 
 
PROMPT = '''\nWould you like to continue (A/B)? \n'''

"\nCustomer code (BD, D, W): \n"
"\nNumber of days: \n"
"Odometer reading at the start: \n"
"Odometer reading at the end:   \n"
"\n\t*** Invalid customer code. Try again. ***"
"\nCustomer summary:"
"\tclassification code:"
"\trental period (days):"
"\todometer reading at start:"
"\todometer reading at end:  "
"\tnumber of miles driven: "
"\tamount due: $"
"Thank you for your loyalty."
