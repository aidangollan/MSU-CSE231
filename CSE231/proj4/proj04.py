import math
EPSILON = 0.0000001

MENU = '''\nOptions below:
    ‘F’: Factorial of N.
    ‘E’: Approximate value of e.
    ‘P’: Approximate value of Pi.
    ‘S’: Approximate value of the sinh of X.
    ‘M’: Display the menu of options.
    ‘X’: Exit.
'''

def factorial(N): 
    try:     #if error pops up know N isn't positive int
        N = int(N)
        if N >= 0: #positive check
            sum = 1
            count = 1
            while count <= N: #stops program when count > N
                sum = sum*count
                count = count + 1
            return(sum)
        else:
            return(None)
    except:
        return(None)
def e(): 
    n = 0
    sum = 0
    while 1/math.factorial(n) > EPSILON: #continues while new addition is bigger than epsilon
        sum = sum + 1/math.factorial(n) #formula for new component of e
        n = n + 1
    return(round(sum,10))

def pi():
    n = 0
    sum = 0
    while abs((-1**n)/((2*n)+1)) > EPSILON: #continues while new addition is bigger than epsilon
        sum = sum + ((-1)**n)/((2*n)+1) #formula for new component of pi
        n = n + 1
    return(round(4*sum,10))

def sinh(x): 
    try: #if error pops up know x isn't float
        x = float(x)
        n = 0
        sum = 0
        while math.fabs((x**((2*n)+1))/math.factorial((2*n)+1)) > EPSILON: #continues while new element is less than epsilon
            sum = sum + (x**((2*n)+1))/math.factorial((2*n)+1)
            n = n + 1 #formula for new component of sinh
        return(round(sum,10))
    except:
        return(None)

def main(): 
    print(MENU)
    type = "" #initialize type var
    while type != "x": #while type isn't the stop type
        try:
            type = input("\nChoose an option: ").lower() #initial input formatted to lower
            if type == "f":
                print("\nFactorial")
                user_input = input("Input non-negative integer N: ") #asks for pos N
                if factorial(user_input) != None: #if no error was detected
                    print("\nCalculated: " + str(factorial(user_input)))
                    print("Math: " + str((math.factorial(int(user_input)))))
                    print("Diff: " + str((factorial(user_input))-(math.factorial(int(user_input))))) #output for the 3 types
                else: #if error was detected
                    print("\nInvalid N.")
            elif type == "e":
                print("\ne")
                print("Calculated: " + str(round(e(),10)))
                print("Math: " + str(round(math.e,10)))
                print("Diff: {:.10f}".format(float((math.e-e())))) #output for the 3 types
            elif type == "p":
                print("\npi")
                print("Calculated: " + str(round(pi(),10)))
                print("Math: " + str(round(math.pi,10)))
                print("Diff: {:.10f}".format(float(math.pi-pi()))) #output for the 3 types
            elif type == "s":
                print("\nsinh")
                user_input = input("X in radians: ") #asks for float x value
                if sinh(user_input) != None: #if no error was detected
                    print("\nCalculated: " + str(round(sinh(user_input),10)))
                    print("Math: " + str(round(math.sinh(float(user_input)),10)))
                    print("Diff: {:.10f}".format(math.fabs(sinh(user_input)-math.sinh((float(user_input)))))) #output for 3 types asked
                else: #if error with input was detected
                    print("\nInvalid X.")
            elif type == "m":
                main() #calls main function
            elif type == "x": #if user wants to end
                print("\nThank you for playing.") 
            else: #if no valid input was detected
                print("\nInvalid option: " + type.upper())
                main() 
        except:
            exit() #ends program
    else:   
        exit() #ends program
# These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.  
if __name__ == '__main__': 
    main()