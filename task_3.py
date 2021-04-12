def three_highest(cars):
    return sorted(cars, key=lambda car: car.dimensions[2], reverse=True)[:3]


def three_fastest(cars):
    return sorted(cars, key=lambda car: car.to100km)[:3]
