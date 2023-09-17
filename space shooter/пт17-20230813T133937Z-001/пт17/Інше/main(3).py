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

        with open('f.json', 'r') as f:
            self.notes = json.load(f)

        for note in self.notes.keys():
            self.ui.lw_notes.addItem(note)

        self.ui.btn_save.clicked.connect(self.save_note)

    def save_note(self):
        if self.ui.lw_notes.selectedItems():
            note = self.ui.lw_notes.currentItem().text()
            txt = self.ui.textEdit.toPlainText()

            self.notes[note]['text'] = txt
            with open('f.json', 'w') as f:
                json.dump(self.notes, f)


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
