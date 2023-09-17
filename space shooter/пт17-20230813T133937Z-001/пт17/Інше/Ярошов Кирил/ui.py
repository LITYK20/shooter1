# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(816, 717)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 781, 641))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.textEdit = QtWidgets.QTextEdit(self.widget)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 0, 0, 9, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.listWidget = QtWidgets.QListWidget(self.widget)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 1, 1, 1, 2)
        self.btn_create = QtWidgets.QPushButton(self.widget)
        self.btn_create.setObjectName("btn_create")
        self.gridLayout.addWidget(self.btn_create, 2, 1, 1, 1)
        self.btn_delete = QtWidgets.QPushButton(self.widget)
        self.btn_delete.setObjectName("btn_delete")
        self.gridLayout.addWidget(self.btn_delete, 2, 2, 1, 1)
        self.btn_save_notes = QtWidgets.QPushButton(self.widget)
        self.btn_save_notes.setObjectName("btn_save_notes")
        self.gridLayout.addWidget(self.btn_save_notes, 3, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 1, 1, 1)
        self.listWidget_2 = QtWidgets.QListWidget(self.widget)
        self.listWidget_2.setObjectName("listWidget_2")
        self.gridLayout.addWidget(self.listWidget_2, 5, 1, 1, 2)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 6, 1, 1, 2)
        self.btn_add = QtWidgets.QPushButton(self.widget)
        self.btn_add.setObjectName("btn_add")
        self.gridLayout.addWidget(self.btn_add, 7, 1, 1, 1)
        self.btn_fix = QtWidgets.QPushButton(self.widget)
        self.btn_fix.setObjectName("btn_fix")
        self.gridLayout.addWidget(self.btn_fix, 7, 2, 1, 1)
        self.btn_save_tage = QtWidgets.QPushButton(self.widget)
        self.btn_save_tage.setObjectName("btn_save_tage")
        self.gridLayout.addWidget(self.btn_save_tage, 8, 1, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 816, 21))
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
        self.label.setText(_translate("MainWindow", "Список заміток:"))
        self.btn_create.setText(_translate("MainWindow", "Створити замітку"))
        self.btn_delete.setText(_translate("MainWindow", "Видалити замітку"))
        self.btn_save_notes.setText(_translate("MainWindow", "Зберегти замітку"))
        self.label_2.setText(_translate("MainWindow", "Список тегів"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Введіть тег..."))
        self.btn_add.setText(_translate("MainWindow", "Додати до замітки"))
        self.btn_fix.setText(_translate("MainWindow", "Відкрипити від заміток"))
        self.btn_save_tage.setText(_translate("MainWindow", "Шукати замітки по тегу"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
