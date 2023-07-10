import configparser
import os
import platform
import shutil
import tarfile
import tempfile

import py7zr
import rarfile
from PySide6.QtWidgets import QFileDialog
from PySide6.QtWidgets import QMessageBox
from pyunpack import Archive

from conf.public import file_map

config = configparser.ConfigParser()
conf_path = tempfile.gettempdir() + "/pub_tools/config.ini"
config.read(conf_path, encoding="utf-8")


# 读取配置文件
def get_conf(section, option):
    if not config.has_section(section) or not config.has_option(section, option):
        return ""
    return config.get(section, option)


# 写入配置文件
def set_conf(section, option, value):
    # 判断配置文件是否存在，不存在则创建, 目录不存在则创建
    if not os.path.exists(os.path.dirname(conf_path)):
        os.makedirs(os.path.dirname(conf_path))
    if not config.has_section(section):
        config.add_section(section)
    config.set(section, option, value)
    with open(conf_path, "w", encoding="utf-8") as f:
        config.write(f)


def open_diag_dir(title):
    path = get_conf("tmp", "tmp_path")
    path = QFileDialog.getExistingDirectory(None, title, path)
    set_conf("tmp", "tmp_path", path)
    return path


# 获取系统临时文件夹
def get_temp_dir():
    return tempfile.gettempdir()


def Error(err):
    QMessageBox.warning(None, "警告", err)


def Info(info):
    QMessageBox.information(None, "信息", info)


def verify_file_type(file, file_type):
    return (
            file_type != "所有"
            and not os.path.isdir(file)
            and file.split(".")[-1] in file_map[file_type]
    )


# 获取文件夹内的所有文件列表方法,并根据变量判断是否递归获取, 并根据文件路径获取文件类型，判断file_type在字典中是否存在
def get_files(folder_path, file_type, is_while=False):
    file_list = []
    if is_while:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if verify_file_type(file, file_type):
                    file_list.append(os.path.join(root, file))
    else:
        for file in os.listdir(folder_path):
            if verify_file_type(file, file_type):
                file_list.append(os.path.join(folder_path, file))
    return file_list


# 获取文件路径中的路径与文件名
def get_file_path(file_path):
    file_path = os.path.split(file_path)
    return file_path


# 修改文件名
def rename_file(file_path, find_str, repl_str):
    path, file_name = get_file_path(file_path)
    file_name = file_name.replace(find_str, repl_str)
    new_file = path + "/" + file_name
    os.rename(file_path, new_file)
    return new_file


def set_bar_value(bar, value=1, total=100):
    # 计算当前进度值,如果超过100则设置为100
    val = int(value / total * 100)
    if val > 100:
        val = 100
    bar.setValue(val)


# 解压文件
async def decompress_file(file_path, dest_filepath, passwords, del_source=False):
    # 获取文件所在目录
    if dest_filepath == "":
        dest_filepath = os.path.dirname(file_path)
    i = 0
    while i < len(passwords):
        pwd = passwords[i]
        try:
            file_ext = file_path.split(".")[-1]
            match file_ext:
                case "zip" | "gz" | "bz2":
                    Archive(filename=file_path, password=pwd).extractall(dest_filepath)
                case "tar":
                    tarfile.open(file_path, mode="r").extractall(dest_filepath)
                case "7z":
                    py7zr.SevenZipFile(
                        file_path,
                        mode="r",
                        password=pwd,
                    ).extractall(dest_filepath)
                case "rar":
                    rarfile.RarFile(file_path, mode="r").extractall(
                        dest_filepath, pwd=pwd
                    )
            if del_source and os.path.isfile(file_path):
                print("删除文件:", file_path)
                os.remove(file_path)
            print(file_path + " extracted successfully.")
            break
        except Exception as e:  # if extraction failed, probably due to wrong password
            print("Extraction failed:", e)
            if i == len(passwords):
                print("All passwords tried, but extraction failed.")
            i += 1


def check_command(command):
    return shutil.which(command) is not None


# 检查命令是否存在，并提示安装
def check_command_hint(command):
    if not check_command(command):
        if "windows" in platform.platform().lower():
            Error("请安装rar解压工具！\n 下载地址：https://www.rarlab.com/download.htm")
        elif "macos" in platform.platform().lower():
            Error("请安装rar解压工具！\n 控制台执行：brew install rar")
        return False
    return True

# def decompress_file(file_path, dest_filepath, passwords):
#     i = 0
#     while i < len(passwords):
#         pwd = passwords[i]
#         try:
#             file_ext = file_path.split(".")[-1]
#             match file_ext:
#                 case "zip" | "tar" | "gz" | "bz2":
#                     # Archive(file_path).extractall(dest_filepath, password=pwd)
#                     with Archive(file_path) as archive:
#                         list = archive.namelist()
#                         for idx, file in enumerate(list):
#                             percent = round((idx / len(list)) * 100)
#                             print(file.filename, percent)
#                             archive.extract(file, dest_filepath, pwd)
#                         archive.close()
#                 case "7z":
#                     with py7zr.SevenZipFile(
#                         file_path,
#                         mode="r",
#                         password=pwd,
#                     ) as z:
#                         # z.extractall(dest_filepath)
#                         list = z.list()
#                         for idx, file in enumerate(list):
#                             percent = round((idx / len(list)) * 100)
#                             print(file.filename, percent)
#                             z.extract(dest_filepath)
#                         z.close()
#                 case "rar":
#                     # rarfile.RarFile(file_path, mode="r", pwd=pwd).extractall(
#                     #     dest_filepath
#                     # )
#                     with rarfile.RarFile(file_path, mode="r", pwd=pwd) as z:
#                         list = z.namelist()
#                         for idx, file in enumerate(list):
#                             percent = round((idx / len(list)) * 100)
#                             print(file.filename, percent)
#                             z.extract(file, dest_filepath, pwd)
#                         z.close()
#             print("File extracted successfully.")
#             break
#         except Exception as e:  # if extraction failed, probably due to wrong password
#             print("Extraction failed:", e)
#             if i == len(passwords):
#                 print("All passwords tried, but extraction failed.")
#             i += 1
