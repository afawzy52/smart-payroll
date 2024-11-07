from icecream import ic
import icecream.icecream

def my_function():
    icecream("Hello world!")
my_function()
def add_numbers(a, b):
    result = a + b
    return result
sum_result = add_numbers(5, 3)
icecream(sum_result)
#print(dir(icecream))