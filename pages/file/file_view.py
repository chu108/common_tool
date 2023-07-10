import asyncio
import threading

from PySide6.QtCore import SIGNAL
from PySide6.QtWidgets import QWidget

from pages.file.ui_view import Ui_Form
from utils.tool import (
    Error,
    get_files,
    set_bar_value,
    rename_file,
    open_diag_dir,
    decompress_file,
    check_command_hint,
    get_conf,
    set_conf,
)


class File_View(QWidget):
    def __init__(self, main_ui, parent=None):
        super().__init__(parent)
        self.main_ui = main_ui
        self.view = Ui_Form()
        self.view.setupUi(self)
        # self.view.right_box.setStyleSheet("QLineEdit {border-radius: 0px;}")
        # 左侧菜单按钮
        self.view.btn_repl.connect(
            self.view.btn_repl, SIGNAL("clicked()"), self.btn_repl_click
        )
        self.view.btn_unzip.connect(
            self.view.btn_unzip, SIGNAL("clicked()"), self.btn_unzip_click
        )

        self.view.repl_sel_folder.clicked.connect(self.repl_sel_folder_click)
        self.view.repl_btn_push.clicked.connect(self.repl_btn_push_click)

        self.view.unzip_sel_folder.connect(
            self.view.unzip_sel_folder, SIGNAL("clicked()"), self.unzip_sel_folder_click
        )
        self.view.unzip_target_folder.connect(
            self.view.unzip_target_folder,
            SIGNAL("clicked()"),
            self.unzip_target_folder_click,
        )
        self.view.unzip_btn_push.connect(
            self.view.unzip_btn_push, SIGNAL("clicked()"), self.unzip_btn_push_click
        )

        self.view.unzip_passes.setText(get_conf("tmp", "passwords"))
        self.view.unzip_target_path.setText(get_conf("tmp", "unzip_target_path"))

    # 批量替换文件名
    def btn_repl_click(self):
        self.view.right_box.setCurrentIndex(0)

    # 批量替换文件名-选择文件夹
    def repl_sel_folder_click(self):
        self.view.repl_sel_folder.setText(open_diag_dir("选择文件夹"))

    # 批量替换文件名
    def repl_btn_push_click(self):
        self.main_ui.pg_bar.reset()
        folder_path = self.view.repl_folder_path.text()
        find_str = self.view.repl_find_str.text()
        repl_str = self.view.repl_repl_str.text()
        file_type = self.view.repl_type_group.checkedButton().text()
        is_while = self.view.repl_is_while.isChecked()
        if not folder_path or not find_str or not repl_str:
            Error("参数不能为空！")
        file_list = get_files(folder_path, file_type, is_while)
        file_len = len(file_list)
        if file_len == 0:
            Error("没有找到 " + file_type + " 类型文件！")
            return
        # 遍历file_list并打印
        for index, file in enumerate(file_list):
            # 批量替换文件名
            rename_file(file, find_str, repl_str)
            # 设置进度条的值
            set_bar_value(self.main_ui.pg_bar, index + 1, file_len)

    # 批量解压文件
    def btn_unzip_click(self):
        # 验证unrar命令是否存在
        if not check_command_hint("unrar"):
            return
        self.view.right_box.setCurrentIndex(1)

    # 批量解压文件-选择文件夹
    def unzip_sel_folder_click(self):
        path = open_diag_dir("选择源文件夹")
        self.view.unzip_folder_path.setText(path)

    def unzip_target_folder_click(self):
        self.view.unzip_target_path.setText(open_diag_dir("选择目标文件夹"))

    # 批量解压文件 - 内部调用
    def _unzip_btn_push_click(self):
        # 验证unrar命令是否存在
        if not check_command_hint("unrar"):
            return
        unzip_folder_path = self.view.unzip_folder_path.text()
        unzip_target_path = self.view.unzip_target_path.text()
        unzip_passes = self.view.unzip_passes.toPlainText().split("\n")
        unzip_is_while = self.view.unzip_is_while.isChecked()
        unzip_del_source = self.view.unzip_del_source.isChecked()
        print(unzip_folder_path, unzip_passes, unzip_is_while)
        if not unzip_folder_path:
            Error("参数不能为空！")
            return
        file_list = get_files(unzip_folder_path, "解压", unzip_is_while)
        file_len = len(file_list)
        if file_len == 0:
            Error("没有找到支持压缩包！")
            return
        # 遍历file_list并打印
        for index, file in enumerate(file_list):
            # 批量解压文件
            asyncio.run(
                decompress_file(file, unzip_target_path, unzip_passes, unzip_del_source)
            )
            # 设置进度条的值
            set_bar_value(self.main_ui.pg_bar, index + 1, file_len)
        # 保存密码
        set_conf("tmp", "passwords", self.view.unzip_passes.toPlainText())
        # 保存目标文件夹
        set_conf("tmp", "unzip_target_path", unzip_target_path)

    # 批量解压开始
    def unzip_btn_push_click(self):
        try:
            self.main_ui.pg_bar.reset()
            self.main_ui.pg_bar.setFormat("处理中。。。")
            threading.Thread(target=self._unzip_btn_push_click).start()
        except Exception as e:
            Error("无法启动线程:\n" + str(e))
