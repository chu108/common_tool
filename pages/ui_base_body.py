# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'base_body.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject)
from PySide6.QtWidgets import (QGridLayout, QStackedWidget,
                               QVBoxLayout, QWidget)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(762, 542)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.left_box = QWidget(Form)
        self.left_box.setObjectName(u"left_box")
        self.verticalLayout = QVBoxLayout(self.left_box)
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.gridLayout.addWidget(self.left_box, 0, 0, 1, 1)

        self.right_box = QStackedWidget(Form)
        self.right_box.setObjectName(u"right_box")
        self.right_box.setStyleSheet(u"background-color:rgb(110, 110, 110)")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_2 = QGridLayout(self.page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.right_box.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_3 = QGridLayout(self.page_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.right_box.addWidget(self.page_2)

        self.gridLayout.addWidget(self.right_box, 0, 1, 1, 1)

        self.retranslateUi(Form)

        self.right_box.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
    # retranslateUi
