#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
@Author  :   Anonymous
@License :   (C) Copyright 2019, Anonymous
@Contact :   anonymous@demo.com
@Software:   PyCharm
@File    :   peeweedb.py
@Time    :   2019/11/16 09:10
@Desc    :   直接运行脚本即可
	1. 运行环境 Python3
	2. 参数 back_travel_num 设置号码尾部遍历的位数
	3. phone文件夹 放置需要遍历的号码文件，可以放多个文件，脚本会自动读取
"""


import os
import sys
import itertools
import threading


class Logger(object):

	def __init__(self, filename='default.log', stream=sys.stdout):
		self.terminal = stream
		self.log = open(filename, 'a', encoding="utf-8")

	def write(self, message):
		self.terminal.write(message)
		self.log.write(message)

	def flush(self):
		pass


sys.stdout = Logger(stream=sys.stdout)
sys.stderr = Logger(stream=sys.stderr)


def generate_pwd(minlength:int, maxlength:int, choices:str = '0123456789')->iter:
	for i in range(minlength, maxlength + 1):
		keyiter = itertools.product(choices, repeat=i)
		for c in keyiter:
			yield ''.join(c)


def write_pwd(pwd_iter:iter, mk:int = 100):
	pwd_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "字典")
	if not os.path.exists(pwd_folder):
		os.makedirs(pwd_folder)

	pwd_nums = mk*1000
	pwd_num_count = 1
	file_count = 1

	while pwd:
		pwd_name = str(file_count*mk) + "k_pwd.txt"
		pwd_path = os.path.join(pwd_folder, pwd_name)
		print("[++++] 已遍历 [%s] 个字典, 文件保存到: [%s] ..." % (file_count*mk, pwd_path))
		with open(pwd_path, "w", encoding="utf-8") as pwd_file:
			for pwd in pwd_iter:
				if pwd_num_count == pwd_nums:
					pwd_num_count = 1
					file_count += 1
					break
				pwd_file.write(pwd+"\n")
				pwd_num_count += 1


if __name__ == "__main__":
	pwd_iter = generate_pwd(minlength=2, maxlength=3, choices="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
	write_pwd(pwd_iter, mk=100)
