def rental_car_cost(days):
    if days > 7:
        return (40 * days) - 50
    elif days > 3:
        return (40 * days) - 20
    else:
        return 40 * days

print rental_car_cost(5)

