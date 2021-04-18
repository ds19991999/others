#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import itertools as its
import os

words = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
r = its.product(words, repeat=15)

def get_path(filename):
	folder = "passwd"
	if not os.path.exists(folder):
		os.makedirs(folder)
		path = folder + "/" + filename
		file = open(path, "w")
		file.close()
	else:
		path = folder + "/" + filename
	return path

num = 0
name = 0
for i in r:	
	if num % 1000000 == 0:
		num = 0
		name += 1
		filename = "passwd" + str(name) + ".txt"
		passwd_path = get_path(filename)
		print("---->>>现在正在将密码写入(%s)中......" % passwd_path)
	with open(passwd_path,"a",encoding="utf-8") as dic:
			dic.write("".join(i) + "\n")
	num += 1
