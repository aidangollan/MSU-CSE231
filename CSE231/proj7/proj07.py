
GENRES = ['Unknown','Action', 'Adventure', 'Animation',"Children's",
          'Comedy','Crime','Documentary', 'Drama', 'Fantasy', 'Film-noir',
          'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 
          'War', 'Western']
OCCUPATIONS = ['administrator', 'artist', 'doctor', 'educator', 'engineer',
               'entertainment', 'executive', 'healthcare', 'homemaker', 'lawyer',
               'librarian', 'marketing', 'none', 'other', 'programmer', 'retired',
               'salesman', 'scientist', 'student', 'technician', 'writer']
'''
Three main data structures (lists)
L_users, indexed by userID, list of tuples (age,gender,occupation)
L_reviews, indexed by userID, list of tuples (movieID, rating)
L_movies, indexed by movieID, list of tuples (movieName, releaseDate, list of genres)
'''
MENU = '''
        Options:
        1. Highest rated movie for a specific year
        2. Highest rated movie for a specific Genre
        3. Highest rated movies by a specific Gender (M,F)
        4. Highest rated movies by a specific occupation
        5. Quit
        '''
def open_file(s): #asks for valid file and returns file pointer
    try: #handle EOF error
        cont = 1
        while cont != 0: #while we want to re-prompt
            file_name = input("\nInput {} filename: ".format(s)) #ask for file name with proper prompt
            try:
                fp = open(file_name,"r",encoding ="windows-1252") #open file in windows-1252 encoding
                cont = 0 #don't reprompt
                return(fp) #return file pointer
            except:
                print('\nError: No such file; please try again.') #error message
    except:
        exit() #handles EOF error

def read_reviews(N,fp): #takes number of users and the file pointer and returns a list of review tuples
    list_of_lists = [[]] #initialize lists and tuples
    review_tuple = ()
    i = 0 
    while i < N: #initializes list_of_lists to proper length
        list_of_lists.append([])
        i += 1
    for line in fp: #breaks text up into list
        line = line.split()
        review_tuple = (int(line[1]),int(line[2])) #creates tuple
        list_of_lists[int(line[0])].append(review_tuple) #adds tuple to list
    for i in list_of_lists:
        i.sort() #sorts list
    return(list_of_lists)

def read_users(fp): #reads file pointer and returns list of user tuples
    list_of_tuples = [[]] #initializes lists and tuples
    user_tuple = ()
    for line in fp: #splits string into list
        line = line.strip("\n").split("|")
        user_tuple = (int(line[1]),line[2],line[3]) #creates tuple
        list_of_tuples.append(user_tuple) #adds tuple to list of tuples
    return(list_of_tuples)

def read_movies(fp): #takes file pointer and returns list of tuples of movies
    list_of_tuples = [[]] #initializes lists and tuples
    movie_tuple = ()
    for line in fp: #splits string into list
        genre_list = []
        line = line.strip("\n").split("|")
        line.pop(0) #removes first element of list
        for i in enumerate(line):
            if i[1] == "1": #adds movies to genre list if i[i] == "1"
                genre_list.append(GENRES[i[0]-4])
        movie_tuple = (line[0],line[1],genre_list) #makes movie tuple
        list_of_tuples.append(movie_tuple) #adds tuple to list
    return(list_of_tuples)
        
def year_movies(year,L_movies): #takes year and movie list and returns all movies of that year
    movie_ID_list = [] #initializes list
    for i in enumerate(L_movies): #goes line by line for L_movies
        try: #test if i is []
            if int(i[1][1][-4:]) == year: #if year on line == year
                movie_ID_list.append(i[0]) #adds i[0] to movie list
        except:
            pass
    return(movie_ID_list)


def genre_movies(genre,L_movies): #takes genre and movie list and returns all movies of that genre
    genre_ID_list = [] #initializes list
    for i in enumerate(L_movies): #goes line by line for movie list
        try:
            if check_match(genre,i[1][2]) != False: #if that element has the same genre as genre, add it to the list
               genre_ID_list.append(i[0]) 
        except:
            pass
    return(genre_ID_list)

def gen_users (gender, L_users, L_reviews): #takes gender, users, and reviews, and returns reviews by each person of that gender
    list_of_lists = [] #initializes lists
    for i in enumerate(L_users): #goes line by line
        try: #if i == []
            if gender == i[1][1]: #if gender in file == gender
                list_of_lists.append(L_reviews[i[0]]) #add their review to list
        except:
            pass
    return(list_of_lists)
          
def occ_users (occupation, L_users, L_reviews): #takes occupation, users, and reviews, and returns reviews by each person of that occupation
    list_of_lists = [] #initializes list
    for i in enumerate(L_users): #goes line by line
        try: #if i == []
            if occupation.lower() == i[1][2]: #if occupation in file is same as occupation
                list_of_lists.append(L_reviews[i[0]]) #adds review to list
        except:
            pass
    return(list_of_lists)

def highest_rated_by_movie(L_in,L_reviews,N_movies): #takes list of movies, reviews, and number of movies, and returns max average and a list of movies with that average
    rating_list = [] #initializes lists and variables
    rating_avg_list = []
    max_avg = 0
    movies_final_list = []
    avg = 0
    i = 0
    while i < N_movies: #initializes rating_list to proper length
        rating_list.append([0,0])
        i += 1
    for i in L_reviews:
        for j in i: #takes each individual review
            try: #if j == []
                if j[0] in L_in: #if movie in L_in
                    rating_list[j[0]][1] += 1 #adds 1 to count
                    rating_list[j[0]][0] += j[1] #adds rating to total
            except:
                pass
    for i in rating_list: #takes average for each total rating and count
        try: #if i == []
            avg = round(i[0] / i[1],2) #takes rounded average of each movie
            rating_avg_list.append(avg) #adds it to average list
        except:
            rating_avg_list.append(0.0) #if empty makes average 0.0
    max_avg = max(rating_avg_list) #finds max of averages
    for i in enumerate(rating_avg_list): #goes by each average
        if max_avg == i[1]: #if max average is the same as the average for the movie
            movies_final_list.append(i[0]) #add the movie to the list
    return(movies_final_list,max_avg)
           
def highest_rated_by_reviewer(L_in,N_movies): #takes list of movies and number of movies and returns max average and list of movies with that average
    in_list = [] #initializes list
    for i in L_in:
        for j in i: #goes by individual movie
            try:
                if j[0] not in in_list: #if the movie isn't in in_list
                    in_list.append(j[0]) #add to in_list
            except:
                pass
    return(highest_rated_by_movie(in_list,L_in,N_movies))
    
def check_match(S,L): #checks if a string is in a list, regardless of case
    TF = False #initializes booleen
    for i in L: 
        if S.lower() != i.lower(): #if string isn't i
            if TF != True: #if i doesn't already = True
                TF = False #make i false
        else: #if string is i
            TF = True #make TF Truw
    return(TF)

def main(): #main function, takes file names and user choices as inputs, and returns outputs from previous functions
    len_review = 0 #initialize variables
    cont = 1
    fp_users = open_file("users") #opens files
    fp_reviews = open_file("reviews") #opens files
    fp_movies = open_file("movies") #opens files
    users_list = read_users(fp_users) #makes user list
    num_users = len(users_list) - 1 #length of user list
    reviews_list = read_reviews(num_users,fp_reviews) #makes reviews list
    num_reviews = len(reviews_list) - 1 #length of reviews list
    movies_list = read_movies(fp_movies) #makes movies list
    num_movies = len(movies_list) - 1 #length of movies list
    print(MENU) #prints menu
    try: #deals with EOF error
        while cont != 0: #while we want to keep reprompting
            year = 0 #initializes variables to be reset each time
            option = 0
            genre_input = ""
            gender_input = ""
            occupation_input = ""
            while option < 1 or option > 5: #while we want to reprompt
                try: #test if input is int
                    option = int(input('\nSelect an option (1-5): ')) #converts to int
                    if option < 1 or option > 5: #if option is not in range
                        print("\nError: not a valid option.")
                except: #if option is not int
                    print("\nError: not a valid option.")
                    option = 0 #avoid error with while statement
            if option == 1: #input from above
                while year < 1930 or year > 1998: #while in range
                    year = input('\nInput a year: ')
                    try: #tests for int
                        year = int(year)
                        if year < 1930 or year > 1998: #if year in range
                            print("\nError in year.")
                    except: #year not int
                        print("\nError in year.")
                        year = 0
                year_list = year_movies(year,movies_list) #makes list of movies in that year
                high_year = highest_rated_by_movie(year_list,reviews_list,num_movies) #makes list of highest avg and what movies
                print('\nAvg max rating for the year is: ' + str(high_year[1])) #prints highest avg
                for i in high_year[0]:
                    print(movies_list[i][0]) #prints what movies had that avg
            elif option == 2: #input from above
                print('\nValid Genres are:  {}'.format(GENRES)) #prints valid genres
                while check_match(genre_input,GENRES) == False: #while input isn't in Genres list   
                    genre_input = input('Input a genre: ') #ask for input
                    if check_match(genre_input,GENRES) == False:
                        print("\nError in genre.") #if not in genres display error message
                genre_list = genre_movies(genre_input,movies_list) #makes list of movies with that genre
                high_genre = highest_rated_by_movie(genre_list,reviews_list,num_movies) #makes list of highest avg and what movies have that avg
                print('\nAvg max rating for the Genre is: ' + str(high_genre[1])) #prints highest avg
                for i in high_genre[0]:
                    print(movies_list[i][0]) #prints movies with that avg
            elif option == 3: #input from above
                while gender_input != "M" and gender_input != "F": #while input isn't in range
                    gender_input = input('\nInput a gender (M,F): ').upper() #asks for input
                    if gender_input != "M" and gender_input != "F":
                        print("\nError in gender.") #if input isn't in range display error message
                gend_list = gen_users(gender_input,users_list,reviews_list) #makes list of movies by gender of reviewer
                high_gend = highest_rated_by_reviewer(gend_list,num_movies) #makes list of highest avg and what movies have that avg
                print('\nAvg max rating for the Gender is: ' + str(high_gend[1])) #prints highest avg
                for i in high_gend[0]:
                    print(movies_list[i][0]) #prints all movies with that avg
            elif option == 4: #input from above
                print('\nValid Occupatipns are:  {}'.format(OCCUPATIONS)) #displays valid occupations
                while check_match(occupation_input,OCCUPATIONS) == False: #while occupation input not in range
                    occupation_input = input('Input an occupation: ') #prompts for input
                    if check_match(occupation_input,OCCUPATIONS) == False: #checks if input is in range
                            print("\nError in occupation.") #displays error message
                occ_list = occ_users(occupation_input,users_list,reviews_list) #makes list of movies by the occupation of the reviewer
                high_occ = highest_rated_by_reviewer(occ_list,num_movies) #makes a list of the highest avg and the movies with that avg
                print('\nAvg max rating for the occupation is: ' + str(high_occ[1])) #prints highest avg
                for i in high_occ[0]:
                    print(movies_list[i][0]) #prints movies with that avg
            elif option == 5: #input from above
                fp_movies.close() #closes files
                fp_reviews.close()
                fp_users.close()
                cont = 0 #stops reprompting
    except:
        exit() #ends file


if __name__ == "__main__":
    main()
                                           
