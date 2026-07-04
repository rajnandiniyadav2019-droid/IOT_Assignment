km_to_m = lambda x: x * 1000
m_to_cm = lambda x: x * 100
cm_to_mm = lambda x: x * 10
feet_to_inches = lambda x: x * 12
inch_to_cm = lambda x: x * 2.54

def distance_converter(distance, conversion_type, func):
    print(conversion_type, "=", func(distance))

distance = float(input("Enter distance: "))

distance_converter(distance, "km to m", km_to_m)
distance_converter(distance, "m to cm", m_to_cm)
distance_converter(distance, "cm to mm", cm_to_mm)
distance_converter(distance, "feet to inches", feet_to_inches)
distance_converter(distance, "inch to cm", inch_to_cm)
