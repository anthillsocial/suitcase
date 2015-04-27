#!/usr/bin/python3

# Notes: A motor with 1 kg.cm torque is capable of holding a 1 kg weight 
#        at a radial distance of 1 cm.
# Measurment from center of circle to outside edge
rpm = 28
rps = rpm/60
torque = 40 # kg.cm
radius = 20 # cm
canhold = torque/radius
force = torque*0.098 

output = "A motor with a torque of: {} kg.cm"
output += " Is capable of holding: {}kg"
output += " At a radial distance of: {}cm"
output += " Force:{} N.m"
output += " If it it rotates at: {}rmp"
output += " Rotations per second: {}rps"
output = output.format(torque, canhold, radius, force, rpm,rps)
print(output)
