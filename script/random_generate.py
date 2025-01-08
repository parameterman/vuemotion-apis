import random
from class_define import *
from color import *
def random_base() -> Base:
    """随机生成一个 Base 类的实例"""
    x = random.randint(0, 100)  # 随机生成 x 坐标
    y = random.randint(0, 100)  # 随机生成 y 坐标
    scale_x = random.uniform(0.5, 2.0)  # 随机生成 x 方向缩放比例
    scale_y = random.uniform(0.5, 2.0)  # 随机生成 y 方向缩放比例
    rotation = random.randint(0, 360)  # 随机生成旋转角度
    opacity = random.uniform(0.0, 1.0)  # 随机生成透明度
    fill_color =  get_random_color_name()  # 生成随机填充颜色
    border_color = get_random_color_name()  # 生成随机边框颜色
    border_width = random.randint(1, 10)  # 随机生成边框宽度
    border_offset = random.randint(0, 10)  # 随机生成边框偏移
    border_interval = (random.randint(0, 5), random.randint(0, 5))  # 随机生成边框间隔

    # 创建并返回 Base 类的实例
    return Base(x, y, scale_x, scale_y, rotation, opacity,
                fill_color, border_color, border_width,
                border_offset, border_interval)

def random_group() -> Group:
    """随机生成一个 Group 类的实例"""
    x = random.randint(0, 100)  # 随机生成 x 坐标
    y = random.randint(0, 100)  # 随机生成 y 坐标
    scale_x = random.uniform(0.5, 2.0)  # 随机生成 x 方向缩放比例
    scale_y = random.uniform(0.5, 2.0)  # 随机生成 y 方向缩放比例
    rotation = random.randint(0, 360)  # 随机生成旋转角度
    opacity = random.uniform(0.0, 1.0)  # 随机生成透明度
    

    # 创建并返回 Group 类的实例
    return Group(x, y, scale_x, scale_y, rotation, opacity)

def random_line() -> Line:
    """随机生成一个 Line 类的实例"""
    x = random.randint(0, 100)  # 随机生成 x 坐标
    y = random.randint(0, 100)  # 随机生成 y 坐标
    scale_x = random.uniform(0.5, 2.0)  # 随机生成 x 方向缩放比例
    scale_y = random.uniform(0.5, 2.0)  # 随机生成 y 方向缩放比例
    rotation = random.randint(0, 360)  # 随机生成旋转角度
    opacity = random.uniform(0.0, 1.0)  # 随机生成透明度
    fill_color =  get_random_color_name()  # 生成随机填充颜色
    border_color = get_random_color_name()  # 生成随机边框颜色
    border_width = random.randint(1, 10)  # 随机生成边框宽度
    border_offset = random.randint(0, 10)  # 随机生成边框偏移
    border_interval = (random.randint(0, 5), random.randint(0, 5))  # 随机生成边框间隔

    # 创建并返回 Line 类的实例
    return Line(x, y, scale_x, scale_y, rotation, opacity,
                fill_color, border_color, border_width,
                border_offset, border_interval)

def random_rect() -> Rect:
    """随机生成一个 Rect 类的实例"""
    x = random.randint(0, 100)  # 随机生成 x 坐标
    y = random.randint(0, 100)  # 随机生成 y 坐标
    scale_x = random.uniform(0.5, 2.0)  # 随机生成 x 方向缩放比例
    scale_y = random.uniform(0.5, 2.0)  # 随机生成 y 方向缩放比例
    rotation = random.randint(0, 360)  # 随机生成旋转角度
    opacity = random.uniform(0.0, 1.0)  # 随机生成透明度
    # fill_color =  get_random_color_name()  # 生成随机填充颜色
    # border_color = get_random_color_name()  # 生成随机边框颜色
    # border_width = random.randint(1, 10)  # 随机生成边框宽度
    # border_offset = random.randint(0, 10)  # 随机生成边框偏移
    # border_interval = (random.randint(0, 5), random.randint(0, 5))  # 随机生成边框间隔
    width = random.randint(50, 500)  # 随机生成宽度
    height = random.randint(50, 500)  # 随机生成高度
    radius = random.randint(0, 20)  # 随机生成圆角半径
    # 创建并返回 Rect 类的实例
    return Rect(x, y, scale_x, scale_y, rotation, opacity,width, height, radius)


def random_circle() -> Circle:
    x = random.randint(0, 100)  # 随机生成 x 坐标
    y = random.randint(0, 100)  # 随机生成 y 坐标
    scale_x = random.uniform(0.5, 2.0)  # 随机生成 x 方向缩放比例
    scale_y = random.uniform(0.5, 2.0)  # 随机生成 y 方向缩放比例
    rotation = random.randint(0, 360)  # 随机生成旋转角度
    opacity = random.uniform(0.0, 1.0)  # 随机生成透明度
    # fill_color =  get_random_color_name()  # 生成随机填充颜色
    # border_color = get_random_color_name()  # 生成随机边框颜色
    # border_width = random.randint(1, 10)  # 随机生成边框宽度
    # border_offset = random.randint(0, 10)  # 随机生成边框偏移
    # border_interval = (random.randint(0, 5), random.randint(0, 5))  # 随机生成边框间隔
    radius = random.randint(5, 20)  # 随机生成圆角半径
    cx = random.randint(0, 100)  # 随机生成 x 坐标
    cy = random.randint(0, 100)  # 随机生成 y 坐标
    bool = random.randint(0, 1)  # 随机生成是否填充

    if bool == 1:
        return Circle(x, y, scale_x, scale_y, rotation, opacity, radius,cx=None, cy=None)
    else:
        return Circle(x, y, scale_x, scale_y, rotation, opacity, radius, cx, cy)


def random_Arc() -> Arc:
    """随机生成一个 Arc 类的实例"""
    x = random.randint(0, 100)  # 随机生成 x 坐标
    y = random.randint(0, 100)  # 随机生成 y 坐标
    scale_x = random.uniform(0.5, 2.0)  # 随机生成 x 方向缩放比例
    scale_y = random.uniform(0.5, 2.0)  # 随机生成 y 方向缩放比例
    rotation = random.randint(0, 360)  # 随机生成旋转角度
    opacity = random.uniform(0.0, 1.0)  # 随机生成透明度
    radius = random.randint(5, 20)  # 随机生成圆角半径
    from_ = random.randint(0, 90)  # 随机生成起始角度
    to = random.randint(90, 360)  # 随机生成终止角度
    return Arc(x, y, scale_x, scale_y, rotation, opacity, radius, from_, to)


def random_text() -> Text:
    """随机生成一个 Text 类的实例"""
    x = random.randint(0, 100)  # 随机生成 x 坐标
    y = random.randint(0, 100)  # 随机生成 y 坐标
    scale_x = random.uniform(0.5, 2.0)  # 随机生成 x 方向缩放比例
    scale_y = random.uniform(0.5, 2.0)  # 随机生成 y 方向缩放比例
    rotation = random.randint(0, 360)  # 随机生成旋转角度
    opacity = random.uniform(0.0, 1.0)  # 随机生成透明度
    fill_color =  get_random_color_name()  # 生成随机填充颜色
    border_color = get_random_color_name()  # 生成随机边框颜色
    border_width = random.randint(1, 10)  # 随机生成边框宽度
    border_offset = random.randint(0, 10)  # 随机生成边框偏移
    border_interval = (random.randint(0, 5), random.randint(0, 5))  # 随机生成边框间隔

    # 创建并返回 Text 类的实例
    return Text(x, y, scale_x, scale_y, rotation, opacity,
                fill_color, border_color, border_width,
                border_offset, border_interval)

def random_ellipse() -> Ellipse:
    """随机生成一个 Ellipse 类的实例"""
    x = random.randint(0, 100)  # 随机生成 x 坐标
    y = random.randint(0, 100)  # 随机生成 y 坐标
    scale_x = random.uniform(0.5, 2.0)  # 随机生成 x 方向缩放比例   
    scale_y = random.uniform(0.5, 2.0)  # 随机生成 y 方向缩放比例
    rotation = random.randint(0, 360)  # 随机生成旋转角度
    opacity = random.uniform(0.0, 1.0)  # 随机生成透明度
    cx = random.randint(0, 100)  # 随机生成 x 坐标
    cy = random.randint(0, 100)  # 随机生成 y 坐标
    rx = random.randint(50, 500)  # 随机生成 x 半径
    ry = random.randint(50, 500)  # 随机生成 y 半径
    # 创建并返回 Ellipse 类的实例
    return Ellipse(x, y, scale_x, scale_y, rotation, opacity, cx, cy, rx, ry)

def random_number_axis() -> NumberAxis:
    """随机生成一个 NumberAxis 类的实例"""
    x = random.randint(0, 100)  # 随机生成 x 坐标
    y = random.randint(0, 100)  # 随机生成 y 坐标
    scale_x = random.uniform(0.5, 2.0)  # 随机生成 x 方向缩放比例
    scale_y = random.uniform(0.5, 2.0)  # 随机生成 y 方向缩放比例
    rotation = random.randint(0, 360)  # 随机生成旋转角度
    opacity = random.uniform(0.0, 1.0)  # 随机生成透明度
    # fill_color =  get_random_color_name()  # 生成随机填充颜色
    # base_unit = random.choice(['number' , 'radian' , 'degree'])
    
    base_unit = 'number'
    # interval = random.randint(100, 200)  # 随机生成间隔
    font_size = random.randint(18, 24)  # 随机生成字体大小
    domain = [random.randint(-10, 0), random.randint(0, 10)]
    return NumberAxis(x, y, scale_x, scale_y, rotation, opacity, base_unit=base_unit, font_size=font_size, domain=domain)

def sequence_gen() -> str:
    #生成数列
    sequence = ''
    pass

def Series_gen_ax() -> str:
    #生成级数
    series = ''
    lower_bound = 0
    upper_bound = 9999

def arithmetic_series(n, a, d):
    """
    生成等差级数的前n项。
    
    参数:
    n: 项数
    a: 第一项
    d: 公差
    """
    n(n*d+a)/2

    series = []
    current = a
    for _ in range(n):
        series.append(current)
        current += d
    return series
def geometric_series(n, a, r):
    """
    生成等比级数的前n项。
    
    参数:
    n: 项数
    a: 第一项
    r: 公比
    """
    series = []


    current = a
    for _ in range(n):
        series.append(current)
        current *= r
    return series
def fibonacci_series(n):
    """
    生成斐波那契级数的前n项。
    
    参数:
    n: 项数
    """
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series


    