#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
脚本说明：
1. 运行脚本需将系统输入法切换为英文
2. 全局操作时间设置尽量长一点，否则由于超时脚本会崩
3. awvs界面需为全屏
4. 保证桌面左上角位置为空，目的是文件复制到桌面后会自动跑到这个位置
5. awvs软件界面按钮位置可能会因为系统分辨率不同而改变，所以使用脚本之前先测出几个按钮的位置
6. 运行脚本后不要动键盘鼠标
"""


import pyautogui
import time, os
import shutil


##########################################全局设置################################################
# 设置全局打开单个awvs文件所需时间（秒）
open_awvs_file_time = 15
# 设置全局单个操作所需时间（秒）
sigle_option_time = 3
##################################################################################################

def mouse_click(location:list, clicks=1):
	pyautogui.click(location[0], location[1], clicks=clicks, interval=0.0, button='left')
	time.sleep(sigle_option_time)
	# print("click location {}, {} success ...".format(location[0], location[1]))
	

def deal_with_awvs(file_path):
	files = os.listdir(file_path)
	wvs_files = []
	for file in files:
		if ".wvs" in file:
			file = os.path.join(file_path, file)
			wvs_files.append(file)
	return wvs_files


def wvs2xml(awvs_path, desktop_path, result_path, location_wvs, location_Actions, location_Export_to_XML, location_X):
	wvs_files = deal_with_awvs(awvs_path)
	for wvs_file in wvs_files:
		shutil.copy(wvs_file, desktop_path)
		file_name = wvs_file.split("\\")[-1]
		xml_name = file_name.replace(".wvs", ".xml")

		# 双击 wvs 文件
		time.sleep(sigle_option_time)
		mouse_click(location_wvs,2)
		time.sleep(open_awvs_file_time)
		# 单击 Actions
		mouse_click(location_Actions, 1)
		# 单击 Export to XML
		mouse_click(location_Export_to_XML, 1)
		time.sleep(sigle_option_time)

		pyautogui.typewrite(["backspace"], "0.1")
		pyautogui.typewrite(xml_name, 0.1)
		pyautogui.typewrite(["enter", "enter", "0.1"])

		# 关闭 wvs 文件
		mouse_click(location_X, 1)

		os.remove(os.path.join(desktop_path, file_name))
		try:
			shutil.move(os.path.join(desktop_path, xml_name), result_path)
		except Exception:
			os.remove(os.path.join(desktop_path, xml_name))
		print("成功将 {} 转换为 {}".format(file_name, xml_name))


if __name__ == "__main__":
	########################################  脚本配置  #############################################
	awvs_path = "awvs"
	desktop_path = r"C:\Users\Alien\Desktop"
	result_path = "result"

	# 按钮位置，我电脑的分辨率跟你们可能不一样，需要自己测
	location_wvs = [35, 20] # 鼠标点击桌面左上角的位置
	location_Actions = [70, 35] # Actions 按钮
	location_Export_to_XML = [110, 110] # Export to XML 按钮
	location_X = [1343, 9] # 关闭 按钮
	################################################################################################

	wvs2xml(awvs_path, desktop_path, result_path, location_wvs, location_Actions, location_Export_to_XML, location_X)

