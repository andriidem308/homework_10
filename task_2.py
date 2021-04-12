from collections import namedtuple


Car = namedtuple('Car', ['brand', 'model', 'dimensions', 'engine', 'to100km', 'consumption'])


def print_car(car: Car):
    print(f'***** {car.brand} {car.model} *****')
    print(f'Length: {car.dimensions[0]}mm, Width: {car.dimensions[1]}mm, Height: {car.dimensions[2]}mm')
    print(f'Engine power: {car.engine}hp')
    print(f'Speed up to 100km/s in {car.to100km}s')
    print(f'Fuel consumption: {car.consumption}L\n')


def create_cars():
    bmw_x7 = Car('BMW', 'X7', (5151, 2000, 1805), 335, 5.4, 8.5)
    bmw_m5 = Car('BMW', 'M5', (4720, 1750, 1392), 617, 2.9, 10.8)
    audi_q7 = Car('Audi', 'Q7', (5086, 1983, 1737), 333, 6.2, 5.7)
    audi_q8 = Car('Audi', 'Q8', (4986, 1995, 1705), 340, 5.4, 6.0)
    chevrolet_camaro = Car('Chevrolet', 'Camaro', (4784, 1897, 1348), 455, 4.1, 14.5)
    audi_r8 = Car('Audi', 'R8', (4430, 1940, 1240), 602, 3.6, 13.4)

    return [bmw_x7, bmw_m5, audi_q7, audi_q8, chevrolet_camaro, audi_r8]


def print_cars(car_list):
    for car in car_list:
        print_car(car)

