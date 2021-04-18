#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
-------------------------------------------------
   File Name：     decode8bin.py
   Description :
   Author :        admin
   date：          2020/5/19
-------------------------------------------------
   Change Activity:
                   2020/5/19
-------------------------------------------------
"""

import time
import shutil
import os, re
import sys

def time_print(str):
    str_head = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    str_out = "[++++] {} {}".format(str_head, str)
    print(str_out)


def walk_files(path_temp):
    """
    递归获取文件路径
    :param path_temp:
    :return:
    """
    path_temp = path_temp.replace("/", "\\")
    for root, dirs, files in os.walk(path_temp):
        for file in files:
            file_path = os.path.join(root, file)
            yield file_path
        for dir in dirs:
            path_temp = os.path.join(root, dir)
            walk_files(path_temp)


def new_files(path_temp, file_path):
    """
    在指定文件夹创建文件
    :param path_temp:
    :param file_path:
    :return:
    """
    path_temp = path_temp.replace("/", "\\")
    new_file_full_path = os.path.join(path_temp, file_path)
    new_file_folder = os.path.split(new_file_full_path)[0]
    if os.path.split(new_file_full_path)[1][0] == ".":
        return None
    if not os.path.exists(new_file_folder):
        os.makedirs(new_file_folder)
    return new_file_full_path


def decode_content(content):
    def sub_str(value):
        ls = value.group().split('\\')[1:]
        ls = [int(i, 8) for i in ls]
        try:
            return bytes(ls).decode('utf8')
        except UnicodeDecodeError:
            print("[----] UnicodeDecodeError: {}".format(value))
            return value
    try:
        new_content = re.sub(r'(?:\\\d{3}){3}', sub_str, content)
    except TypeError:
        print("[----] TypeError: {}".format(content))
        return content
    return new_content


def analysis_file(file_folder, new_folder):
    file_paths = walk_files(file_folder)
    for file_path in file_paths:
        new_file_full_path = new_files(new_folder, file_path)
        if new_file_full_path:
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content_list = f.readlines()
                time_print("正在处理：{}".format(file_path))
            except UnicodeDecodeError:
                shutil.copyfile(file_path, new_file_full_path)
                continue
            with open(new_file_full_path, "w", encoding="utf-8") as f:
                # 按行处理
                for content in content_list:
                    new_content = decode_content(content)
                    f.write(new_content)

def print_help():
    print("python3 decode_file.py 目标文件夹(默认vhostlog) 新文件夹(默认new)\n\n")

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) == 2:
        folder1 = args[0]
        folder2 = args[1]
    else:
        print_help()
        folder1 = "vhostlog"
        folder2 = "new"
    try:
        analysis_file(folder1, folder2)
    except Exception as msg:
        print("[----] Error: {}".format(msg))

