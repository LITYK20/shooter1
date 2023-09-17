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
        self.ui.btn_del.clicked.connect(self.dell_note)
        self.ui.lw_notes.itemClicked.connect(self.show_note)
        self.ui.tag_create.clicked.connect(self.add_tag)
        self.ui.tag_del.clicked.connect(self.del_tag)

    def del_tag(self):
        if self.ui.lw_notes.selectedItems() and self.ui.lw_tags.selectedItems():
            note = self.ui.lw_notes.currentItem().text()
            tag = self.ui.lw_tags.currentItem().text()

            self.notes[note]['tags'].remove(tag)
            with open('f.json', 'w') as f:
                json.dump(self.notes, f)
            self.show_note()

    def add_tag(self):
        if self.ui.lw_notes.selectedItems() and self.ui.lineEdit.text():
            note = self.ui.lw_notes.currentItem().text()  # назва обраної замітки
            tag = self.ui.lineEdit.text()

            self.ui.lw_tags.addItem(tag)
            self.ui.lineEdit.clear()

            self.notes[note]['tags'].append(tag)
            with open('f.json', 'w') as f:
                json.dump(self.notes, f)

    def show_note(self):
        note = self.ui.lw_notes.currentItem().text()
        txt = self.notes[note]['text']

        self.ui.textEdit.setText(txt)
        self.ui.lw_tags.clear()
        for tag in self.notes[note]['tags']:
            self.ui.lw_tags.addItem(tag)

    def dell_note(self):
        if self.ui.lw_notes.selectedItems():
            note = self.ui.lw_notes.currentItem().text()
            del self.notes[note]

            self.ui.lw_notes.clear()
            for note in self.notes:
                self.ui.lw_notes.addItem(note)

            with open('f.json', 'w') as f:
                json.dump(self.notes, f)

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
