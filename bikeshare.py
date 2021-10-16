import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def check_input(input_str,input_type):
    while True:
        input_read=input(input_str)
        try:
            if input_read in ['chicago', 'new york city', 'washington'] and input_type==1:
                break
            elif input_read in ['all', 'January', 'February', 'March', 'April', 'May', 'June'] and input_type==2:
                break
            elif input_read in ['all', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'] and input_type==3:
                break
            else:
                if input_type==1:
                    print('wrong city!, your input should be chicago or new york city or washington')
                if input_type==2:
                    print('wrong month!, your input should be january or february or march or April or May or June or all')
                if input_type==3:
                    print('wrong day!, your input should be Saturday or Sunday or Monday or Tuesday or Wednesday or Thursday or Friday or all')
        except Error_input:
            print('sorry, input not found , please enter correct input')
    return input_read

def get_filters():
    city_options = ['Chicago','New York City','Washington']
    month_options = ['All', 'January', 'February', 'March', 'April', 'May', 'June']
    day_options = ['All', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    while True:
        try:
            city = city_options.index(input('\n(Chicago, New York City, Washington)\n').lower().title())
            month = month_options.index(input('\n(January, February, March, April, May, June, All)\n').lower().title())
            day = day_options.index(input('\n(Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, All)\n').lower().title())
            return city_options[city].lower(), month_options[month].lower(), day_options[day].lower()
        except ValueError:
            print ("Your previous choice is not available. Please try again")
            
    print('Hello! Let\'s explore some US bikeshare data!')
    print('-'*40)
    

def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['houre'] = df['Start Time'].dt.hour
    
    if month != 'all':
       months = ['january', 'february', 'march', 'april', 'may', 'june']
       month = months.index(month) + 1
       df = df[df['month'] == month]

    if day != 'all':
       df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    start_time = time.time()
    popular_month = df['month'].mode()[0]
    print('Most common month:', popular_month)
    popular_day = df['day_of_week'].mode()[0]
    print('Most common day of week:', popular_day)
    popular_hour = df['houre'].mode()[0]
    print('Most common Hour of day:', popular_hour)
    print('\nCalculating The Most Frequent Times of Travel...\n',(time.time() - start_time))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    start_time = time.time()
    popular_start_station = df['Start Station'].mode()[0]
    print('Most common Start Station:', popular_start_station)
    popular_end_station = df['End Station'].mode()[0]
    print('Most common End Station:', popular_end_station)
    group_field = df.groupby(['Start Station', 'End Station'])
    popular_combination_station = group_field.size().sort_values(ascending=False).head(1)
    print('Most combination of Start Station and End Station:', popular_combination_station)
    print('\nCalculating The Most Popular Stations and Trip...\n')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    start_time = time.time()
    all_trip_duration = (df['Trip Duration'].sum())
    print('total travel time:', all_trip_duration)
    average_trip_duration = (df['Trip Duration'].mean())
    print('average travel time:', average_trip_duration)
    print('\nCalculating Trip Duration...\n')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df, city):
    print('\nuser...\n')
    start_time = time.time()
    count_of_user_type = (df['User Type'].value_counts())
    print('counts of each user type:', count_of_user_type)
    if city != 'washington':
        count_of_gender_type = (df['Gender'].value_counts())
        print('counts of each gender:', count_of_gender_type)
        min_birth_year = (df['Birth Year'].min())
        print('earliest year of birth:', min_birth_year)
        max_birth_year = (df['Birth Year'].max())
        print('Most recent year of birth:', max_birth_year)
        birth_year = (df['Birth Year'].mode()[0])
        print('Most common year of birth:', birth_year)
      
    print('\nCalculating User Stats...\n')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
