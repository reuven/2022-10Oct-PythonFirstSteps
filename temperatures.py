# 1. Create a new module, `convert_temp.py`, containing two functions, `c2f` and `f2c`, which convert from Celsius to # 
# Fahrenheit (or back).  The functions assume that they get a single number as input.
# 2. The return value will be the converted temperature.
# 3. import this module, and show that you can convert temperatures in either direction.

print('Hello from the temp module!')

def c2f(c_temp):
    return c_temp * 1.8 + 32.00

def f2c(f_temp):
    return (f_temp - 32) / 1.8 

print('Goodbye from the temp module!')