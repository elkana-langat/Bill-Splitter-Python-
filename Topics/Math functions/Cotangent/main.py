import math

angle_in_degrees = int(input())
angle_in_radians = angle_in_degrees * math.pi / 180
contangent = 1 / math.tan(angle_in_radians)
result = round(contangent, 10)

print(result)