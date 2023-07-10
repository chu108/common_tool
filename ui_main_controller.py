from PySide6.QtWidgets import QWidget

from pages.file.file_view import File_View
from ui_main import Ui_Widget as Ui_Main


class Main_Page(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Main()
        self.ui.setupUi(self)

        self.file_view = File_View(self.ui)
        self.ui.tab_view.insertTab(0, self.file_view, "文件处理")
        self.ui.tab_view.setCurrentWidget(self.file_view)
