import csv

MENU = '''\nSelect an option from below:
            (1) Display all companies in the New York Stock Exchange
            (2) Display companies' symbols
            (3) Find max price of a company
            (4) Find the company with the maximum stock price
            (5) Find the average price of a company's stock
            (6) quit
    '''
WELCOME = "Welcome to the New York Stock Exchange.\n"

###########################################################
    #  Project 9
    #
    #  Program
    #    prompt for files
    #    input two file names
    #    prompt for integer
    #    loop while int != 6
    #       if int < 2 output formatted names or codes
    #       if 2 < int < 6 prompt for code
    #           if code is in list of codes output info depending on int
    #       if int == 6 exit program
    ###########################################################
 
def open_file():
    """
        open two files a price file and securities file
        returns file pointers for both files
    """
    try: #Handle EOF error
        cont = True
        while cont == True:
            file_name_p = input("\nEnter the price's filename: ")
            file_name_s = input("\nEnter the security's filename: ")
            try: 
                fp_p = open(file_name_p,"r")
                fp_s = open(file_name_s,"r")
                return(fp_p,fp_s) #return fp tuple
                cont = False
            except:
                print("\nFile not found. Please try again.") #invalid fp
    except:
        exit()       

def read_file(securities_fp):
    """
    takes a securities file pointer and returns a set of the company names and a dictionary with important info on companies
    """
    name_set = set({})
    master_dict = {}
    if securities_fp.name == "securities.csv": #if data is inbetween ""
        for line in securities_fp:
            line = line.split('","')
            line[0] = line[0].strip('"') #formatting
            line[7] = line[7].strip('"')
            line[7] = line[7].strip('\n')
            if line[0] == 'Ticker symbol': #skip first line
                continue
            name_set.add(line[1])
            master_dict[line[0]] = [line[1],line[3],line[4],line[5],line[6],[]]
    else: #if data is inbetween ,
        for line in securities_fp:
            line = line.split(",")
            if line[0] == 'Ticker symbol': #skip first line
                continue
            bridge = line[5].strip('"') + "," + line[6].strip('"') #formatting
            line.pop(5)
            line.pop(5)
            line.insert(5,bridge)
            line[0] = line[0].strip('"')
            line[1] = line[1].strip('"')
            name_set.add(line[1])
            master_dict[line[0]] = [line[1],line[3],line[4],line[5],line[6],[]]
    return(name_set,master_dict) #return set and dict
        
def add_prices (master_dictionary, prices_file_pointer):
    """
    takes the dictionary from read_file, and a prices file pointer, and adds the price data from the price file to the dictionary
    returns nothing
    """
    for line in prices_file_pointer:
        line = line.split(",")
        if line[0] == "\ufeffdate": #skip first line
            continue
        try: #add data to dictionary only if converting to float works
            master_dictionary[line[1]][5].append([line[0],float(line[2]),float(line[3]),float(line[4]),float(line[5])])
        except:
            continue
    
def get_max_price_of_company (master_dictionary, company_symbol):
    """
    takes the master dictionary, and a company code, and returns the max price of a company and the date of the price as a tuple, or returns (None,None)
    """
    max_list = []
    try: #if data doesn't work, then return (None,None) tuple
        for i in master_dictionary[company_symbol][5]:
            max_list.append((i[4],i[0]))
        max_price = max(max_list)
        return(max_price)
    except:
        return(None,None)
        

def find_max_company_price (master_dictionary):
    """
    takes the master dictionary, and returns the company with the highest max price, and the price itself
    """
    company_list = []
    max_price = ["",0]
    for i in master_dictionary:
        if get_max_price_of_company(master_dictionary,i)[0] != None: #checks that each company has a max price
            company_list.append((i,get_max_price_of_company(master_dictionary,i)[0]))
    for i in company_list: #finds max price of company list
        if i[1] > max_price[1]:
            max_price[0] = i[0]
            max_price[1] = i[1]
    return(tuple(max_price))


def get_avg_price_of_company (master_dictionary, company_symbol):
    """
    takes the master dictionary and a company code, and if the company code is valid it returns the company and the average price of the company
    """
    count = 0
    sum = 0
    try: #if index is in range
        price_list = master_dictionary[company_symbol][5] #makes a list of the prices for the company
        for i in price_list: #averages high price in price list
            sum += i[4]
            count += 1
        return(round(sum/count,2))
    except:
        return(0.0)

def display_list (lst):  # "{:^35s}"
    """
    takes a list of company names and prints it in a specific format
    """
    count = 1
    name_list_big = []
    name_list_small = []
    for i in lst:
        name_list_small.append(i) #makes a list of the company names
        if count % 3 == 0: #executes every 3 companies
            name_list_big.append(name_list_small)
            name_list_small = []
        count += 1
    else: #when the for loop is done
        if len(lst) % 3 == 1: #add last element as a list to big list
            name_list_big.append([lst[len(lst)-1]])
        elif len(lst) % 3 == 2: #add last 2 elements as a list to big list
            name_list_big.append([lst[len(lst)-1],lst[len(lst)-2]])
    for i in name_list_big:
        try:
            print("{:^35s}{:^35s}{:^35s}".format(i[0],i[1],i[2])) #prints 3 elements if possible
        except:
            try:
                print("{:^35s}{:^35s}".format(i[0],i[1])) #if not print 2 elements
                print("")
            except:
                print("{:^35s}".format(i[0])) #if not print the one element list
                print("")
    if len(lst) % 3 == 0:
        print("\n") #if the last line is 3 long print "\n"
    

def main():
    """
    takes an int as a user input and uses the above functions to output data until the user chooses option 6
    """
    print(WELCOME)
    fp = open_file()
    fp_p = fp[0]
    fp_s = fp[1]
    read_file_var = read_file(fp_s)
    name_list = list(read_file_var[0])
    name_list.sort()
    master_dict = read_file_var[1]
    code_list = []
    for i in master_dict:
        code_list.append(i)
    code_list.sort()
    add_prices(master_dict,fp_p)
    cont = True
    try:
        while cont == True:
            print(MENU)
            user_input = input("\nOption: ")
            try:
                user_input = int(user_input)
                if user_input < 1 or user_input > 6:
                    print("\nInvalid option. Please try again.")
            except:
                print("\nInvalid option. Please try again.")
            if user_input == 1:
                print("\n{:^105s}".format("Companies in the New York Stock Market from 2010 to 2016"))  
                display_list(name_list)
            elif user_input == 2:
                print("\ncompanies' symbols:")
                display_list(code_list)
            elif user_input == 3:
                while cont == True:
                    company_symbol = input("\nEnter company symbol for max price: ")
                    if company_symbol in master_dict.keys():
                        try: #if indice is in range
                            print("\nThe maximum stock price was ${:.2f} on the date {:s}/\n".format(get_max_price_of_company(master_dict,company_symbol)[0],get_max_price_of_company(master_dict,company_symbol)[1]))
                        except:
                            print("\nThere were no prices.") #if out of range then there were no prices
                        cont = False
                    else:
                        print("\nError: not a company symbol. Please try again.")
                cont = True
            elif user_input == 4:
                print("\nThe company with the highest stock price is {:s} with a value of ${:.2f}\n".format(find_max_company_price(master_dict)[0],find_max_company_price(master_dict)[1]))
            elif user_input == 5:
                while cont == True:
                    company_symbol = input("\nEnter company symbol for average price: ")
                    if company_symbol in master_dict.keys(): #if code is valid
                        print("\nThe average stock price was ${:.2f}.\n".format(get_avg_price_of_company(master_dict,company_symbol)))
                        cont = False
                    else:
                        print("\nError: not a company symbol. Please try again.") #if not valid reprompt for code
                cont = True
            elif user_input == 6:
                cont = False
                exit()
    except:
        exit() 
       
if __name__ == "__main__": 
    main() 
