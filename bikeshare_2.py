import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'C:/Users/AMAL/myfile/pdsnd_github/chicago.csv',
              'new york city': 'C:/Users/AMAL/myfile/pdsnd_github/new_york_city.csv',
              'washington': 'C:/Users/AMAL/myfile/pdsnd_github/washington.csv' }

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
        try :
            city = input("Please choose a city (chicago, new york city, washington) by writing it here:  ")
            city =city.lower()
            if city not in CITY_DATA:
                raise ValueError(f'You entered {city}, which is not in US bikeshare data.')
            else:
                break
        except (ValueError, KeyboardInterrupt):
            print("Please try again!")


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try :
            month = input("Please choose a month (all, january, february, ... , june) by writing it here:  ")
            month =month.lower()
            if month not in ['all', 'january', 'february','march','april','may','june']:
                raise ValueError(f'You entered {month}, which is not in US bikeshare data.')
            else:
                break
        except (ValueError, KeyboardInterrupt):
            print("Please try again!")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try :
            day = input("Please choose a day of week (all, monday, tuesday, ... sunday) by writing it here:  ")
            day =day.lower()
            if day not in ['all', 'monday', 'tuesday','wednesday','thursday','friday','saturday','sunday']:
                raise ValueError(f'You entered {day}, which is not in US bikeshare data.')
            else:
                break
        except (ValueError, KeyboardInterrupt):
            print("Please try again!")




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
      # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = pd.DatetimeIndex(df['Start Time']).month
    df['day_of_week'] = pd.DatetimeIndex(df['Start Time']).day_name()


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)
    
        # filter by month to create the new dataframe
        df = df.loc[df['month']==(month+1)]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df.loc[df['day_of_week']==day.title()]
    
    df.reset_index(drop=True, inplace=True)
    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    popular_month = df['month'].mode()[0]
    print('The most common month : ',months[popular_month-1].title())

    # TO DO: display the most common day of week    
    popular_day_of_week = df['day_of_week'].mode()[0]
    print('The most common day of week : ',popular_day_of_week)

    # TO DO: display the most common start hour
    df['hour'] =df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The most common start hour : ',popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station : ',start_station)

    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print('The most commonly used end station : ',end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['combination']=df['Start Station']+'] to ['+df['End Station']
    combination = df['combination'].mode()[0]
    print('The most frequent combination of start station and end station trip : from [',combination,']')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print('The total travel time ',total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print('The mean of travel time ',mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('The counts of user by types \n',df['User Type'].value_counts())


    if('Gender' in df):
        # TO DO: Display counts of gender
        print('The counts of user by gender \n',df['Gender'].value_counts())
        
        # TO DO: Display earliest, most recent, and most common year of birth
        print('The earliest year of birth amoung the user is ',df['Birth Year'].min())
        print('The most recent year of birth amoung the user is ',df['Birth Year'].max())
        print('The most common year of birth amoung the user is ',df['Birth Year'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def print_ndivilual_trip(df):
    counter=5
    while True:
        indivilual = input('\nWould you like to view indivilual trip data? Enter yes or no.\n')
        if indivilual.lower() == 'yes':
            for i in range(counter):
                print(df.loc[i].to_json())
            counter+=counter
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
        
        print_ndivilual_trip(df)

                
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
