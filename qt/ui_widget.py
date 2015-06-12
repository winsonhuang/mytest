# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ToPxPtEm.ui'
#
# Created: Fri Jun 12 12:39:25 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(320, 260)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        
        self.lab_Pixels = QtGui.QLabel(self.centralwidget)
        self.lab_Pixels.setGeometry(QtCore.QRect(60, 50, 30, 12))
        self.lab_Pixels.setObjectName(_fromUtf8("lab_Pixels"))
        self.lab_Points = QtGui.QLabel(self.centralwidget)
        self.lab_Points.setGeometry(QtCore.QRect(60, 100, 30, 12))
        self.lab_Points.setObjectName(_fromUtf8("lab_Points"))
        self.lab_EMs = QtGui.QLabel(self.centralwidget)
        self.lab_EMs.setGeometry(QtCore.QRect(60, 150, 30, 12))
        self.lab_EMs.setObjectName(_fromUtf8("lab_EMs"))
        
        self.txt_Pixels = QtGui.QLineEdit(self.centralwidget)
        self.txt_Pixels.setGeometry(QtCore.QRect(100, 50, 100, 20))
        self.txt_Pixels.setObjectName(_fromUtf8("txt_Pixels"))
        self.txt_Points = QtGui.QLineEdit(self.centralwidget)
        self.txt_Points.setGeometry(QtCore.QRect(100, 100, 100, 20))
        self.txt_Points.setObjectName(_fromUtf8("txt_Points"))
        self.txt_EMS = QtGui.QLineEdit(self.centralwidget)
        self.txt_EMS.setGeometry(QtCore.QRect(100, 150, 100, 20))
        self.txt_EMS.setObjectName(_fromUtf8("txt_EMS"))
        
        self.btn_PxTo = QtGui.QPushButton(self.centralwidget)
        self.btn_PxTo.setGeometry(QtCore.QRect(210, 50, 50, 23))
        self.btn_PxTo.setObjectName(_fromUtf8("btn_PxTo"))
        self.btn_PtTo = QtGui.QPushButton(self.centralwidget)
        self.btn_PtTo.setGeometry(QtCore.QRect(210, 100, 50, 23))
        self.btn_PtTo.setObjectName(_fromUtf8("btn_PtTo"))
        self.btn_EmTo = QtGui.QPushButton(self.centralwidget)
        self.btn_EmTo.setGeometry(QtCore.QRect(210, 150, 50, 23))
        self.btn_EmTo.setObjectName(_fromUtf8("btn_EmTo"))
        
                    
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "ToPxPtEm", None))
        self.btn_PxTo.setText(_translate("MainWindow", "PxTo", None))
        self.btn_PtTo.setText(_translate("MainWindow", "PtTo", None))
        self.btn_EmTo.setText(_translate("MainWindow", "EmTo", None))
        self.lab_Pixels.setText(_translate("MainWindow", "Pixels ", None))
        self.lab_Points.setText(_translate("MainWindow", "Points", None))
        self.lab_EMs.setText(_translate("MainWindow", "EMs ", None))

