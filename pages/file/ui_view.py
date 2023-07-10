# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'view.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, Qt)
from PySide6.QtWidgets import (QButtonGroup, QCheckBox, QFormLayout,
                               QGridLayout, QHBoxLayout, QLabel, QLayout,
                               QLineEdit, QPushButton, QRadioButton, QSizePolicy,
                               QStackedWidget, QTextEdit, QVBoxLayout, QWidget)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(762, 542)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 12, 0, 0)
        self.right_box = QStackedWidget(Form)
        self.right_box.setObjectName(u"right_box")
        self.right_box.setStyleSheet(u"background-color:rgb(65, 70, 81);border-radius:8px;")
        self.page_repl = QWidget()
        self.page_repl.setObjectName(u"page_repl")
        self.gridLayout_2 = QGridLayout(self.page_repl)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.repl_layout = QFormLayout()
        self.repl_layout.setObjectName(u"repl_layout")
        self.repl_layout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.repl_layout.setRowWrapPolicy(QFormLayout.DontWrapRows)
        self.repl_layout.setLabelAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.label = QLabel(self.page_repl)
        self.label.setObjectName(u"label")

        self.repl_layout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.repl_folder_path = QLineEdit(self.page_repl)
        self.repl_folder_path.setObjectName(u"repl_folder_path")

        self.gridLayout_4.addWidget(self.repl_folder_path, 0, 0, 1, 1)

        self.repl_sel_folder = QPushButton(self.page_repl)
        self.repl_sel_folder.setObjectName(u"repl_sel_folder")

        self.gridLayout_4.addWidget(self.repl_sel_folder, 0, 1, 1, 1)

        self.repl_layout.setLayout(0, QFormLayout.FieldRole, self.gridLayout_4)

        self.label_5 = QLabel(self.page_repl)
        self.label_5.setObjectName(u"label_5")

        self.repl_layout.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.label_2 = QLabel(self.page_repl)
        self.label_2.setObjectName(u"label_2")

        self.repl_layout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.repl_find_str = QLineEdit(self.page_repl)
        self.repl_find_str.setObjectName(u"repl_find_str")

        self.repl_layout.setWidget(2, QFormLayout.FieldRole, self.repl_find_str)

        self.label_3 = QLabel(self.page_repl)
        self.label_3.setObjectName(u"label_3")

        self.repl_layout.setWidget(3, QFormLayout.LabelRole, self.label_3)

        self.repl_repl_str = QLineEdit(self.page_repl)
        self.repl_repl_str.setObjectName(u"repl_repl_str")

        self.repl_layout.setWidget(3, QFormLayout.FieldRole, self.repl_repl_str)

        self.label_4 = QLabel(self.page_repl)
        self.label_4.setObjectName(u"label_4")

        self.repl_layout.setWidget(4, QFormLayout.LabelRole, self.label_4)

        self.repl_btn_push = QPushButton(self.page_repl)
        self.repl_btn_push.setObjectName(u"repl_btn_push")

        self.repl_layout.setWidget(5, QFormLayout.FieldRole, self.repl_btn_push)

        self.repl_type_layout = QHBoxLayout()
        self.repl_type_layout.setObjectName(u"repl_type_layout")
        self.repl_type_all = QRadioButton(self.page_repl)
        self.repl_type_group = QButtonGroup(Form)
        self.repl_type_group.setObjectName(u"repl_type_group")
        self.repl_type_group.addButton(self.repl_type_all)
        self.repl_type_all.setObjectName(u"repl_type_all")

        self.repl_type_layout.addWidget(self.repl_type_all)

        self.repl_type_video = QRadioButton(self.page_repl)
        self.repl_type_group.addButton(self.repl_type_video)
        self.repl_type_video.setObjectName(u"repl_type_video")

        self.repl_type_layout.addWidget(self.repl_type_video)

        self.repl_type_audio = QRadioButton(self.page_repl)
        self.repl_type_group.addButton(self.repl_type_audio)
        self.repl_type_audio.setObjectName(u"repl_type_audio")

        self.repl_type_layout.addWidget(self.repl_type_audio)

        self.repl_type_file = QRadioButton(self.page_repl)
        self.repl_type_group.addButton(self.repl_type_file)
        self.repl_type_file.setObjectName(u"repl_type_file")
        self.repl_type_file.setChecked(True)

        self.repl_type_layout.addWidget(self.repl_type_file)

        self.repl_type_img = QRadioButton(self.page_repl)
        self.repl_type_group.addButton(self.repl_type_img)
        self.repl_type_img.setObjectName(u"repl_type_img")

        self.repl_type_layout.addWidget(self.repl_type_img)

        self.repl_layout.setLayout(1, QFormLayout.FieldRole, self.repl_type_layout)

        self.repl_is_while = QCheckBox(self.page_repl)
        self.repl_is_while.setObjectName(u"repl_is_while")
        self.repl_is_while.setChecked(True)

        self.repl_layout.setWidget(4, QFormLayout.FieldRole, self.repl_is_while)

        self.gridLayout_2.addLayout(self.repl_layout, 0, 0, 1, 1)

        self.right_box.addWidget(self.page_repl)
        self.page_unzip = QWidget()
        self.page_unzip.setObjectName(u"page_unzip")
        self.gridLayout_3 = QGridLayout(self.page_unzip)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.label_6 = QLabel(self.page_unzip)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_6)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.unzip_folder_path = QLineEdit(self.page_unzip)
        self.unzip_folder_path.setObjectName(u"unzip_folder_path")

        self.horizontalLayout.addWidget(self.unzip_folder_path)

        self.unzip_sel_folder = QPushButton(self.page_unzip)
        self.unzip_sel_folder.setObjectName(u"unzip_sel_folder")

        self.horizontalLayout.addWidget(self.unzip_sel_folder)

        self.formLayout_3.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout)

        self.label_9 = QLabel(self.page_unzip)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_9)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.unzip_target_path = QLineEdit(self.page_unzip)
        self.unzip_target_path.setObjectName(u"unzip_target_path")

        self.horizontalLayout_2.addWidget(self.unzip_target_path)

        self.unzip_target_folder = QPushButton(self.page_unzip)
        self.unzip_target_folder.setObjectName(u"unzip_target_folder")

        self.horizontalLayout_2.addWidget(self.unzip_target_folder)

        self.formLayout_3.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_2)

        self.label_7 = QLabel(self.page_unzip)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_7)

        self.unzip_passes = QTextEdit(self.page_unzip)
        self.unzip_passes.setObjectName(u"unzip_passes")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.unzip_passes)

        self.label_8 = QLabel(self.page_unzip)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.label_8)

        self.unzip_is_while = QCheckBox(self.page_unzip)
        self.unzip_is_while.setObjectName(u"unzip_is_while")

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.unzip_is_while)

        self.label_10 = QLabel(self.page_unzip)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_3.setWidget(4, QFormLayout.LabelRole, self.label_10)

        self.unzip_del_source = QCheckBox(self.page_unzip)
        self.unzip_del_source.setObjectName(u"unzip_del_source")

        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.unzip_del_source)

        self.unzip_btn_push = QPushButton(self.page_unzip)
        self.unzip_btn_push.setObjectName(u"unzip_btn_push")

        self.formLayout_3.setWidget(5, QFormLayout.FieldRole, self.unzip_btn_push)

        self.gridLayout_3.addLayout(self.formLayout_3, 0, 0, 1, 1)

        self.right_box.addWidget(self.page_unzip)

        self.gridLayout.addWidget(self.right_box, 0, 1, 1, 1)

        self.left_box = QWidget(Form)
        self.left_box.setObjectName(u"left_box")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left_box.sizePolicy().hasHeightForWidth())
        self.left_box.setSizePolicy(sizePolicy)
        self.left_box.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.left_box.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout = QVBoxLayout(self.left_box)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, -1, -1)
        self.btn_repl = QPushButton(self.left_box)
        self.left_btn_group = QButtonGroup(Form)
        self.left_btn_group.setObjectName(u"left_btn_group")
        self.left_btn_group.addButton(self.btn_repl)
        self.btn_repl.setObjectName(u"btn_repl")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_repl.sizePolicy().hasHeightForWidth())
        self.btn_repl.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.btn_repl, 0, Qt.AlignTop)

        self.btn_unzip = QPushButton(self.left_box)
        self.left_btn_group.addButton(self.btn_unzip)
        self.btn_unzip.setObjectName(u"btn_unzip")
        sizePolicy1.setHeightForWidth(self.btn_unzip.sizePolicy().hasHeightForWidth())
        self.btn_unzip.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.btn_unzip, 0, Qt.AlignTop)

        self.gridLayout.addWidget(self.left_box, 0, 0, 1, 1, Qt.AlignTop)

        self.retranslateUi(Form)

        self.right_box.setCurrentIndex(1)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u6587\u4ef6\u5939", None))
        self.repl_sel_folder.setText(QCoreApplication.translate("Form", u"\u9009\u62e9", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u6587\u4ef6\u7c7b\u578b", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u67e5\u627e\u5b57\u7b26\u4e32", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u66ff\u6362\u5b57\u7b26\u4e32", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u5305\u542b\u5b50\u76ee\u5f55", None))
        self.repl_btn_push.setText(QCoreApplication.translate("Form", u"\u6279 \u91cf \u66ff \u6362", None))
        self.repl_type_all.setText(QCoreApplication.translate("Form", u"\u6240\u6709", None))
        self.repl_type_video.setText(QCoreApplication.translate("Form", u"\u89c6\u9891", None))
        self.repl_type_audio.setText(QCoreApplication.translate("Form", u"\u97f3\u9891", None))
        self.repl_type_file.setText(QCoreApplication.translate("Form", u"\u6587\u672c", None))
        self.repl_type_img.setText(QCoreApplication.translate("Form", u"\u56fe\u7247", None))
        self.repl_is_while.setText(QCoreApplication.translate("Form", u"\u662f", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u6587\u4ef6\u5939", None))
        self.unzip_sel_folder.setText(QCoreApplication.translate("Form", u"\u9009\u62e9", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u76ee\u6807\u6587\u4ef6\u5939", None))
        self.unzip_target_path.setPlaceholderText(QCoreApplication.translate("Form",
                                                                             u"\u4e3a\u7a7a\u5219\u4e0e\u6e90\u6587\u4ef6\u5728\u540c\u4e00\u76ee\u5f55",
                                                                             None))
        self.unzip_target_folder.setText(QCoreApplication.translate("Form", u"\u9009\u62e9", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u89e3\u538b\u5bc6\u7801\u5217\u8868", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u5305\u542b\u5b50\u76ee\u5f55", None))
        self.unzip_is_while.setText(QCoreApplication.translate("Form", u"\u662f", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"\u5220\u9664\u6e90\u6587\u4ef6", None))
        self.unzip_del_source.setText(QCoreApplication.translate("Form", u"\u662f", None))
        self.unzip_btn_push.setText(QCoreApplication.translate("Form", u"\u6279 \u91cf \u89e3 \u538b", None))
        self.btn_repl.setText(QCoreApplication.translate("Form", u"\u6587\u4ef6\u540d\u66ff\u6362", None))
        self.btn_unzip.setText(QCoreApplication.translate("Form", u"\u6279\u91cf\u89e3\u538b\u7f29", None))
    # retranslateUi
