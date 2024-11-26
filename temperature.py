def main():
    # Get user input

    x = float(input("What's the temperature? "))
    y = input("Farenheit or Celsius? (f or c): ")
    # Convert and return
    temp = get_temp(x,y)
    metric = get_metric(y)
    print(f"That is {temp: .2f} degrees {metric}. ")

def get_temp(x,y):
    if y == "f":
        temp = (x - 32) / 1.8
        return temp
    elif y == "c":
        temp = (x * 1.8) + 32
        return temp
    else: 
        raise ValueError("Invalid metric. Please enter 'f' or 'c'.")

def get_metric(y):
    if y == "f":
        return "Celsius"
    elif y == "c":
        return "Farenheit"
    else: 
        raise ValueError("Invalid metric. Please enter 'f' or 'c'.")
        

main()