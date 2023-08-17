import math

def calculate_cone_volume(radius, height):
    # 计算底面面积
    base_area = math.pi * radius**2

    # 计算体积
    volume = (1/3) * base_area * height

    return volume

# 输入圆锥的底面半径和高度
radius = float(input("请输入底面半径："))
height = float(input("请输入高度："))

cone_volume = calculate_cone_volume(radius, height)
print("圆锥的体积为：", cone_volume)
