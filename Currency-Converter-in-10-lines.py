from currency_converter import *
print("===================================================")
print("Created by Programmer Choicean")
print("Check out his GitHub - https://github.com/SkyisjustTheBeginning")
print("===================================================")
#Taking Input from user
amt = float(input("Amount:"))
currency1 = str(input("Currency 1:"))
currency2 = str(input("Currency 2:"))
#Variable to convert
c = CurrencyConverter()
#Conversion
#Converted Amount is rounded to 2 decimal places.
converted_amt = c.convert(amt,currency1,currency2)
print("Converted Amount - ",round(converted_amt,2))
print("Currency Converter using Python ! - Choicean")
print("Values have been rounded to 2 decimal places")
print("Happy Coding!")
