#coding=utf-8
#想要学习微信消息制作，首先你得有个女朋友
from __future__ import unicode_literals
from threading import Timer
from wxpy import *
from wechat_sender import Sender
import time,requests
bot = Bot(console_qr=2,cache_path='botoo.pk1') 
def get_news():
  # 这里是从网上摘取的句子，因此每日会不同
  url = "http://open.iciba.com/dsapi/"
  r = requests.get(url)
  contents = r.json()['content']
  translation = r.json()['translation']
  return contents,translation
def send_news():
  try:
    ufriend = bot.friends().search(u'Mr-Lee')[0]）#朋友昵称在此写
    ufriend.send(get_news()[0])
    ufriend.send(get_news()[1][5:])
    ufriend.send(u'晚安')
    t = Timer(86400,send_news) # 计时：一天
    t.start()
  except:
    ufriend = bot.friends().search("L")[0] # 你的微信名称，不是微信号
    ufriend.send(u'消息发送失败')

