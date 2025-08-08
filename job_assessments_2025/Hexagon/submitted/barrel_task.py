import argparse
import numpy as np
from scipy.optimize import least_squares
"""
####example 
V=113.7333512
l=5
r=3
result: h=4.500000m
"""

# create a parser object
parser = argparse.ArgumentParser(description = 'Find height of liquid in a barrel, given the volume (m^3), length (m) and radius (m)')

# add arguments
parser.add_argument('V', type = float, help = 'Input the volume in (m^3) as a float')
parser.add_argument('l', type = float, help = 'Input the length in (m) as a float')
parser.add_argument('r', type = float, help = 'Input the radius in (m) as a float')

# parse the arguments from standard input
args = parser.parse_args()

#check that the inputs are sensible
if args.r < 0:
    raise ValueError("The radius must be positive")
if args.l < 0:
    raise ValueError("The length must be positive")
if (args.V < 0) or (args.V > ((np.pi * (args.r**2)) * args.l)):
    raise ValueError("The volume must be obtainable given the radius and length specified")

# h0: (initial estimate for h based on proportionality)
x0_barrel = (args.V / ((np.pi * (args.r**2)) * args.l)) * args.r * 2

def fun_barrel(h,V,l,r):
    #create the objective function
    theta = 2*(90-(np.rad2deg(np.arcsin((h[0]/r[0])-1))))
    sector_area = (np.pi * (r[0]**2) * theta)/(360)
    triangle_area = 0.5 * (r[0]**2) * np.sin(np.deg2rad(theta))
    full_circle = np.pi * (r[0]**2)
    minim_eqn = V[0] - (l[0]*(full_circle - sector_area + triangle_area))
    return [minim_eqn]

#perform the optimisation
res = least_squares(fun_barrel, x0_barrel, args=([args.V],[args.l],[args.r]),ftol=2.23*1e-16,gtol=2.23*1e-16,xtol=2.23*1e-16,verbose=0)

print('height = ',round(res.x[0],6),'m') #print the result, rounded to the nearest micrometre



