'''
output the given year month day and print them with the type of number
'''

months = [
  'January',
  'February',
  'March',
  'April',
  'May',
  'June',
  'August',
  'September',
  'October',
  'November',
  'December'
]

# list which end with the number  1-31

endings = ['st','nd','rd'] + 17*['th']\
        + ['st','nd','rd'] + 7*['th']\
        + ['st']

year    = raw_input('Year:')
month   = raw_input('Month (1-12):')
day     = raw_input('Day (1-31):')

month_number = int(month)
day_number   = int(day)

# remember  that the number of month and day should minus 1 which can get  the correct  index
month_name = months[month_number-1]
ordinal    = day +endings[day_number -1]

print  month_name + '' + ordinal + '.' + year