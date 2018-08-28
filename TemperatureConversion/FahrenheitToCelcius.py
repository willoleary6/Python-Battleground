# take in user input
import time

fahrenheitTemp = int(input("What is the current temperature in fahrenheit? \n"))
type(fahrenheitTemp)
celsiusTemp = (fahrenheitTemp - 32) * (5/9)
print('it is '+str(fahrenheitTemp)+'°F or...')
time.sleep(1)
print(str(celsiusTemp)+"°C")
