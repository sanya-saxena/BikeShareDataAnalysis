import time
import pandas as pd
import numpy as np
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """Gets inputs from user till valid input is received"""
    print('\nHello! Let\'s explore some US bikeshare data!')
    c = ['chicago','new york city','washington']
    while True:
        city = input("Which city's information do you want? Chicago/New York City/Washington\n").strip()
        if city.lower() in c:
            break
        else:
            print("You have entered wrong name of city. Please try again!")
    m = ['january','february','march','april','may','june','all']
    while True:
        month = input("Which month's data are you interested in? (January/February/March/April/May/June/All). Please enter only in lower case!\n").strip()
        if month in m:
            break
        else:
            print("You have entered wrong month. Please try again!")
    d = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']
    while True:
        day = input("Which day's data are you interested in? (Monday/Tuesday/Wednesday/Thursday/Friday/Saturday/Sunday/All). Please enter only in lower case!\n").strip()
        if day in d:
            break
        else:
            print("You have entered wrong day. Please try again!")

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """Reads corresponding CSV file"""
    df = pd.read_csv(CITY_DATA[city.lower()])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day.lower() != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    if popular_month == 1:
        popular_month = 'January'
    elif popular_month == 2:
        popular_month = 'February'
    elif popular_month == 3:
        popular_month = 'March'
    elif popular_month == 4:
        popular_month = 'April'
    elif popular_month == 5:
        popular_month = 'May'
    elif popular_month == 6:
        popular_month = 'June'
    print('Most Popular Month:',popular_month)
    # display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    popular_day = df['day_of_week'].mode()[0]
    print('Most Popular Day:',popular_day)
    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("Most Popular start station: ",popular_start_station)

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("Most Popular end station: ",popular_end_station)

    # display most frequent combination of start station and end station trip
    trip_series = df['Start Station'].astype(str) + " to " + df['End Station'].astype(str)
    most_popular_trip = trip_series.describe()["top"]
    print('Most Popular trip is from ',most_popular_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df['Trip Duration'].sum()
    print('Total travel time in seconds: ',total_time)

    # display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('Mean travel time in seconds: ',mean_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('Breakdown of users: ')
    user_types = df['User Type'].value_counts()
    print(user_types)

    # Display counts of gender
    print('\nBreakdown of gender: ')
    if 'Gender' in str(df.columns.values):
        gender_types = df['Gender'].value_counts()
        print(gender_types)
    else:
        print('Sorry! No gender data available for selected query.')
    # Display earliest, most recent, and most common year of birth
    print('\nBreakdown of birth year: ')
    if 'Birth Year' in str(df.columns.values):
        print('Earliest birth year is: ',df['Birth Year'].min())
        print('Latest birth year is: ',df['Birth Year'].max())
        print('Most common birth year is: ',df['Birth Year'].mode()[0])
    else:
        print('Sorry! No birth year data available for selected query.')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        exit = input('\nWould you like to exit? Enter yes to exit and any other key to continue.\n')
        if exit.lower()=='yes':
            print('Thank you!')
            break
        else:
            print('\nYou are being redirected to the start of the application.')
            print('-'*40)

if __name__ == "__main__":
	main()
