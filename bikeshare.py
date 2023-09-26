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
        city = input("Input City Name: ").lower()
        if city not in CITY_DATA.keys():
            print('City not in database, please type another city name')
            continue
        else:
            print(f"Thank you for choosing {city}")
            city
            break       
        

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        mth = input("Input Month Name: ")
        mth = mth.lower()
        months = ['all','january', 'february', 'march', 'april', 'may', 'june']
        if mth not in months:
            print('Invalid month, please type another month name')
            continue
        else:
            print(f"Thank you for choosing {mth}")
            month = mth
            break       

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        dow = input("Input day of week: ")
        dow = dow.lower()
        day_of_week = ['all','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday']
        if dow not in day_of_week:
            print('Invalid day of week, please type another day of week')
            continue
        else:
            print(f"Thank you for choosing {dow}")
            day = dow
            break

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
    df = pd.read_csv(CITY_DATA.get(city))
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # filter by month if applicable
    if month != 'all':
        df = df[df['month'] == month.title()]
    # filter by day of week if applicable
    if day != 'all':
    # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
   
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print(f"The most common month is {df['month'].mode()[0]}")

    # TO DO: display the most common day of week
    print(f"The most common day of week is {df['day_of_week'].mode()[0]}")

    # TO DO: display the most common start hour
    df['Start_hour'] = df['Start Time'].dt.hour
    print(f"The most common start hour is {df['Start_hour'].mode()[0]}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print(f"The most common Start Station is {df['Start Station'].mode()[0]}")

    # TO DO: display most commonly used end station
    print(f"The most common End Station is {df['End Station'].mode()[0]}")

    # TO DO: display most frequent combination of start station and end station trip
    df['Start_to_End Station'] = df['Start Station'] +' to '+ df['End Station']
    print(f"The most common Start to End Station is from {df['Start_to_End Station'].mode()[0]}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print(f"The total travel time is {df['Trip Duration'].sum()}")

    # TO DO: display mean travel time
    print(f"The mean travel time is {df['Trip Duration'].mean()}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(f"The counts of user types are given below: {df['User Type'].value_counts()}")

    # TO DO: Display counts of gender
    if city == 'washington' :
        pass
    else:
        # TO DO: Display counts f gender
        print(f"The count by gender is: {df['Gender'].value_counts()}")
        # TO DO: Display earliest, most recent, and most common year of birth
        print(f"The earliest year of birth is {df['Birth Year'].describe()[3]}, most recent year of birth is {df['Birth Year'].describe()[7]}, most common year of birth is {df['Birth Year'].mode()[0]}")
        
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    if view_data == "yes":
        start_loc = 0
        next_loc = 5
        while True:
            print(df.iloc[start_loc:next_loc])
            ques = input('\nDo you wish to continue to the next 5 rows of the data? Enter yes or no\n').lower()
            if (ques == 'no') or (next_loc + 5 > len(df)):
                break
            start_loc += 5
            next_loc += 5             

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df)
        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
