import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    
    
    while True:
        cities = ['chicago', 'new york city', 'washington']
        city = input("Please choice the city you prefer:\n 'chicago', 'new york city', 'washington' : ").lower()
        if city in cities:
            break
        else:
            print("invalid city please re inpot")
    while True:
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
        month = input("Please choose a month you prefare:\n'january', 'february', 'march', 'april', 'may', 'june' or 'all': ").lower()
        if month in months:
            break
        else:
            print("invalid month input")
    while True:
        days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','all']
        day = input("Please choose a day:\n'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','all': ").lower()
        if day in days:
            break
        else:
            print("invalid day please re inpot input")
   # TO DO: get user input for month (all, january, february, ... , june)


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    if month!= 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("The most common month is: ", df['month'].mode()[0], "\t")

    # TO DO: display the most common day of week
    print(", And The most common day of week  is: ", df['day_of_week'].mode()[0], "\t")

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("T, And The most common start hour is: ", df['hour'].mode()[0], "\t")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most commonly start station is: ", df['Start Station'].mode()[0], "\t")


    # TO DO: display most commonly used end station
    print(". And The most popular End station: ",df['End Station'].mode()[0], "\t")

    # TO DO: display most frequent combination of start station and end station trip
    df['start_and_end']=df['Start Station']+"   to   "+ df['End Station']
    print("The most used start and end stations is:",df['start_and_end'].mode()[0], "\t")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['travel_du']=df['End Time'].astype('datetime64[D]')-df['Start Time'].astype('datetime64[D]')
    print("Total travel time:\t",df['travel_du'].sum())

    # TO DO: display mean travel time
    print("The total mean time for travel duration is: ", df['travel_du'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("The count of user types:\n", df['User Type'].value_counts())
    
    # Display counts of gender
    if "Gender" in df.columns:
        print("The counts of gender:\n", df['Gender'].value_counts())

     
    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print("The earliest year of birth: " + df['Birth Year'].min() + "\n" + "The most recent year of birth: " + df['Birth Year'].max() + "\n" + "The most common year of birth: " + df['Birth Year'].mode()[0] + "\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    x = 1
    while True:
        raw = input('\nWould you like to see some raw data? Enter yes or no.\n')
        if raw.lower() == 'yes':
            print(df[x:x+5])
            x = x+5
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
