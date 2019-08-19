#coding:utf-8
import pygame
from pygame.locals import *
import time


#初始化pygame环境
pygame.init()

#创建一个长宽分别为480/650窗口
screen = pygame.display.set_mode((1800, 700))
screen.fill((255,255,255))

#设置窗口标题
pygame.display.set_caption("飞机大战")

#加载图片
enemy1=pygame.image.load("images/ball.png")
bg=pygame.image.load("images/bg.jpg")

def handleEvent():
    for event in pygame.event.get():
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()
       
x = 100 
y = 100
z = 5
a = 5
screen.blit(enemy1,(x,y))
while True:
    screen.blit(bg,(0,0))
    x = x + z
    y = y + a
    if x>=1800:
        z=-z
    if y>=700:
        a=-a
    if x<=0:
        z=-z
    if y<=0:
        a=-a
    screen.blit(enemy1,(x,y))
    
    # 更新屏幕内容
    pygame.display.update()
    #监听有没有按下退出按钮
    handleEvent()
