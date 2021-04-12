def three_highest(cars):
    return sorted(cars, key=lambda car: car.dimensions[2])[-3:][::-1]


def three_fastest(cars):
    return sorted(cars, key=lambda car: car.to100km)[:3]
