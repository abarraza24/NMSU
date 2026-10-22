from car import *
from electric_car import ElectricCar

my_tesla = ElectricCar('Tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

my_crolla_cross = Car('Toyota', 'Corolla Cross', 2023)
print(my_crolla_cross.get_descriptive_name())