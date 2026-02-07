import math, sys

def function(x):
    return (1/2) * math.cos(x)**2

def f_prime(x):
    return math.cos(x) * math.sin(x) * (-1)

def find_lambda(x):
    return float(1 / (f_prime(x)))

def calculate_x_n_plus_1(x_n):
    return x_n - (function(x_n) * (1 / f_prime(x_n)))


"""
I tried to make it work with newtons method, but I think I missed something, though the
newtons method implementation itself should be fine. 
"""
# initial = 8
# current = initial
# for k in range(0,100):
#     current = calculate_x_n_plus_1(current)
#     # if(current == 0):
#     #     sys.exit(1)
#     #     print('current is zero')
initial = 10
current = initial
for k in range(0,1000):
    current = function(current)
print(current)
# This should always work in practice, but if for whatever reason it didn't.
# We can add below a function call below which verifies that we have 10 digits, and if we don't
# allocate another 1000 rounds of iteration until we do, ad-infinitum.
