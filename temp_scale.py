# Title : Temperature Scale
# Ganesh lohiya
# M 36

x=int(input("Enter temperature:"))  # take input from the user
y=input("is it in celcius or fahrenhite")  # ask for the unit of temperature
if y=="celcius": 
 f=(9*x/5)+32   # celcius to fahrenhite formula
 print(f)
else: 
 c=(5/9)*(x-32)   # fahrenhite to celsius formula
 print(c)
