# -*- coding: utf-8 -*-

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['all','january', 'february', 'march', 'april', 'may', 'june']

days = ['all','saturday', 'sunday','monday', 'tuesday', 'wednesday', 'friday']
 
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    #assign initial values of strings city, month and day to empty string
    city_input=''
    month_input=''
    day_input=''
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while city_input.lower() not in CITY_DATA:
        city_input = input("\nWhat is the name of the city to analyze data? Choose chicago or new york city or washington\n")
        if city_input.lower() in CITY_DATA:
            #get the name of the city
            city = CITY_DATA[city_input.lower()]
            
        else:
            #wrong input for the name of city
            print("Wrong Choice for the city name, Please enter chicago or new york city or washington.\n")

    # get user input for month (all, january, february, ... , june)
    
    while month_input.lower() not in months:
        month_input = input("\nWhat is the  month to analyze data?Choose 'all' or  january or february, ... , june\n")
        if month_input.lower() in months:
            #get the month
            month = month_input.lower()
        else:
            #wrong input for the month
            print("Wrong Choice for the month, Please enter 'all' or january, february, ... , june.\n")


    # get user input for day of week (all, monday, tuesday, ... sunday)
   
    while day_input.lower() not in days:
        day_input = input("\nWhat is the  day to analyze data?Choose 'all' or saturday, sunday, ... , friday\n")
        if day_input.lower() in days:
            #get the day
            day = day_input.lower()
        else:
            #wrong input for the day
            print("Wrong Choice for the day, Please enter 'all' or saturday, sunday, ... , friday\n")

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
    df = pd.read_csv(city)
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df["day_of_week"] =df["Start Time"].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = months.index(month)
        # filter by month to create the new dataframe
        df = df.loc[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df.loc[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    
    print('Most commen month is : {} '.format(df['month'].mode()[0]))
    
    # display the most common day of week
    
    print("The most common day is: " + str(df['day_of_week'].mode()[0]))

    # display the most common start hour
     
    print("The most common start hour is: " + str(df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station is: {}".format(common_start_station))

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station is: {}".format(common_end_station))

    # display most frequent combination of start station and end station trip
    frequent_combination = (df['Start Station'] + "||" + df['End Station']).mode()[0]
    print("The most frequent combination of start station and end station trip is : " + str(frequent_combination.split("||")))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time is: {}".format(str(total_travel_time)))

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time is: {}".format(str(mean_travel_time)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The count of user types is: {} \n".format(str(user_types)))

    # Display counts of gender
    if city == 'chicago.csv' or city == 'new_york_city.csv':
        gender = df['Gender'].value_counts()
        print("The count of user gender is: {} \n".format(str(gender)))

        # Display earliest, most recent, and most common year of birth
        earliest_birth = df['Birth Year'].min()
        most_recent_birth = df['Birth Year'].max()
        most_common_birth = df['Birth Year'].mode()[0]
        print('Earliest birth is: {}\n'.format(earliest_birth))
        print('Most recent birth is: {}\n'.format(most_recent_birth))
        print('Most common birth is: {}\n'.format(most_common_birth) )


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_five_raw(df):
    
   # Displays 5 raw data.
    
    print(df.head())
    next = 0
    while True:
        raw_data = input('\nWant to see next five row of raw data? Enter yes or no.\n')
        if raw_data.lower() != 'yes':
            return
        next = next + 5
        print(df.iloc[next:next+5])

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        
        while True:
            raw_data = input('\nWant to see first five row of raw data? Enter yes or no.\n')
            if raw_data.lower() != 'yes':
                break
            display_five_raw(df)
            break
        
        restart = input('\nDo yo want to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
