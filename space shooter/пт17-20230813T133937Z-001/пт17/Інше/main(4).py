import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
# from PyQt5 import uic
from ui import Ui_MainWindow
import json
from PyQt5.QtWidgets import QInputDialog


class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_create.clicked.connect(self.new_note)

        self.notes = {}

    def new_note(self):
        txt, result = QInputDialog.getText(self.ui.centralwidget, 'Нова замітка', "Введіть назву замітки")
        if result:
            self.notes[txt] = {'text': '', 'tags': []}
            self.ui.lw_notes.addItem(txt)
            with open('f.json', 'w') as f:
                json.dump(self.notes, f)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Widget()
    ex.show()
    sys.exit(app.exec_())
