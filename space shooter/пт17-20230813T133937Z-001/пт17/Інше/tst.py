import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
# from PyQt5 import uic
from main import Ui_MainWindow
from PyQt5.QtGui import QIcon

import os
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QFileDialog,
    QLabel, QPushButton, QListWidget,
    QHBoxLayout, QVBoxLayout
)
from PyQt5.QtCore import Qt  # потрібна константа Qt.KeepAspectRatio для зміни розмірів із збереженням пропорцій
from PyQt5.QtGui import QPixmap  # оптимізована для показу на екрані картинка

from PIL import Image
from PIL.ImageQt import ImageQt  # Для перенесення графіки з Pillow до QT
from PIL import ImageFilter
from PIL.ImageFilter import (
    BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
    EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN,
    GaussianBlur, UnsharpMask
)
workdir = ''


def filter(files, extensions):
    # створення порожнього списку, куди ми будемо додавати файли, які нам підходять
    result = []
    # прохід по цьому списку
    for f in files:
        # прохід по списку дозволених розширень
        for e in extensions:
            # перевірка на те, чи закінчується поточний файл на розширення
            if f.endswith(e):
                # додавання поточного файлу у список графічних файлів
                result.append(f)
    # повернення списку графічних файлів
    return result


def chooseWorkdir():
    # робимо workdir глобальною змінною
    global workdir
    # викликаємо вікно з вибором папки, передаємо результат у змінну workdir
    workdir = QFileDialog.getExistingDirectory()


class ImageProcessor():
    # створення ініту, в ньому створюємо основні властивості
    def __init__(self):
        self.image = None  #  об'єкт картинки, за замовчуванням None
        self.filename = None  #  назва файлу картинки, за замовчуванням None
        self.save_dir = 'abc'  #  шлях до папки, куди треба зберігати картинки

    def load_image(self, filename):
        self.filename = filename  #  запам'ятувємо назву файлу
        file_path = os.path.join(workdir, filename)  #  додаємо шлях до папки до назви картинки, щоб отримати шлях до файлу

        self.image = Image.open(file_path)  # відкриваємо картинку

    def save_image(self):
        path = os.path.join(workdir, self.save_dir)
        if not (os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path, self.filename)
        self.image.save(image_path)

    def do_bw(self):
        self.image = self.image.convert('L')  # робимо картинку чб
        self.save_image()  # зберігаємо картикну
        image_path = os.path.join(workdir, self.save_dir, self.filename)  # генеруємо шлях, до тільки що збереженої картинки
        #ex.show_image(image_path) # показуємо картинку на екрані

    def do_flip(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.save_image()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        ex.show_image(image_path)

    def do_sharp(self):
        self.image = self.image.filter(ImageFilter.SHARPEN)
        self.save_image()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        ex.show_image(image_path)

    def do_rotate(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.save_image()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        ex.show_image(image_path)

    def do_blur(self):
        self.image = self.image.filter(ImageFilter.BLUR)
        self.save_image()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        ex.show_image(image_path)

workimage = ImageProcessor()

class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.label.itemClicked.connect(self.show_choosen_image)
        self.ui.pushButton_6.clicked.connect(workimage.do_bw)
        self.ui.pushButton_3.clicked.connect(workimage.do_rotate)
        self.ui.pushButton_2.clicked.connect(workimage.do_rotate2)

    def show_choosen_image(self):
        text = self.ui.label.currentItem().text()
        workimage.load_image(text)
        self.show_image(os.path.join(workdir, text))

    def show_image(self, path):
        self.ui.label_2.hide()
        pixmap = QPixmap(path)
        width = self.ui.label_2.width()
        height = self.ui.label_2.height()
        pixmap = pixmap.scaled(width, height, Qt.KeepAspectRatio)
        self.ui.label_2.setPixmap(pixmap)
        self.ui.label_2.show()

app = QApplication(sys.argv)
ex = Widget()
ex.show()

def showFilenamesList():
    fine = ['.jpg', '.jpeg', '.png', '.gif', '.bmp'] # створення списку валідних розширень
    chooseWorkdir() # виклик функції для отримання шляху до папки
    filenames = filter(os.listdir(workdir), fine) # виклик функції для фільтрації. Виклик функції для отримання списку всіх файлів в папці

    ex.ui.label.clear() # очищення тексту(label)
    for files in filenames: # перебираємо всі дозволені файли
        ex.ui.label.addItem(files) # додаємо всі відібрані файли

ex.ui.pushButton.clicked.connect(showFilenamesList)

sys.exit(app.exec_())