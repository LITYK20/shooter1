# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'оцман.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(666, 648)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(40, 10, 601, 584))
        self.widget.setObjectName("widget")
        self.Layout1 = QtWidgets.QGridLayout(self.widget)
        self.Layout1.setContentsMargins(0, 0, 0, 0)
        self.Layout1.setObjectName("Layout1")
        self.textEdit_left = QtWidgets.QTextEdit(self.widget)
        self.textEdit_left.setObjectName("textEdit_left")
        self.Layout1.addWidget(self.textEdit_left, 0, 0, 1, 1)
        self.BoxGrop_1 = QtWidgets.QVBoxLayout()
        self.BoxGrop_1.setObjectName("BoxGrop_1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_1_up = QtWidgets.QLabel(self.widget)
        self.label_1_up.setObjectName("label_1_up")
        self.verticalLayout_2.addWidget(self.label_1_up)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget_1_up = QtWidgets.QListWidget(self.widget)
        self.listWidget_1_up.setObjectName("listWidget_1_up")
        self.verticalLayout.addWidget(self.listWidget_1_up)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_1_left = QtWidgets.QPushButton(self.widget)
        self.pushButton_1_left.setObjectName("pushButton_1_left")
        self.horizontalLayout.addWidget(self.pushButton_1_left)
        self.pushButton_2_right = QtWidgets.QPushButton(self.widget)
        self.pushButton_2_right.setStyleSheet("color rgb(255, 22, 1):")
        self.pushButton_2_right.setObjectName("pushButton_2_right")
        self.horizontalLayout.addWidget(self.pushButton_2_right)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.BoxGrop_1.addLayout(self.verticalLayout_2)
        self.pushButton_3_centr = QtWidgets.QPushButton(self.widget)
        self.pushButton_3_centr.setObjectName("pushButton_3_centr")
        self.BoxGrop_1.addWidget(self.pushButton_3_centr)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.BoxGrop_1.addWidget(self.label_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.listWidget_2 = QtWidgets.QListWidget(self.widget)
        self.listWidget_2.setObjectName("listWidget_2")
        self.verticalLayout_3.addWidget(self.listWidget_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_3.addWidget(self.lineEdit_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_4_left = QtWidgets.QPushButton(self.widget)
        self.pushButton_4_left.setObjectName("pushButton_4_left")
        self.horizontalLayout_2.addWidget(self.pushButton_4_left)
        self.pushButton_5_right = QtWidgets.QPushButton(self.widget)
        self.pushButton_5_right.setObjectName("pushButton_5_right")
        self.horizontalLayout_2.addWidget(self.pushButton_5_right)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.pushButton_6_centr = QtWidgets.QPushButton(self.widget)
        self.pushButton_6_centr.setObjectName("pushButton_6_centr")
        self.verticalLayout_3.addWidget(self.pushButton_6_centr)
        self.BoxGrop_1.addLayout(self.verticalLayout_3)
        self.Layout1.addLayout(self.BoxGrop_1, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 666, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_1_up.setText(_translate("MainWindow", "Список заміток"))
        self.pushButton_1_left.setText(_translate("MainWindow", "Створити замітку"))
        self.pushButton_2_right.setText(_translate("MainWindow", "Видалити замітку"))
        self.pushButton_3_centr.setText(_translate("MainWindow", "Зберегти замітку"))
        self.label_2.setText(_translate("MainWindow", "Список тегів"))
        self.pushButton_4_left.setText(_translate("MainWindow", "Додати замітку"))
        self.pushButton_5_right.setText(_translate("MainWindow", "Відкріпити від замітки"))
        self.pushButton_6_centr.setText(_translate("MainWindow", "Шукати замітки по тегу"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
