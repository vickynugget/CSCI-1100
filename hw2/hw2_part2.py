"""
This program tells how long will a future year be.


Author: Xueqi Huang
Version: 1


"""
##define functions
def time_to_seconds(h,m,s):
    seconds = h*3600 + m*60 + s
    return seconds
def seconds_to_str(second):
    print(second//3600,'hours',second%3600//60,'mins',second%3600%60,'secs')


##call function
print('A day in 2017 is 23 hours 56 minutes and 4 seconds long.')
second = time_to_seconds(23,56,4)
print('Which is equivalent to', second, 'seconds.')

##input future year
future_year = int(input('Enter a future year => '))
print(future_year)

##calculate lenght of year
rate = 6*3600/900000000
length_of_year = int(rate*(future_year-2017)+second)

##print output
print('A day in year', future_year, 'will be', length_of_year, 'seconds long')
print('which is equivalent to ', end='')
seconds_to_str(length_of_year)

