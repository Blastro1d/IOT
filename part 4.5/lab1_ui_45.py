# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lab1_45.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1125, 602)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 20, 88, 27))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("background-color: green; color: white; font-weight: bold;")
        self.pushButton.setObjectName("pushButton")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 60, 211, 211))
        self.groupBox.setObjectName("groupBox")
        self.spinBox = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox.setGeometry(QtCore.QRect(20, 50, 171, 28))
        self.spinBox.setSuffix("")
        self.spinBox.setPrefix("")
        self.spinBox.setMaximum(1000)
        self.spinBox.setProperty("value", 10)
        self.spinBox.setObjectName("spinBox")
        self.spinBox_2 = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_2.setGeometry(QtCore.QRect(20, 110, 171, 28))
        self.spinBox_2.setMaximum(1000)
        self.spinBox_2.setProperty("value", 10)
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_3 = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_3.setGeometry(QtCore.QRect(20, 170, 171, 28))
        self.spinBox_3.setMaximum(1000)
        self.spinBox_3.setProperty("value", 60)
        self.spinBox_3.setObjectName("spinBox_3")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 30, 191, 19))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 151, 19))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 150, 181, 19))
        self.label_3.setObjectName("label_3")
        self.MplWidget = MplWidget(Form)
        self.MplWidget.setGeometry(QtCore.QRect(240, 60, 851, 391))
        self.MplWidget.setObjectName("MplWidget")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 380, 211, 31))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.Table_button = QtWidgets.QPushButton(Form)
        self.Table_button.setGeometry(QtCore.QRect(10, 420, 211, 27))
        self.Table_button.setObjectName("Table_button")
        self.mean_X = QtWidgets.QLCDNumber(Form)
        self.mean_X.setGeometry(QtCore.QRect(400, 490, 71, 31))
        self.mean_X.setProperty("value", 0.0)
        self.mean_X.setObjectName("mean_X")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(250, 490, 101, 19))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(240, 550, 131, 19))
        self.label_5.setObjectName("label_5")
        self.Standard_dev_X = QtWidgets.QLCDNumber(Form)
        self.Standard_dev_X.setGeometry(QtCore.QRect(400, 550, 71, 31))
        self.Standard_dev_X.setProperty("value", 0.0)
        self.Standard_dev_X.setObjectName("Standard_dev_X")
        self.mean_Y = QtWidgets.QLCDNumber(Form)
        self.mean_Y.setGeometry(QtCore.QRect(540, 490, 71, 31))
        self.mean_Y.setProperty("value", 0.0)
        self.mean_Y.setObjectName("mean_Y")
        self.mean_Z = QtWidgets.QLCDNumber(Form)
        self.mean_Z.setGeometry(QtCore.QRect(700, 490, 71, 31))
        self.mean_Z.setProperty("value", 0.0)
        self.mean_Z.setObjectName("mean_Z")
        self.Standard_dev_Y = QtWidgets.QLCDNumber(Form)
        self.Standard_dev_Y.setGeometry(QtCore.QRect(540, 550, 71, 31))
        self.Standard_dev_Y.setProperty("value", 0.0)
        self.Standard_dev_Y.setObjectName("Standard_dev_Y")
        self.Standard_dev_Z = QtWidgets.QLCDNumber(Form)
        self.Standard_dev_Z.setGeometry(QtCore.QRect(700, 550, 71, 31))
        self.Standard_dev_Z.setProperty("value", 0.0)
        self.Standard_dev_Z.setObjectName("Standard_dev_Z")
        self.time_left = QtWidgets.QLCDNumber(Form)
        self.time_left.setGeometry(QtCore.QRect(963, 20, 91, 23))
        self.time_left.setAutoFillBackground(False)
        self.time_left.setStyleSheet("background-color: black;")
        self.time_left.setDigitCount(4)
        self.time_left.setProperty("value", 0.0)
        self.time_left.setProperty("intValue", 0)
        self.time_left.setObjectName("time_left")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(400, 460, 66, 19))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(540, 460, 61, 19))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(700, 460, 66, 19))
        self.label_8.setObjectName("label_8")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Start"))
        self.groupBox.setTitle(_translate("Form", "GroupBox"))
        self.label.setText(_translate("Form", "Measurement interval in ms"))
        self.label_2.setText(_translate("Form", "X-axis interval"))
        self.label_3.setText(_translate("Form", "Measurement duration in s"))
        self.plainTextEdit.setPlaceholderText(_translate("Form", "Give a filename for table..."))
        self.Table_button.setText(_translate("Form", "Make table"))
        self.label_4.setText(_translate("Form", "Mean values"))
        self.label_5.setText(_translate("Form", "Standerd deviation"))
        self.label_6.setText(_translate("Form", "X"))
        self.label_7.setText(_translate("Form", "Y"))
        self.label_8.setText(_translate("Form", "Z"))
from mplwidget import MplWidget
