###########################################################
    #  Project 10
    #
    #  Prompts users for legal moves to the game Klondike
    #   If move is legal preform it and display board
    #   Else print error message and board
    #   Print win screen and winning board when plyer has won
    ###########################################################

from cards import Card, Deck

MENU ='''Prompt the user for an option and check that the input has the 
       form requested in the menu, printing an error message, if not.
       Return:
    TT s d: Move card from end of Tableau pile s to end of pile d.
    TF s d: Move card from end of Tableau pile s to Foundation d.
    WT d: Move card from Waste to Tableau pile d.
    WF d: Move card from Waste to Foundation pile d.
    SW : Move card from Stock to Waste.
    R: Restart the game (after shuffling)
    H: Display this menu of choices
    Q: Quit the game        
    '''
def initialize():
    "Initialize data structures for use in game and return said structures"
    Tableau = [[],[],[],[],[],[],[]]
    Foundations = [[],[],[],[]]
    Waste = []
    deck = Deck()
    deck.shuffle()
    for j in range(7):
        i = 6-j #start from left to right, skipping 1 more each time
        while i >= 0:
            Tableau[6-i].append(deck.deal())
            Tableau[6-i][-1].flip_card()
            i -= 1
    for i in Tableau:
        i[-1].flip_card()
    Waste.append(deck.deal())
    return(Tableau,deck,Foundations,Waste)

    
    
def display(tableau, stock, foundation, waste):
    """ display the game setup """
    stock_top_card = "empty"
    found_top_cards = ["empty","empty","empty","empty"]
    waste_top_card = "empty"
    if len(waste):
        waste_top_card = waste[-1] 
    if len(stock):
        stock_top_card = "XX" #stock[-1]
    for i in range(4):
        if len(foundation[i]):
            found_top_cards[i] = foundation[i][-1]
    print()
    print("{:5s} {:5s} \t\t\t\t\t {}".format("stock","waste","foundation"))
    print("\t\t\t\t     ",end = '')
    for i in range(4):
        print(" {:5d} ".format(i+1),end = '')
    print()
    print("{:5s} {:5s} \t\t\t\t".format(str(stock_top_card), str(waste_top_card)), end = "")
    for i in found_top_cards:
        print(" {:5s} ".format(str(i)), end = "")
    print()
    print()
    print()
    print()
    print("\t\t\t\t\t{}".format("tableau"))
    print("\t\t ", end = '')
    for i in range(7):
        print(" {:5d} ".format(i+1),end = '')
    print()
    # calculate length of longest tableau column
    max_length = max([len(stack) for stack in tableau])
    for i in range(max_length):
        print("\t\t    ",end = '')
        for tab_list in tableau:
            # print card if it exists, else print blank
            try:
                print(" {:5s} ".format(str(tab_list[i])), end = '')
            except IndexError:
                print(" {:5s} ".format(''), end = '')
        print()
    print()
    

def stock_to_waste( stock, waste ):
    "moves card from stock to waste"
    if not stock.is_empty():
        waste.append(stock.deal())
        return(True)
    else:
        return(False)
    
       
def waste_to_tableau( waste, tableau, t_num ):
    "Moves card from waste to specified collumn in tableau if move is legal, if not returns False"
    red = [2,3]
    black = [1,4]
    try:
        if waste[-1].suit() in red and tableau[t_num][-1].suit() in black or waste[-1].suit() in black and tableau[t_num][-1].suit() in red: #check for opposite suit
            if waste[-1].rank() + 1 == tableau[t_num][-1].rank():
                tableau[t_num].append(waste[-1]) #check for correct rank
                waste.pop(-1)
                return(True)
            else:
                return(False)
        else:
            return(False)
    except: #if empty list error occurs
        if len(tableau[t_num]) == 0 and waste[-1].rank() == 13: #if king
            tableau[t_num].append(waste[-1])
            waste.pop(-1)
            return(True)
        else:
            return(False)
        

def waste_to_foundation( waste, foundation, f_num ):
    "Moves card from waste to specified collumn in foundation if move is legal, if not return False"
    try:
        if waste[-1].suit() == foundation[f_num][-1].suit(): #check if suit is matching
            if waste[-1].rank() - 1 == foundation[f_num][-1].rank():
                foundation[f_num].append(waste[-1]) #checks that rank is appropriate
                waste.pop(-1)
                return(True)
            else:
                return(False)
        else:
            return(False) 
    except: #if empty list error occurs
        if waste[-1].rank() == 1: #if ace
            foundation[f_num].append(waste[-1])
            waste.pop(-1)
            return(True)
        else:
            return(False)

def tableau_to_foundation( tableau, foundation, t_num, f_num ):
    "Moves card from specified collumn of tableau to specified collumn in foundation if move is legal. Otherwise returns False"
    try:
        if tableau[t_num][-1].suit() == foundation[f_num][-1].suit(): #if suit is matching
            if tableau[t_num][-1].rank() - 1 == foundation[f_num][-1].rank(): #if rank is appropriate
                foundation[f_num].append(tableau[t_num][-1])
                tableau[t_num].pop(-1)
                if len(tableau[t_num]) != 0:
                    if tableau[t_num][-1].is_face_up() == False:
                        tableau[t_num][-1].flip_card()
                return(True)
            else:
                return(False)
        else:
            return(False)
    except: #if empty list error occurs
        if tableau[t_num][-1].rank() == 1: #if ace
            foundation[f_num].append(tableau[t_num][-1])
            tableau[t_num].pop(-1)
            if len(tableau[t_num]) != 0:
                if tableau[t_num][-1].is_face_up() == False:
                    tableau[t_num][-1].flip_card()
            return(True)
        else:
            return(False)

def tableau_to_tableau( tableau, t_num1, t_num2 ):
    "Moves card from specified collumn in tableau to specified collumn in tableau if move is legal. Otherwise returns False"
    red = [2,3]
    black = [1,4]
    try:
        if tableau[t_num1][-1].suit() in red and tableau[t_num2][-1].suit() in black or tableau[t_num1][-1].suit() in black and tableau[t_num2][-1].suit() in red: #checks for opposing suits
            if tableau[t_num1][-1].rank() + 1 == tableau[t_num2][-1].rank(): #checks for appropriate rank
                tableau[t_num2].append(tableau[t_num1][-1])
                tableau[t_num1].pop(-1)
                if len(tableau[t_num1]) != 0:
                    if tableau[t_num1][-1].is_face_up() == False:
                        tableau[t_num1][-1].flip_card()
                return(True)
            else:
                return(False)
        else:
            return(False)
    except: #empty list exception
        if len(tableau[t_num1]) == 0:
           return(False)
        elif tableau[t_num1][-1].rank() == 13:
            tableau[t_num2].append(tableau[t_num1][-1])
            tableau[t_num1].pop(-1)
            if len(tableau[t_num1]) != 0:
                if tableau[t_num1][-1].is_face_up() == False:
                    tableau[t_num1][-1].flip_card()
            return(True)
        else:
            return(False)
        
    
def check_win (stock, waste, foundation, tableau):
    "Checks if all win conditions are met, returns True if yes and False if not"
    win_con = 0
    if len(waste) == 0:
        win_con += 1
    for i in foundation:
        if len(i) == 13:
            win_con += 1
    for i in tableau:
        if len(i) == 0:
            win_con += 1
    if stock.is_empty() == True:
        win_con += 1
    if win_con == 13:
        return(True)
    else:
        return(False)

def parse_option(in_str):
    '''Prompt the user for an option and check that the input has the 
           form requested in the menu, printing an error message, if not.
           Return:
        TT s d: Move card from end of Tableau pile s to end of pile d.
        TF s d: Move card from end of Tableau pile s to Foundation d.
        WT d: Move card from Waste to Tableau pile d.
        WF d: Move card from Waste to Foundation pile d.
        SW : Move card from Stock to Waste.
        R: Restart the game (after shuffling)
        H: Display this menu of choices
        Q: Quit the game        
        '''
    option_list = in_str.strip().split()
    
    opt_char = option_list[0][0].upper()
    
    if opt_char in 'RHQ' and len(option_list) == 1:  # correct format
        return [opt_char]
    
    if opt_char == 'S' and len(option_list) == 1:
        if option_list[0].upper() == 'SW':
            return ['SW']
    
    if opt_char == 'W' and len(option_list) == 2:
        if option_list[0].upper() == 'WT' or option_list[0].upper() == 'WF':
            dest = option_list[1] 
            if dest.isdigit():
                dest = int(dest)
                if option_list[0].upper() == 'WT' and (dest < 1 or dest > 7):
                    print("\nError in Destination")
                    return None
                if option_list[0].upper() == 'WF' and (dest < 1 or dest > 4):
                    print("\nError in Destination")
                    return None
                opt_str = option_list[0].strip().upper()
                return [opt_str,dest]
                               
    if opt_char == 'T' and len(option_list) == 3 and option_list[1].isdigit() \
        and option_list[2].isdigit():
        opt_str = option_list[0].strip().upper()
        if opt_str in ['TT','TF']:
            source = int(option_list[1])
            dest = int(option_list[2])
            # check for valid source values
            if opt_str in ['TT','TF'] and (source < 1 or source > 7):
                print("\nError in Source.")
                return None
            #elif opt_str == 'MFT' and (source < 0 or source > 3):
                #print("Error in Source.")
                #return None
            # source values are valid
            # check for valid destination values
            if (opt_str =='TT' and (dest < 1 or dest > 7)) \
                or (opt_str == 'TF' and (dest < 1 or dest > 4)):
                print("\nError in Destination")
                return None
            return [opt_str,source,dest]

    print("\nError in option:", in_str)
    return None   # none of the above


def main():   
    "Manages above functions to allow user to play the game klondike"
    tableau = initialize()[0]
    stock = initialize()[1]
    foundation = initialize()[2]
    waste = initialize()[3]
    print(MENU)
    display(tableau,stock,foundation,waste)
    user_input = None
    cont = True
    try:
        while cont == True:
            while user_input == None:
                user_input = input("\nInput an option (TT,TF,WT,WF,SW,R,H,Q): " )
                user_input = parse_option(user_input)
                try:
                    if user_input[0] not in ("TT","TF","WT","WF","SW","R","H","Q"):
                        display(tableau,stock,foundation,waste)
                except:
                    display(tableau,stock,foundation,waste)
            if user_input[0] == "SW":
                if stock_to_waste(stock,waste):
                    display(tableau,stock,foundation,waste)
                else:
                    print("\nInvalid move!\n")
                    display(tableau,stock,foundation,waste)
            elif user_input[0] == "WF":
                if waste_to_foundation(waste,foundation,user_input[1]-1):
                    if check_win(stock,waste,foundation,tableau):
                        print("You win!")
                    display(tableau,stock,foundation,waste)
                else:
                    print("\nInvalid move!\n")
            elif user_input[0] == "WT":
                if waste_to_tableau(waste,tableau,user_input[1]-1):
                    display(tableau,stock,foundation,waste)
                else:
                    print("\nInvalid move!\n")
                    display(tableau,stock,foundation,waste)
            elif user_input[0] == "TF":
                if tableau_to_foundation(tableau,foundation,user_input[1]-1,user_input[2]-1):
                    if check_win(stock,waste,foundation,tableau):
                        print("You win!")
                    display(tableau,stock,foundation,waste)
                else:
                    print("\nInvalid move!\n")
                    display(tableau,stock,foundation,waste)
            elif user_input[0] == "TT":
                if tableau_to_tableau(tableau,user_input[1]-1,user_input[2]-1):
                    display(tableau,stock,foundation,waste)
                else:
                    print("\nInvalid move!\n")
                    display(tableau,stock,foundation,waste)
            elif user_input[0] == "H":
                print(MENU)
            elif user_input[0] == "R":
                Deck.shuffle()
                main()
            elif user_input[0] == "Q":
                cont = False
            user_input = None #handles loop error
    except:
        quit() #handles EOF error
if __name__ == '__main__':
     main()
