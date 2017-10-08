# -*- coding: utf-8 -*-
import Image,ImageDraw,ImageFont
import random
import math, string  

class RandomChar():
  """用于随机生成汉字"""
	#@staticmethod
	def Unicode():
    	val = random.randint(0x4E00, 0x9FBF)
    	return unichr(val)  

	#@staticmethod
  	def GB2312():
		head = random.randint(0xB0, 0xCF)
		body = random.randint(0xA, 0xF)
		tail = random.randint(0, 0xF)
		val = ( head << 8 ) | (body << 4) | tail
		str = "%x" % val
		return str.decode('hex').decode('gb2312')  




for i in range(0, num):
    char = RandomChar().GB2312()
	print char;




