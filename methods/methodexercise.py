l = {'nyc': 0.20, 'la': 0.22, 'nc': 0.15}
fed_tax = 0.10


def state_tax(state):
    return l[state]


def net_tax(gross):
    state_name = input("Input the name of state: ")
    if state_name in l:
        net_value = gross - (gross * state_tax(state_name)) - (gross * fed_tax)
        return net_value
    else:
        return None


x = float(input("Input gross value: "))
y = net_tax(x)
print("Your net value is: " + str(y))
