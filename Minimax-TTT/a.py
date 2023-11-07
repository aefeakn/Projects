#import math

from math import gcd     # importing gcd function

x = int(input())
y = int(input())

z = gcd(x,y)

print(z)

s = ((x*y)/z)

print(s)