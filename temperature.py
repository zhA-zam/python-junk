''' 
Converts the temperature in Canada, which would be in degrees Celsius, 
to what the temperature would be in degrees Fahrenheit rounded to a whole 
number using the formula:
Fahrenheit = (Celsius * 9 / 5) + 32
The result is the display of the temperature in both Celsius and Fahrenheit,
phrased in a way that Homer Simpson would speak it.

The formula is taken from the lab assignment Google Doc "Lab 1 Temperature"
By: Zoha Azam
Date: September 19, 2023
'''
Celsius = int(input("What is the current temperature in Canada? "))  # Allows for user input to be used in math operations
Fahrenheit = round(Celsius*9/5+32)

print(Celsius,"degrees in Canada would be",Fahrenheit,"degrees in Springfield. D'oh!")
