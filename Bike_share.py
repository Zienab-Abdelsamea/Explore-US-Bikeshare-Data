import time
import pandas as pd
import numpy as np





CITY_DATA = {'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv'}
months = ['january', 'february', 'march', 'april', 'may', 'june']
days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday' ]

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
        
    print('Hello! Let\'s explore some US bikeshare data!')
    #ask user to input the specific city he want to know about
    city = input("\nWhich city would you like to know data about?: chicago, new york city,or washington\n").lower() 
   
    # if user entered a wrong choice, program ask him to choose a valid choice
    while (city not in CITY_DATA):        
        print("Wrong choice,please enter a valid one")
        city = input("Which city would you like to know data about?: chicago, new york city, washington\n").lower()
   
    # ask user to input a specific month he want to know about
    month = input('\nWhich month would you like to know data about?: all, january, february, ... , june \n').lower()
    # if user entered a wrong choice, program ask him to choose a valid choice
    while (month != 'all' and month not in months):
        print("Wrong choice,please enter a valid one")
        month = input('Which month would you like to know data about?: all, january, february, ... , june \n').lower()
        
    # ask user to input a specific day he want to know about
    day = input('\nWhich day would you like to know data about?: all, monday, tuesday, ... sunday \n').lower()
    # if user entered a wrong choice, program ask him to choose a valid choice
    while (day != 'all' and day not in days):
        print("Wrong choice,please enter a valid one")
        day = input('Which day would you like to see data about?: all, monday, tuesday, ... sunday \n').lower()

    print('-' * 40)
    return city, month, day

        





def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df["day_of_month"] = df['Start Time'].dt.day
    df['hour'] = df["Start Time"].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df





def time_stats(df):
    """
         Displays statistics on the most frequent times of travel.
    """
        
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['month'].mode()[0]
    print('The most common month is: ',most_common_month)
    # display the most common day of week
    most_common_day_of_week=df['day_of_week'].mode()[0]
    print('The most common day of week is:',most_common_day_of_week)
    # display the most common day of month
    most_common_day_of_month = df["day_of_month"].mode()[0]
    print('The most common day of month is:',most_common_day_of_month)
    # display the most common start hour
    most_common_hour = df['hour'].mode()[0]
    print('The most common hour is:',most_common_hour)

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    





def station_stats(df):
    """
    Displays statistics on the most popular stations and trip.
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print("The most common start station is:",start_station)

    # display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print("The most common end station is:",end_station)

    # display most frequent combination of start station and end station trip
    common_start_end = (df["Start Station"] + '-' + df["End Station"]).mode()[0]
    
    print("The most frequent combination of start station and end station trip is:",common_start_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

    





def trip_duration_stats(df):
    """
    Displays statistics on the total and average trip duration.
    """
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time:",total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("mean travel time:",mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)





def user_stats(df):
    """
    Displays statistics on bikeshare users.
    """
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type = df["User Type"].value_counts()
    print("counts of user types: \n",user_type)

    # Display counts of gender
    # washington dataset has no gender, so if the user entered it
    # we throw an excecption: gender is not available
    try:
        gender = df["Gender"].value_counts()
        print("counts of user gender: \n",gender)
    except:
        print('No gender available in this Stats\n')

    # Display earliest , most recent, and most common year of birth
    # washington dataset has no birth year, so if the user entered it
    # we throw an excecption: birth year is not available
    try:
        earliest_year = int(df['Birth Year'].min())
        print("earliest year of birth:",earliest_year)
        
        most_recent_year = int(df['Birth Year'].max())
        print("most recent year of birth:",most_recent_year)
        
        most_common_year = int(df['Birth Year'].mode()[0])
        print("most common year of birth:",most_common_year)
    except:
        print('No birth year available in this Stats\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)





def show_data(df): 
    """
    show a sample of data
    """
    i = 5
    order = ''
    
    while order != "no" and "yes":
        
        order = input("Do you want to see a {} samples of data?: yes or no\n".format(i)).lower()
        
        if order == "no":
            break
            
        elif order == 'yes':
            print(df.head(i))
            print('-'*40)
            i += 5
            
        else:
            print("please enter a valid choice")    





def Restart():
    restart = input('\nWould you like to restart?,Please enter \"yes or no\".\n').lower()
    if restart == "yes":
        main()
    elif restart =="no":
        print('-'*40)
        print("Thanks for using my program!")
    else:
        print("enter a valid choice")
        Restart()





def main():
    city, month, day = get_filters()
    df = load_data(city, month, day)
    time_stats(df)
    station_stats(df)
    trip_duration_stats(df)
    user_stats(df)
    show_data(df)
    Restart()
        


if __name__ == "__main__":
	main()



