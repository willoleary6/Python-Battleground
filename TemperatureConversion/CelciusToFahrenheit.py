# take in user input
import time

celsiusTemp = int(input("What is the current temperature in celsius? \n"))
type(celsiusTemp)
fahrenheitTemp = (celsiusTemp * (9/5)) + 32
print('it is '+str(celsiusTemp)+'°C or...')
time.sleep(1)
print(str(fahrenheitTemp)+"°F")
