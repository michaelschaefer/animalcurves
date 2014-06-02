########################################################
## This is a template file for animalcurves.py        ##
##                                                    ##
## Just fill in your own T, N, func_x and func_y.     ##
## As long as these four guys (well, N is optional)   ##
## are available for animalcurves.py you can add      ##
## other imports, define new parameters and functions ##
## as you like.                                       ##
########################################################


#############
## IMPORTS ##
#############

# work with floating point divisions by default
from __future__ import division

# you probably want to use Pi
from math import pi

# unlike in math, numpy functions work on arrays
from numpy import sin, cos


################
## PARAMETERS ##
################

# plot the curve over the interval [0,T]
T = 2*pi

# plot N line segments
N = 1001


##########################
## COORDINATE FUNCTIONS ##
##########################

# the x coordinates
def func_x(t):
    return sin(t)

# the y coordinates
def func_y(t):
    return cos(t)

