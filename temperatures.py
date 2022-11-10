# 1. Create a new module, `convert_temp.py`, containing two functions, `c2f` and `f2c`, which convert from Celsius to # 
# Fahrenheit (or back).  The functions assume that they get a single number as input.
# 2. The return value will be the converted temperature.
# 3. import this module, and show that you can convert temperatures in either direction.

# this line means: Only print __name__ and __file__ when the program is being run standalone.
# if we were imported as a module, don't print anything.

if __name__ == '__main__':
    print(f'Hello from {__name__}!')
    print(f'Now in file: {__file__}')

def c2f(c_temp):
    return c_temp * 1.8 + 32.00

def f2c(f_temp):
    return (f_temp - 32) / 1.8 

if __name__ == '__main__':
    print(f'Goodbye from {__name__}!')