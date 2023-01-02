def main(temp):
    """
    Display the message according to the following temperature conditions given to you in Celsius:
    Temp<0: "Freezing"
    Temp 1-10: "Very Cold"
    Temp 11-20: "Cold"
    Temp 21-30: "Normal"
    Temp 31-40: "Hot"
    Temp >40: "Very Hot"

    Args:
        temp: integer
    Returns:
        string: the message to print
    """
    if temp<0:
        out = "Freezing"
    elif temp > 0 and temp <= 10:
        out = "Very Cold"
    elif temp > 10 and temp <= 20:
        out = "Cold"
    elif temp > 20 and temp <= 30:
        out =  "Normal"
    elif temp > 30 and temp <= 40:
        out = "Hot"
    elif temp>40:
        out = "Very hot"
    
    return out

print(main(21))