# coding:utf-8
from PIL import Image
import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout,
                             QLabel, QApplication)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class Atsumori(QWidget):
    hbox = ""

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.hbox = QHBoxLayout(self)
        self.setLayout(self.hbox)
        # self.move(0, 0)
        self.showFullScreen()
        self.setWindowTitle('Atsumori!!')

    def display(self):
        self.show()

    def showPic(self, width, height, path):
        # QPixmapオブジェクト作成
        pixmap = QPixmap(path)
        pixmap.scaled(width, height, Qt.KeepAspectRatioByExpanding)
        # ラベルを作ってその中に画像を置く
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        lbl.setAlignment(Qt.AlignCenter)
        self.hbox.addWidget(lbl)


def showImageApp(path):
    app = QApplication(sys.argv)
    ex = Atsumori()
    ex.showPic(app.desktop().width(), app.desktop().height(), path)
    ex.display()
    sys.exit(app.exec_())


if __name__ == '__main__':
    path = "src/atsumori.png"
    showImageApp(path)
