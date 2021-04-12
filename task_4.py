# from task_2 import
from recordclass import RecordClass


class Car(RecordClass):
    brand: str
    model: str
    dimensions: list
    engine: int
    to100km: float
    consumption: float

    def boost(self):
        self.engine *= 1.1


def create_cars():
    bmw_x7 = Car('BMW', 'X7', (5151, 2000, 1805), 335, 5.4, 8.5)
    bmw_m5 = Car('BMW', 'M5', (4720, 1750, 1392), 617, 2.9, 10.8)
    audi_q7 = Car('Audi', 'Q7', (5086, 1983, 1737), 333, 6.2, 5.7)
    audi_q8 = Car('Audi', 'Q8', (4986, 1995, 1705), 340, 5.4, 6.0)
    chevrolet_camaro = Car('Chevrolet', 'Camaro', (4784, 1897, 1348), 455, 4.1, 14.5)
    audi_r8 = Car('Audi', 'R8', (4430, 1940, 1240), 602, 3.6, 13.4)

    return [bmw_x7, bmw_m5, audi_q7, audi_q8, chevrolet_camaro, audi_r8]


def boost_cars(cars):
    for car in cars:
        car.boost()
