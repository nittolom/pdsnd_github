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
    cityloop='y'
    monthloop='y'
    dayloop='y'
    while cityloop =='y':
        city=str(input('Enter one of the following cities as shown: Chicago, New York City, Washington:  ')).lower()
        if city=='washington' or city=='new york city' or city=='chicago':
            print('You chose', city.title())
            cityloop='n'
        else:
            print('Oops, invalid entry. Make sure to input one of the options shown.')

    #TO DO: get user input for month (all, january, february, ... , june)
    while monthloop=='y':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month= str(input('Which month would you like to analyze? January, February, March, April, May, June, or all?  ')).lower()
        if month in months:
            print('You chose', month.title())
            month = months.index(month) + 1
            monthloop='n'
        elif (month=='all'):
            print('You chose', month.title())
            monthloop='n'
        else:
            print('Oops, invalid entry. Make sure to input one of the options shown.')
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while dayloop=='y':
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday']
        day= str(input('Which day would you like to analyze? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or all?  ')).lower()
        if day in days:
            print('You chose', day.title())
            dayloop='n'
        elif (day=='all'):
            print('You chose', day.title())
            dayloop='n'
        else:
            print('Oops, invalid entry. Make sure to input one of the options shown.')
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
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    if (month != 'all'):
        df = df[df['month'] == month]
    if (day != 'all'):
        df = df[df['day_of_week'] == day.title()] 
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    monthsindex = ['january', 'february', 'march', 'april', 'may', 'june']
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # TO DO: display the most common month
    print('The most frequent traveled month in this dataset is',monthsindex[(df['month'].mode()[0])-1].title())

    # TO DO: display the most common day of week
    print('The most frequent traveled day in this dataset is', df['day_of_week'].mode()[0])
    # TO DO: display the most common start hour
    print('The most frequent hour traveled in this dataset is hour',df['hour'].mode()[0])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    df['StartEnd']=df['Start Station']+" to "+df['End Station']
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most commonly used start station in this dataset is',df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('The most commonly used end station in this dataset is',df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    print('The most frequent start to end station trip in this dataset is',df['StartEnd'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    total_travel_hours=total_travel_time//3600
    left_over_seconds=total_travel_time%3600
    total_travel_minutes=left_over_seconds//60
    total_seconds=left_over_seconds%60
    print('The total travel time for this dataset is',total_travel_hours,'hours',total_travel_minutes,'minutes',total_seconds,'seconds')

    # TO DO: display mean travel time
    avg_travel_time=df['Trip Duration'].mean()
    avg_travel_hours=avg_travel_time//3600
    avgleft_over_seconds=avg_travel_time%3600
    avg_travel_minutes=avgleft_over_seconds//60
    avgtotal_seconds=avgleft_over_seconds%60
    print('The avg travel time for this dataset is',avg_travel_hours,'hours',avg_travel_minutes,'minutes',avgtotal_seconds,'seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
    print(df['User Type'].value_counts())
    print(" ")
    # TO DO: Display counts of gender
    try:
        print(df['Gender'].value_counts())
        print(" ")
    # TO DO: Display earliest, most recent, and most common year of birth
        print('The earliest birth year in this dataset is',int(df['Birth Year'].min()))
        print('The most recent birth year in this dataset is',int(df['Birth Year'].max()))
        print('The most common birth year in this dataset is',int(df['Birth Year'].mode()[0]))
    except:
        print('Washington does not have Gender or Birth statistics')
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
        rawdata='y'
        counter=5
        start=0
        while rawdata=='y':
            data= input('Would you like to see the raw data? Enter yes or no: ')
            if data.lower() =='yes':
                print(df.iloc[start:counter].to_dict())
                print(" ")
                start=counter
                counter=counter+5
                rawdata='y'
            elif data.lower() =='no':
                rawdata='n'
            else:
                print('Oops invalid input. Choose an option shown.')
        restartloop='y'
        while restartloop=='y':
            restart = input('\nWould you like to restart the program? Enter yes or no.\n')
            if restart.lower() == 'yes':
               restartloop='restart'
            elif restart.lower() == 'no':
                restartloop='no'
            else:
                print('Oops invalid input. Choose an option shown.')
        if restartloop=='no':
            print(" ")
            print('Have a nice day!')
            break
        if restartloop=='restart':
            restartloop='y'
            
if __name__ == "__main__":
	main()
