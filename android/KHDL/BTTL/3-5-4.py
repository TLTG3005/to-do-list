drink = {
    'Tra':{
        'Tra chanh': 10,
        'Tra dao': 20,
        'Tra tac': 10
    },
    'nuoc ngot':{
        'coca':10,
        'pepsi':10
    },
    'nuoc ep':{
        'cam':15,
        'buoi':20,
        'tao':25
    }
}
print('--Menu--')
for drink_type in drink:
    print(drink_type)
    for drink, price in drink[drink_type].items():
        print(drink, price)