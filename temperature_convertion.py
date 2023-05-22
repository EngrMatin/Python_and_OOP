tempInCelsius = int(input("Enter temperature in Degree Celsius: "))

""" C/5 = (F-32)/9
=>  F = 9*C/5 + 32 """
tempInFafrenheit = 9*tempInCelsius/5 + 32
print(f"The equivalent temperature of {tempInCelsius} degree celsius is {tempInFafrenheit} degree fahrenheit.")