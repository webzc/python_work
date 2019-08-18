#coding:utf-8
import pygame
from pygame.locals import *
import sys
import time

#pygame环境初始化
pygame.init()
game_activate = False


#设置一个长为1250，宽为700的窗口
screen = pygame.display.set_mode((1250, 700))
screen.fill((255,255,255))

# 设置窗口标题
pygame.display.set_caption("愤怒的小鸟")

#加载图片
bg = pygame.image.load('images/bg2.png') 
bird = pygame.image.load('images/bird.png')
pig = pygame.image.load('images/pig.png')
slingshot1 = pygame.image.load('images/slingshot1.png')
slingshot2 = pygame.image.load('images/slingshot2.png')
stand1 = pygame.image.load('images/stand1.png')
stand2 = pygame.image.load('images/stand2.png')
stand3 = pygame.image.load('images/stand3.png')


def handleEvent():
    for event in pygame.event.get():
        if event.type==pygame.QUIT or event.type == KEYDOWN and event.key == K_q:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == K_2:
            game_activate = True 
            print("测试成功")
    

#声明位置变量
x = 150
y = 315

while True:
	#试试按下2
    screen.blit(bg,(0,0))
    screen.blit(slingshot1,(155,300))
    screen.blit(slingshot2,(125,300))
    screen.blit(bird,(105,460))
    screen.blit(bird,(50,500))
    screen.blit(bird,(10,500))
    screen.blit(pig,(825,365))
    screen.blit(pig,(910,365))
    screen.blit(pig,(995,365))
    screen.blit(pig,(1130,315))
    screen.blit(stand1,(1132,361))
    screen.blit(stand2,(1150,372))
    screen.blit(bird,(x,y))
    x = x + 5
    
    
    
    pygame.display.update()
    handleEvent()
