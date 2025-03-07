def new_fcn():
    pass

def new_fcn2():
    pass

def convert_temp(value,unit_from,unit_to):
    if unit_from=="C" and unit_to=="F":
        value=(value * 9/5) + 32
        return value

    elif unit_from=="F" and unit_to=="C":
        value=(value - 32) * 5/9
        return value

    elif unit_from=="K" and unit_to=="C":
        value=value - 273.15
        return value

    elif unit_from=="C" and unit_to=="K":
        value=value + 273.15
        return value

    else:
        raise ValueError
        print("Incorrect Input! Please read the Manual again!")



def convert_weight(value,unit_from,unit_to):

    if unit_from=="g" and unit_to=="Kg":
        value=value/1000
        return value

    elif unit_from=="Kg" and unit_to=="g":
        value=value*1000
        return value

    elif unit_from=="Kg" and unit_to=="pounds":
        value=value*2.20462
        return value

    elif unit_from=="pounds" and unit_to=="Kg":
        value=value/2.20462
        return value

    elif unit_from=="g" and unit_to=="pounds":
        value=value*0.00220462
        return value

    elif unit_from=="pounds" and unit_to=="g":
        value=value*453.592
        return value
    else:
        raise ValueError
        print("Incorrect Input! Please read the Manual again!")



def convert_length (value,unit_from,unit_to):
    if unit_from=="Km" and unit_to=="m":
        value=value*0.001
        return value
    elif unit_from=="m" and unit_to=="Km":
        value=value*1000
        return value
    elif unit_from=="miles" and unit_to=="km":
        value=value*1.60934
        return value
    elif unit_from=="Km" and unit_to=="miles":
        value=value*0.621371
        return value
    else:
        raise ValueError
        print("Incorrect Input! Please read the Manual again!")


def main():
    print("Hello User! Welcome to Our Unit conversion Simple Application!")
    print("\nFor Distance you can only use Km, m and miles and For Weight you can only use Kg, g, pounds and For Temperature you can only use K, C and F!")
    print("\nPlease read the Manual carefully before using the Application!")

    category = input("Choose a category (temperature, length, weight): ").lower()
    value = float(input("Enter the value to convert: "))
    unit_from = input("Enter the source unit: ")
    unit_to = input("Enter the target unit: ")

    try:
        if category == "temperature":
            result = convert_temp(value, unit_from, unit_to)
        elif category == "length":
            result = convert_length(value, unit_from, unit_to)
        elif category == "weight":
            result = convert_weight(value, unit_from, unit_to)
        else:
            raise ValueError("Unsupported category! Try Again!")

        print(f"{value} {unit_from} is {result:.2f} {unit_to}.")


    except ValueError as e:
        print(e,"e")



if __name__ == "__main__":
    main()






















