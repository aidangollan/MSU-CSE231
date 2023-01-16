
MENU = '''
 Menu : 
    1: Popular people (with the most friends). 
    2: Non-friends with the most friends in common.
    3: People with the most second-order friends. 
    4: Input member name, to print the friends  
    5: Quit                       '''
    
def open_file(s):
    try: #handle EOF error
        cont = 1
        while cont != 0: #while we want to re-prompt
            file_name = input("\nInput a {} file: ".format(s)) #ask for file name with proper prompt
            try:
                fp = open(file_name,"r") #open file
                cont = 0 #don't reprompt
                return(fp) #return file pointer
            except:
                print("\nError in opening file.") #error message
    except:
        exit() #handles EOF error

def read_names(fp): #reads name file and returns list of names
    out_list = [] #initializes list
    for line in fp: #For each name in the file
        line = line.strip("\n") #remove the new line formatting
        out_list.append(line) #add the name as a new element of the list
    return(out_list) #returns list of names

def read_friends(fp,names_lst): #reads friends file and returns list of friends
    out_list = [] #initializes list
    for line in fp: #for each person in the file
        line_list = [] #initializes a list to be reset once per line
        line = line.strip("\n") #turns line into list of numbers
        line = line.split(',')
        line.pop()
        for i in line: #for each number in line
            i = int(i) #turns i into int
            line_list.append(names_lst[i]) #adds correct name to list
        out_list.append(line_list) #adds list of names to final list
    return(out_list) #returns list of friends

def create_friends_dict(names_lst,friends_lst): #creates paired list of names and their friends
    big_list = zip(names_lst, friends_lst) #zips two together
    out_dict = {} #initializes dict
    for i in big_list: #for each pairing in big list
        out_dict[i[0]] = i[1] #creates a dict with the 2 elements
    return(out_dict) #returns dict

def find_common_friends(name1, name2, friends_dict): #finds common friends between 2 people
    name1_list = friends_dict[name1] #makes list of person one's friend's
    name2_list = friends_dict[name2] #makes list of person two's friend's
    cmn_name_list = [] #initializes common name list
    for i in name1_list: #for each element in list 1
        if i in name2_list: #checks if element is in list 2
            cmn_name_list.append(i) #adds element to common list
    cmn_name_list = set(cmn_name_list) #turns list into set
    return(cmn_name_list) #returns set

def find_max_friends(names_lst, friends_lst): #finds the person with the most friends
    friends_lst_new = [] #initializes lists
    max_list = []
    for i in friends_lst: #for each list of friends in friends list
        friends_lst_new.append(len(i)) #turn list into it's len
    for i in enumerate(friends_lst_new): #for each number in new list
        if i[1] == max(friends_lst_new): #if that number is the same as the max
            max_list.append(names_lst[i[0]]) #add the corrisponding name to list
    max_list.sort() #sort list
    return((max_list, max(friends_lst_new))) #makes tuple of max list and what that max is
           
def find_max_common_friends(friends_dict): #finds the people who have the max number of common friends
    possible_pairs = [] #initializes lists
    cmn_friends_list = []
    out_list = []
    for i in friends_dict: #loops through dict 1 time
        for j in friends_dict: #loops through dict again once for each element
            if i != j and [j,i] not in possible_pairs: #filters non compatible elements
                possible_pairs.append([i,j]) #adds element to possible pairs list
    for i in possible_pairs: #loops through possible pairs of people
        cmn_friends_list.append(len(find_common_friends(i[0],i[1],friends_dict))) #adds number of common friends to list
    for i in enumerate(cmn_friends_list): #goes through each pairing and their common friends
        if i[1] == max(cmn_friends_list): #if num of common friends is equal to the max
            out_list.append(tuple(possible_pairs[i[0]])) #add pairing of people to final list
    return(out_list,max(cmn_friends_list)) #returns list of pairs with max common friends, and what that max is
   
def find_second_friends(friends_dict): #makes list of exclusively second friends
    fof_dict = {} #initializes friend of friends dict
    for i in friends_dict: #loops over each name in friend dict
        fof_set = set() #intializes empty set
        for j in friends_dict[i]: #loops over each element that maps to i in dict
            fof_set.update(friends_dict[j]) #adds all friends of friends to fof set
        for k in friends_dict[i]: #loops through friends of person
            fof_set.discard(k) #removes all friends of original person 
        fof_set.discard(i) #removes person's name
        fof_dict[i] = fof_set #maps person's name to set of fof
    return(fof_dict) #returns fof dictionary

def find_max_second_friends(seconds_dict): #finds person with the most fof
    len_list = [] #initializes lists
    out_list = []
    names_list = []
    for i in seconds_dict: #loops through dictionary of fof
        len_list.append(len(seconds_dict[i])) #converts each entry to it's len
        names_list.append(i) #makes a list of names
    for i in enumerate(len_list): #loops through the list of lengths
        if i[1] == max(len_list): #if len value is equal to the max
            out_list.append(names_list[i[0]]) #adds name of person with max to final list
    return(out_list,max(len_list)) #returns final list

def main(): #main function coded mostly by teacher
    print("\nFriend Network\n")
    fp = open_file("names")
    names_lst = read_names(fp)
    fp = open_file("friends")
    friends_lst = read_friends(fp,names_lst)
    friends_dict = create_friends_dict(names_lst,friends_lst)

    print(MENU)
    choice = input("\nChoose an option: ")
    while choice not in "12345":
        print("Error in choice. Try again.")
        choice = input("Choose an option: ")
        
    while choice != '5':

        if choice == "1":
            max_friends, max_val = find_max_friends(names_lst, friends_lst)
            print("\nThe maximum number of friends:", max_val)
            print("People with most friends:")
            for name in max_friends:
                print(name)
                
        elif choice == "2":
            max_names, max_val = find_max_common_friends(friends_dict)
            print("\nThe maximum number of commmon friends:", max_val)
            print("Pairs of non-friends with the most friends in common:")
            for name in max_names:
                print(name)
                
        elif choice == "3":
            seconds_dict = find_second_friends(friends_dict)
            max_seconds, max_val = find_max_second_friends(seconds_dict)
            print("\nThe maximum number of second-order friends:", max_val)
            print("People with the most second_order friends:")
            for name in max_seconds:
                print(name)
                
        elif choice == "4": #prints list of names of friends for a specific person
            name_input = "" #initializes name variable
            while name_input not in friends_dict: #while name doesn't exist in file
                name_input = input("\nEnter a name: ") #prompts for name
                if name_input not in friends_dict: #tests if you need to do error message
                    print("\nThe name {} is not in the list.".format(name_input)) #prints error message
            print("\nFriends of {}:".format(name_input))
            for i in friends_dict[name_input]: #prints each name on a new line
                print(i)


        else: 
            print("Shouldn't get here.")
            
        choice = input("\nChoose an option: ")
        while choice not in "12345":
            print("Error in choice. Try again.")
            choice = input("Choose an option: ")

if __name__ == "__main__":
    main()
