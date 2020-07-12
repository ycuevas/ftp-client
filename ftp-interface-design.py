# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ftp-interface-design.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(576, 464)
        Dialog.setStyleSheet("background-color: #3a4055;\n"
"color: white")
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.serverLabel = QtWidgets.QLabel(Dialog)
        self.serverLabel.setObjectName("serverLabel")
        self.gridLayout.addWidget(self.serverLabel, 0, 0, 1, 1)
        self.serverName = QtWidgets.QLineEdit(Dialog)
        self.serverName.setMinimumSize(QtCore.QSize(482, 0))
        self.serverName.setMaximumSize(QtCore.QSize(482, 16777215))
        self.serverName.setText("")
        self.serverName.setObjectName("serverName")
        self.gridLayout.addWidget(self.serverName, 0, 1, 1, 1)
        self.usernameLabel = QtWidgets.QLabel(Dialog)
        self.usernameLabel.setObjectName("usernameLabel")
        self.gridLayout.addWidget(self.usernameLabel, 1, 0, 1, 1)
        self.username = QtWidgets.QLineEdit(Dialog)
        self.username.setText("")
        self.username.setObjectName("username")
        self.gridLayout.addWidget(self.username, 1, 1, 1, 1)
        self.passwordLabel = QtWidgets.QLabel(Dialog)
        self.passwordLabel.setObjectName("passwordLabel")
        self.gridLayout.addWidget(self.passwordLabel, 2, 0, 1, 1)
        self.password = QtWidgets.QLineEdit(Dialog)
        self.password.setText("")
        self.password.setObjectName("password")
        self.gridLayout.addWidget(self.password, 2, 1, 1, 1)
        self.listView = QtWidgets.QListView(Dialog)
        self.listView.setObjectName("listView")
        self.gridLayout.addWidget(self.listView, 3, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.serverLabel.setText(_translate("Dialog", "Server"))
        self.usernameLabel.setText(_translate("Dialog", "Username"))
        self.passwordLabel.setText(_translate("Dialog", "Password"))

