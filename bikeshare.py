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
    
    cities = ('washington', 'chicago', 'new york city')
    city = input('Would you like to see data on chicago, washington or new york city? Please select one: ').lower()
    while city not in cities:
        print('Oops, looks like we don\'t have any data on that city.')
        city = input('Please chose between chicago, washington and new york city: ')
        break



    # TO DO: get user input for month (all, january, february, ... , june)
    months = ('all','january', 'february','march','april','may','june')
    month = input('Please select a month (january, february, march...,june). Type "all" for no filter:').lower()
    while month not in months:
        print('Ooops, that is not a valid month. Please try again!')
        month = input('Please chose a month between january and june: ')
        break
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
         
              
        

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ('all','monday','tuesday','wednesday','thursday','friday','saturday','sunday')
    day = input('Please select a day (monday, tuesday, ... sunday). Type "all" for no filter:').lower()
    while day not in days:
        print('Ooops, that is not a valid day. Please try again!')
        day = input('Please chose a day between monday and sunday: ')
        break
 

   
    return city, month, day
    print('-'*40)

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to anayze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
  day is: ' + popular_day)
       Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv('{}.csv'.format(city).replace(' ','_').lower())
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.weekday_name
    
    if month != 'all':
        df = df[df['month'] == month]
        
    
    if day != 'all':
        df = df[df['Day of Week'] == day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    popular_month = df['month'].mode()[0]
    print('The most common month is: {}.'.format(popular_month))

    # TO DO: display the most common day of week
    popular_day = df['Day of Week'].mode()[0]
    print('The most common day is: {}'.format(popular_day))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The most common start hour is: {}'.format(popular_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_station = df['Start Station'].value_counts().idxmax()
    print('The most most commonly used station is\n: {}'.format(popular_station))

    # TO DO: display most commonly used end station
    popular_end = df['End Station'].value_counts().idxmax()
    print('The most most commonly used end station is:\n{}'.format(popular_end))

    # TO DO: display most frequent combination of start station and endstation
    """Found helpful information on this website: https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.value_counts.html"""
    
    popular_trip = df.groupby(['Start Station','End Station']).size().sort_values(ascending=False)

    print('This is the most frequent combination of start and end station:\n', popular_trip.head(1))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print('The total travel time is: {} seconds.'.format(total_time))

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('The average travel time is: {} seconds.'.format(mean_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts().count()
    print('There are {} different kinds of Users.'.format(user_types))
    print(df['User Type'].value_counts())
          
    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_count = df['Gender'].value_counts(dropna=True)
        print('These are the gender counts:\n')
        print(gender_count)
    else:
        print('There is no information regarding gender or birth year for washington.')

   

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        most_recent = df['Birth Year'].max()
        print('The youngest user was born in {}.'.format(most_recent))
        
        earliest = df['Birth Year'].min()
        
        print('The oldest user was born in {}.'.format(earliest))   
        
        most_common = df['Birth Year'].mode()[0]
        print('The most common birth year is {}.'.format(most_common)) 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



 
    answer = input('Would you like to see 5 rows of raw data? type \'yes\' or \'no\': ')
    x = 0
    while answer == 'yes':
        x += 5
        print(df[0+x:5+x])
        answer = input('Would you like to see 5 more rows of raw data? type \'yes\' or \'no\': ')
                
            
    
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