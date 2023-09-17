# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(817, 750)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 10, 520, 572))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lw_notes = QtWidgets.QListWidget(self.widget)
        self.lw_notes.setObjectName("lw_notes")
        self.gridLayout.addWidget(self.lw_notes, 1, 1, 1, 2)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 2)
        self.btn_create = QtWidgets.QPushButton(self.widget)
        self.btn_create.setObjectName("btn_create")
        self.gridLayout.addWidget(self.btn_create, 2, 1, 1, 1)
        self.btn_delete = QtWidgets.QPushButton(self.widget)
        self.btn_delete.setObjectName("btn_delete")
        self.gridLayout.addWidget(self.btn_delete, 2, 2, 1, 1)
        self.btn_safe = QtWidgets.QPushButton(self.widget)
        self.btn_safe.setObjectName("btn_safe")
        self.gridLayout.addWidget(self.btn_safe, 3, 1, 1, 2)
        self.lw_tags = QtWidgets.QListWidget(self.widget)
        self.lw_tags.setObjectName("lw_tags")
        self.gridLayout.addWidget(self.lw_tags, 5, 1, 1, 2)
        self.btn_unfasten = QtWidgets.QPushButton(self.widget)
        self.btn_unfasten.setObjectName("btn_unfasten")
        self.gridLayout.addWidget(self.btn_unfasten, 7, 2, 1, 1)
        self.le_search = QtWidgets.QLineEdit(self.widget)
        self.le_search.setObjectName("le_search")
        self.gridLayout.addWidget(self.le_search, 6, 1, 1, 2)
        self.btn_add = QtWidgets.QPushButton(self.widget)
        self.btn_add.setObjectName("btn_add")
        self.gridLayout.addWidget(self.btn_add, 7, 1, 1, 1)
        self.btn_search = QtWidgets.QPushButton(self.widget)
        self.btn_search.setObjectName("btn_search")
        self.gridLayout.addWidget(self.btn_search, 8, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 1, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.widget)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 0, 0, 9, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Список заміток"))
        self.btn_create.setText(_translate("MainWindow", "Створити  замітку"))
        self.btn_delete.setText(_translate("MainWindow", "Видалити замітку"))
        self.btn_safe.setText(_translate("MainWindow", "Зберегти замітку"))
        self.btn_unfasten.setText(_translate("MainWindow", "Відкріпити від замітки"))
        self.le_search.setText(_translate("MainWindow", "Введіть тег.."))
        self.btn_add.setText(_translate("MainWindow", "Додати  до замітки"))
        self.btn_search.setText(_translate("MainWindow", "Шукати замітки по тегу"))
        self.label_2.setText(_translate("MainWindow", "Список тегів"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
