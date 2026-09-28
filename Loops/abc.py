#write a python program using function to convert celsius to fahrenheit
def celsius_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit.
    Formula: (Celsius * 9/5) + 32
    """
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


# Get temperature input from the user
try:
    celsius_input = float(input("Enter temperature in Celsius: "))

    # Call the function and store the result
    fahrenheit_output = celsius_to_fahrenheit(celsius_input)

    # Display the result formatted to 2 decimal places
    print(f"{celsius_input}°C is equal to {fahrenheit_output:.2f}°F")

except ValueError:
    print("Please enter a valid numerical value.")