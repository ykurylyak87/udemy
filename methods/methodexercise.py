l = {'nyc': 0.20, 'la': 0.22, 'nc': 0.15}
fed_tax = 0.10


def net_tax(gross):
    state_name = input("Input the name of state: ")
    if state_name in l:
        net_value = gross - (gross * l[state_name]) - (gross * fed_tax)
        print("Your net value is: " + str(net_value))
        return net_value
    else:
        print("The input state is not in base")
        return None

net_tax(float(input("Input gross value: ")))
