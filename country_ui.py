# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'country_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
from graphics_drawing import *


class Ui_country_ui(object):
    def setupUi(self, country_ui):
        country_ui.setObjectName("country_ui")
        country_ui.resize(1000, 600)
        self.centralwidget = QtWidgets.QWidget(country_ui)
        self.centralwidget.setObjectName("centralwidget")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(20, 10, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_2.setGeometry(QtCore.QRect(160, 10, 110, 22))
        self.dateEdit_2.setObjectName("dateEdit_2")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(290, 10, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.statistical_methods = QtWidgets.QComboBox(self.centralwidget)
        self.statistical_methods.setGeometry(QtCore.QRect(380, 10, 75, 22))
        self.statistical_methods.setObjectName("statistical_methods")
        self.statistical_methods.addItem("")
        self.statistical_methods.addItem("")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(470, 10, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(560, 10, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.refreshlebal = QtWidgets.QLabel(self.centralwidget)
        self.refreshlebal.setGeometry((QtCore.QRect(690,10,300,23)))
        self.browser = QWebEngineView(self.centralwidget)
        self.browser.setGeometry(QtCore.QRect(40, 40, 900, 500))
        self.browser.load(QUrl('http://localhost:63342/main.py/line.html?_ijt=6rfathn5e84vqqcf2r8etbp83q'))
        self.browser.setObjectName("htmlwindow")

        country_ui.setCentralWidget(self.centralwidget)

        self.pushButton.clicked.connect(lambda :self.get_time())
        self.pushButton_2.clicked.connect(lambda:self.refresh_map())

        self.retranslateUi(country_ui)
        QtCore.QMetaObject.connectSlotsByName(country_ui)

    def retranslateUi(self, country_ui):
        _translate = QtCore.QCoreApplication.translate
        country_ui.setWindowTitle(_translate("country_ui", "国家疫情数据统计折线图"))
        self.comboBox.setItemText(0, _translate("country_ui", "China"))
        self.comboBox.setItemText(1, _translate("country_ui", "US"))
        self.comboBox.setItemText(2, _translate("country_ui", "India"))
        self.comboBox.setItemText(3, _translate("country_ui", "France"))
        self.comboBox.setItemText(4, _translate("country_ui", "Russia"))
        self.comboBox.setItemText(5, _translate("country_ui", "Brazil"))

        self.statistical_methods.setItemText(0, _translate("country_ui", "普通坐标"))
        self.statistical_methods.setItemText(1, _translate("country_ui", "对数坐标"))
        self.pushButton.setText(_translate("country_ui", "修改数据"))
        self.pushButton_2.setText(_translate("country_ui", "刷新"))
        self.refreshlebal.setText(_translate("china_ui", "请等候地图加载"))

    def get_time(self):
        first_time = self.dateEdit.dateTime()
        end_time = self.dateEdit_2.dateTime()
        country = self.comboBox.currentText()
        methods = self.statistical_methods.currentText()

        f_time = first_time.toString("MM-dd-yyyy")
        e_time = end_time.toString("MM-dd-yyyy")
        render_dayly_chart(str(f_time), str(e_time), str(country), str(methods))
        self.refreshlebal.setText("加载完毕,请刷新")


    def refresh_map(self):
        self.browser.load(QUrl('http://localhost:63342/main.py/line.html?_ijt=6rfathn5e84vqqcf2r8etbp83q'))
        self.refreshlebal.setText("请等候地图加载")

