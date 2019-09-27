"""
This program is an experiment in guessing gum balls. Assume that the container of gum balls is a cube, and that the gum balls are spheres. We will make the assumption that all the gum balls line up. 

Author: Xueqi Huang
Version: 1

"""




## two functions to calculate the volume of a sphere given a radius and a cube given a side length

import math
def find_sphere_volume(radius):
    sphere = 4/3*math.pi*radius**3
    return sphere
def find_cube_volume(side):
    cube = side**3
    return cube

## ask the user for the side length of the cube and the radius of the gum balls
side = input('Enter the side length of the cube (in.) => ')
print(side)
radius = input('Enter the radius of the gum ball (in.) => ')
print(radius)

## convert the input to float
side = float(side)
radius = float(radius)


## calculate the total number of gum balls that can be contained in the cube
num_of_ball = int(side/(radius*2))
num_of_ball = int(num_of_ball**3)
print('A box of side length', side, 'will hold', num_of_ball, 'gum balls of radius', str(radius) + '.')

## call functions and print the output
cube_volume = find_cube_volume(side)
sphere_volume = find_sphere_volume(radius)*num_of_ball
radio_of_volume = (format(sphere_volume/cube_volume, '.2%'))
print('The gum balls will take up {0:.2f} in^3\nof the total volume of {1:.2f} in^3 or'.format(sphere_volume, cube_volume), radio_of_volume)

## change the container to a sphere and calculate the new_volume
radius = side/2
new_volume = find_sphere_volume(radius)
print('A sphere with a diameter of {0:.1f} would have volume {1:.2f} in^3'.format(side, new_volume))

## calculate the density
density = cube_volume/num_of_ball
num_of_ball2 = int(new_volume/density)
print('It would hold', num_of_ball2, 'gum balls at the same density.')
