# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject)
from PySide6.QtWidgets import (QGridLayout, QProgressBar, QTabWidget, QWidget)


class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        self.gridLayout_2 = QGridLayout(Widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tab_view = QTabWidget(Widget)
        self.tab_view.setObjectName(u"tab_view")
        self.tab_file = QWidget()
        self.tab_file.setObjectName(u"tab_file")
        self.gridLayout = QGridLayout(self.tab_file)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tab_view.addTab(self.tab_file, "")

        self.gridLayout_2.addWidget(self.tab_view, 0, 0, 1, 1)

        self.pg_bar = QProgressBar(Widget)
        self.pg_bar.setObjectName(u"pg_bar")
        self.pg_bar.setValue(0)

        self.gridLayout_2.addWidget(self.pg_bar, 1, 0, 1, 1)

        self.retranslateUi(Widget)

        self.tab_view.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(Widget)

    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.tab_view.setTabText(self.tab_view.indexOf(self.tab_file),
                                 QCoreApplication.translate("Widget", u"\u5173\u4e8e", None))
    # retranslateUi
