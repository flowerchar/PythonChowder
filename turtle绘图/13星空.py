import random

import pygame


# 流星类
class Star(object):
    """用于指定流星的位置，移动向量，星尾长度"""

    def __init__(self, point, screen, all_speed):
        self.startx = point[0]
        self.starty = point[1]
        screen_rect = screen.get_rect()  # 获得屏幕矩形
        self.speed_x = (self.startx     - screen_rect.centerx) / 25 * all_speed[speed_index]  # 水平方向速度设置
        self.speed_y = (self.starty - screen_rect.centery) / 25 * all_speed[speed_index]  # 竖直方向速度设置
        self.end_x = self.startx + self.speed_x * 5  # 星尾
        self.end_y = self.starty + self.speed_y * 5  # 星尾
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def blitme(self):
        pygame.draw.aaline(screen, self.color, (star.startx, star.starty), (star.end_x, star.end_y), 100)  # 绘制流星轨迹


# 屏幕上流星检测
def on_screen(point):
    if 0 < point[0] < 1600 and 0 < point[1] < 900 and not (point[0] == 800 and point[1] == 450):
        return point


# 初始化设置
pygame.init()

screen = pygame.display.set_mode((1600, 900))
screen_rect = screen.get_rect()
points = []  # 用于存储流星的点集
for i in range(10):  # 生成十颗流星
    point = [random.randint(600, 1000), random.randint(250, 650)]
    points.append(point)

# 全局速度（加速和反向加速）
n = 0
all_speed = []
speed_index = 0  # 全局速度列表索引
while n < 1000:
    i = n / 100
    all_speed.append(i)  # 全局速度
    n += 1

# 主循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill(0)
    pygame.time.Clock().tick(96)

    if speed_index < 999:
        speed_index += 1  # 速度加快
    else:
        speed_index = 0
        all_speed.reverse()  # 反向加速

    # 新增一颗流星
    point1 = [random.randint(600, 1000), random.randint(250, 650)]
    points.append(point1)
    # 画流星
    for point in points:
        star = Star(point, screen, all_speed)
        star.blitme()
        # 流星移动
        point[0] = star.startx + star.speed_x  # 崩溃的电脑
        point[1] = star.starty + star.speed_y  # 崩溃的电脑

    points = list(filter(on_screen, points))  # 内存控制
    pygame.display.update()
