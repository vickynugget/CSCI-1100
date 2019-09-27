
radius_of_sun = input('Enter the radius of the Sun (miles) -> ')
radius_of_sun = int(radius_of_sun)
print(radius_of_sun)
radius_of_moon = input('Enter the radius of the Moon (miles) -> ')
radius_of_moon = int(radius_of_moon)
print(radius_of_moon)
distance_sun_to_earth = input('Enter the maximum distance to the Sun (miles) -> ')
distance_sun_to_earth = int(distance_sun_to_earth)
print(distance_sun_to_earth)
min_distance_moon = input('Enter the minimum distance to the Moon (miles) -> ')
min_distance_moon = int(min_distance_moon)
print(min_distance_moon)
rate_of_moon = input('Enter the rate the Moon is moving away (in/year) -> ')
rate_of_moon = float(rate_of_moon)
print(rate_of_moon)

distance_moon_to_earth = float(distance_sun_to_earth * (radius_of_moon/radius_of_sun))
print('The Moon will have exactly the same apparent size as the Sun when it is ' + '{0:.2f}'.format(distance_moon_to_earth) + ' miles away.')

more_distance_moon_to_earth = distance_moon_to_earth - min_distance_moon
print('The Moon will need to recede another ' + '{0:.2f}'.format(more_distance_moon_to_earth) + ' miles')


rate_of_moon = float(rate_of_moon/12/5280)
years = more_distance_moon_to_earth/rate_of_moon
print('Which will occur in ' , int(years) , ' years at the current rate.')