#coding=utf-8
import threading
import win32gui
import win32con
import win32clipboard as w

def fun_timer():
	def getText():
		
		w.OpenClipboard()
		d = w.GetClipboardData(win32con.CF_UNICODETEXT)
		w.CloseClipboard()
		return d

	def setText(aString):
		w.OpenClipboard()
		w.EmptyClipboard()
		w.SetClipboardData(win32con.CF_UNICODETEXT, aString)
		w.CloseClipboard()
	
	#第一句
	def send_qq(to_who, msg):
		setText(msg)
		qq = win32gui.FindWindow(None, to_who)
		win32gui.SendMessage(qq, 258, 22, 2080193)
		win32gui.SendMessage(qq, 770, 0, 0)
		win32gui.SendMessage(qq, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
		win32gui.SendMessage(qq, win32con.WM_KEYUP, win32con.VK_RETURN, 0)
		
	to_who='伊淑灵'
	msg='风里雨里，程序陪你'
	send_qq(to_who, msg)
	
	#第二句
	def send_qq(to_who, text):
		setText(text)
		qq = win32gui.FindWindow(None, to_who)
		win32gui.SendMessage(qq, 258, 22, 2080193)
		win32gui.SendMessage(qq, 770, 0, 0)
		win32gui.SendMessage(qq, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
		win32gui.SendMessage(qq, win32con.WM_KEYUP, win32con.VK_RETURN, 0)
	to_who='伊淑灵'
	text='猜猜我是程序还是人'
	
	send_qq(to_who, text)
	global timer
	timer = threading.Timer(86400, fun_timer)
	timer.start()
 
timer = threading.Timer(1, fun_timer)
timer.start()

