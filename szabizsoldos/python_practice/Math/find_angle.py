import math

AB = int(10)
BC = int(10)
arc_tangent = math.atan2(AB, BC)
angle = math.degrees(arc_tangent)
print(str(round(angle)) + '°')

# returns 45°
