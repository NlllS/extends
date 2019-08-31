from classes import Arduino, Raspberry, Device

from example_tuple import uim

raspberry = Raspberry()

arduino = Arduino

device = Device(625000, uim)

device.start_press()
device.increase_pressure(5)
device.decrease_pressure(5)
device.stop_press()
