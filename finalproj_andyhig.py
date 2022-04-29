
import pandas as pd
import matplotlib.pyplot as plt
from sodapy import Socrata

plt.close('all')
cdc_api = Socrata('data.cdc.gov', 'Jx6TfqIGNRuPtssfGBZMkZe6l')
death_data = cdc_api.get('bi63-dtpu', limit=100000)

death_data_df = pd.DataFrame.from_records(death_data)
death_data_df['deaths'] = death_data_df['deaths'].astype(int)
death_data_df = death_data_df[death_data_df.cause_name != 'All causes']


death_data_1999 = death_data_df.loc[death_data_df.year == '1999']
death_data_2000 = death_data_df.loc[death_data_df.year == '2000']
death_data_2001 = death_data_df.loc[death_data_df.year == '2001']
death_data_2002 = death_data_df.loc[death_data_df.year == '2002']
death_data_2003 = death_data_df.loc[death_data_df.year == '2003']
death_data_2004 = death_data_df.loc[death_data_df.year == '2004']
death_data_2005 = death_data_df.loc[death_data_df.year == '2005']
death_data_2006 = death_data_df.loc[death_data_df.year == '2006']
death_data_2007 = death_data_df.loc[death_data_df.year == '2007']
death_data_2008 = death_data_df.loc[death_data_df.year == '2008']
death_data_2009 = death_data_df.loc[death_data_df.year == '2009']
death_data_2010 = death_data_df.loc[death_data_df.year == '2010']
death_data_2011 = death_data_df.loc[death_data_df.year == '2011']
death_data_2012 = death_data_df.loc[death_data_df.year == '2012']
death_data_2013 = death_data_df.loc[death_data_df.year == '2013']
death_data_2014 = death_data_df.loc[death_data_df.year == '2014']
death_data_2015 = death_data_df.loc[death_data_df.year == '2015']
death_data_2016 = death_data_df.loc[death_data_df.year == '2016']
death_data_2017 = death_data_df.loc[death_data_df.year == '2017']


main_tree = \
    ('What year are you interested in? Enter a year between "1999-2017", or enter "exit" to end: ', #------------------------------------------  main_tree[0]
        ('1999', #-----------------------------------------------------------------------------------------------------------------------------  year[0]
            ('What state are you interested in? "Michigan" or "California". Or "exit" to end: '), #--------------------------------------------  main_tree[1][1]
                (death_data_1999.loc[death_data_1999.state == 'Michigan']), (death_data_1999.loc[death_data_1999.state == 'California'])), #---  1)main_tree[1][2] = Michigan, 2)main_tree[1][3] = California
        ('2000',
            ('What state are you interested in? "Michigan" or "California". Or "exit" to end: '),
                (death_data_2000.loc[death_data_2000.state == 'Michigan']), (death_data_2000.loc[death_data_2000.state == 'California'])),
        ('2001',
            ('What state are you interested in? "Michigan" or "California". Or "exit" to end: '),
                (death_data_2001.loc[death_data_2001.state == 'Michigan']), (death_data_2001.loc[death_data_2001.state == 'California'])),
        ('2002',
            ('What state are you interested in? "Michigan" or "California". Or "exit" to end: '),
                (death_data_2002.loc[death_data_2002.state == 'Michigan']), (death_data_2002.loc[death_data_2002.state == 'California'])),
        ('2003',
            ('What state are you interested in? "Michigan" or "California". Or "exit" to end: '),
                (death_data_2003.loc[death_data_2003.state == 'Michigan']), (death_data_2003.loc[death_data_2003.state == 'California'])),
        ('2004',
            ('What state are you interested in? "Michigan" or "California". Or "exit" to end: '),
                (death_data_2004.loc[death_data_2004.state == 'Michigan']), (death_data_2004.loc[death_data_2004.state == 'California'])),
        ('2005',
            ('What state are you interested in? "Michigan" or "California". Or "exit" to end: '),
                (death_data_2005.loc[death_data_2005.state == 'Michigan']), (death_data_2005.loc[death_data_2005.state == 'California'])),
        ('2006',
            ('What state are you interested in? "Michigan" or "California". Or "exit" to end: '),
                (death_data_2006.loc[death_data_2006.state == 'Michigan']), (death_data_2006.loc[death_data_2006.state == 'California'])),
        ('2007',
            ('What state are you interested in? "Michigan" or "California". Or "exit" to end: '),
                (death_data_2007.loc[death_data_2007.state == 'Michigan']), (death_data_2007.loc[death_data_2007.state == 'California'])),
        ('2008',
            ('What state are you interested in? "Michigan" or "California". Or "exit" to end: '),
                (death_data_2008.loc[death_data_2008.state == 'Michigan']), (death_data_2008.loc[death_data_2008.state == 'California'])),
        ('2009',
            ('What state are you interested in? "Michigan" or "California". Or "exit" to end: '),
                (death_data_2009.loc[death_data_2009.state == 'Michigan']), (death_data_2009.loc[death_data_2009.state == 'California'])),
        ('2010',
            ('What state are you interested in? "Michigan" or "California". Or "exit" to end: '),
                (death_data_2010.loc[death_data_2010.state == 'Michigan']), (death_data_2010.loc[death_data_2010.state == 'California'])),
        ('2011',
            ('What state are you interested in? "Michigan" or "California". Or "exit" to end: '),
                (death_data_2011.loc[death_data_2011.state == 'Michigan']), (death_data_2011.loc[death_data_2011.state == 'California'])),
        ('2012',
            ('What state are you interested in? "Michigan" or "California". Or "exit" to end: '),
                (death_data_2012.loc[death_data_2012.state == 'Michigan']), (death_data_2012.loc[death_data_2012.state == 'California'])),
        ('2013',
            ('What state are you interested in? "Michigan" or "California". Or "exit" to end: '),
                (death_data_2013.loc[death_data_2013.state == 'Michigan']), (death_data_2013.loc[death_data_2013.state == 'California'])),
        ('2014',
            ('What state are you interested in? "Michigan" or "California". Or "exit" to end: '),
                (death_data_2014.loc[death_data_2014.state == 'Michigan']), (death_data_2014.loc[death_data_2014.state == 'California'])),
        ('2015',
            ('What state are you interested in? "Michigan" or "California". Or "exit" to end: '),
                (death_data_2015.loc[death_data_2015.state == 'Michigan']), (death_data_2015.loc[death_data_2015.state == 'California'])),
        ('2016',
            ('What state are you interested in? "Michigan" or "California". Or "exit" to end: '),
                (death_data_2016.loc[death_data_2016.state == 'Michigan']), (death_data_2016.loc[death_data_2016.state == 'California'])),
        ('2017',
            ('What state are you interested in? "Michigan" or "California". Or "exit" to end: '),
                (death_data_2017.loc[death_data_2017.state == 'Michigan']), (death_data_2017.loc[death_data_2017.state == 'California']))
    )


def run_program():
    """This function runs the program."""
    # Interactive section of function, welcome and asks user the year they want to investigate.
    # while loop is active to reset at end of program if the user wants to run program again.
    list_yrs = ['1999', '2000', '2001', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017']

    print('Welcome to the program!')
    again = True
    while again == True:
        again = False
        user_year = input(main_tree[0])
        if user_year.lower().title() == 'Exit':
            print('Thanks for using the program. Goodbye!')
            exit(0)
        elif user_year:
            index = int(user_year) - 1998
            reset = True
            while reset == True:
                reset = False
                for year in main_tree[0:]:
                    if year[0] == user_year:
                        user_state = input(main_tree[1][1]).lower().title()
                        if user_state != 'Exit':
                            if user_state == 'Michigan' or user_state == 'Mi':
                                mi_target = main_tree[index][2]
                                mi_target = mi_target.sort_values('deaths', ascending=False).nlargest(5, 'deaths')
                                print(f'\nHere are the top 5 causes of death in the state of Michigan in the year {user_year}.')
                                print(mi_target)
                                mi_target.plot(x = 'cause_name', y = 'deaths', kind = 'bar')
                                plt.show()
                                end = input('\nDo you want to run the program again? ').lower().title()
                                if end == 'Yes':
                                    again = True
                                elif end == 'No':
                                    print('Thanks for using the program. Goodbye!')
                                    exit(0)
                            elif user_state == 'California' or user_state == 'Ca':
                                ca_target = main_tree[index][3]
                                ca_target = ca_target.sort_values('deaths', ascending=False).nlargest(5, 'deaths')
                                print(f'\nHere are the top 5 causes of death in the state of California in the year {user_year}.')
                                print(ca_target)
                                ca_target.plot(x = 'cause_name', y = 'deaths', kind = 'bar')
                                plt.show()
                                end = input('\nDo you want to run the program again? ').lower().title()
                                if end == 'Yes':
                                    again = True
                                elif end == 'No':
                                    print('Thanks for using the program. Goodbye!')
                                    exit(0)
                            else:
                                print('Wrong state! Please select from the options above!')
                                reset = True
                                break
                        elif user_state == 'Exit':
                            print('Thanks for using the program. Goodbye!')
                            exit(0)


if __name__ == '__main__':
    run_program()