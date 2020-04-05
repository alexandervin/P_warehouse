from random import randint
from termcolor import cprint


class Road:

    def __init__(self, start, end, distance):
        self.start = start
        self.end = end
        self.distance = distance


class Warehouse:

    def __init__(self, name, content=0):
        pass

    def __str__(self):
        pass

    def set_road_out(self):
        pass

    def truck_arrived(self, truck):
        pass

    def get_next_truck(self):
        pass

    def track_ready(self, truck):
        pass

    def act(self):
        pass


class Vehicle:
    fuel_rate = 0

    def __init__(self, model):
        pass

    def __str__(self):
        pass

    def tank_app(self):
        pass


class Truck(Vehicle):

    def __init__(self, model, body_space=1000):
        pass

    def __str__(self):
        pass

    def ride(self):
        pass

    def go_to(self, road):
        pass

    def act(self):
        pass


class AutoLoader(Vehicle):

    def __init__(self, model, bucket_capacity=100, warehouse=None, role='loader'):
        pass

    def __str__(self):
        pass

    def act(self):
        pass

    def load(self):
        pass

    def unload(self):
        pass


TOTAL_CARGO = 100000

moscow = Warehouse(name='Москва', content=TOTAL_CARGO)
piter = Warehouse(name='Питер', content=0)

moscow_piter = Road(start=moscow, end=piter, distance=715)
piter_moscow = Road(start=piter, end=moscow, distance=780)

moscow.set_road_out(moscow_piter)
piter.set_road_out(piter_moscow)

loader_1 = AutoLoader(model='Bobcat', bucket_capacity=1000, warehouse=moscow, role='loader')
loader_2 = AutoLoader(model='LongKing', bucket_capacity=500, warehouse=piter, role='unloader')

truck_1 = Truck(model='Камаз', body_space=5000)
truck_2 = Truck(model='Газ', body_space=2000)

moscow.truck_arrived(truck_1)
moscow.truck_arrived(truck_2)

hour = 0

#моделирующая часть
while piter.content < TOTAL_CARGO:
    hour += 1
    cprint('----------------------------------Час {0}-----------------------'.format(hour), color='red')
    truck_1.act()
    truck_2.act()
    loader_1.act()
    loader_2.act()
    moscow.act()
    piter.act()
    cprint(truck_1, color='cyan')
    cprint(truck_2, color='cyan')
    cprint(loader_1, color='cyan')
    cprint(loader_2, color='cyan')
    cprint(moscow, color='cyan')
    cprint(piter, color='cyan')