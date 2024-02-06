from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic, QtWidgets
import sys

class WelcomePage(QtWidgets.QMainWindow):
    
    def __init__(self, parent):
        super(WelcomePage, self).__init__()
        uic.loadUi("welcomePage.ui", self)
        self.parent = parent
        self.clicked = False
        self.setFixedHeight(850)
        self.setFixedWidth(1200)
        self.setAutoFillBackground(True)
        self.color = QColor(255, 255, 255)
        self.setStyleSheet("background-color: RGB(255, 255, 255)")

        # Animasi Landing Page
        self.effect = QGraphicsOpacityEffect(self.logo_aplikasi)
        self.logo_aplikasi.setGraphicsEffect(self.effect)

        # Animasi gerakan judul
        self.anim = QPropertyAnimation(self.logo_aplikasi, b"pos")
        self.anim.setStartValue(QPoint(600, 325))
        self.anim.setEndValue(QPoint(315, 325))
        self.anim.setDuration(1500)
        self.anim_2 = QPropertyAnimation(self.effect, b"opacity")
        # Animasi Judul muncul
        self.anim_2.setStartValue(0)
        self.anim_2.setEndValue(1)
        self.anim_2.setDuration(4500)
        self.anim_3 = QPropertyAnimation(self.effect, b"opacity")
        # Animasi judul menghilang
        self.anim_3.setStartValue(1)
        self.anim_3.setEndValue(0)
        self.anim_3.setDuration(2000)
        self.anim_group = QParallelAnimationGroup()
        self.anim_group.addAnimation(self.anim)
        self.anim_group.addAnimation(self.anim_2)
        self.anim_group.start()
        self.anim_group.finished.connect(self.autoEvent)
        # Timer durasi animasi pewarnaan
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.backgroundAnimation)
        self.timer.start(75)
        
        
    def autoEvent(self):
        # Fungsi pindah halaman otomatis apabila tidak dipencet user.
        self.anim_3.start()
        if not self.clicked:
            self.anim_3.finished.connect(self.goMenu)
        self.anim_2.setStartValue(0)
        self.anim_2.setStartValue(1)
        self.anim_2.setDuration(1)
        self.anim_2.start()
        
    def backgroundAnimation(self):
        # Fungsi pewarnaan pada background animasi.
        if self.color.red() <= 253 and self.color.green() <= 231 and self.color.blue() <= 189:
            self.timer.stop() # stop the timer when the color reaches the target color
        else:
            if self.color.red() <= 253:
                self.color = QColor(self.color.red(), self.color.green() - 1, self.color.blue() - 3)
            else:
                self.color = QColor(self.color.red() - 1, self.color.green() - 1, self.color.blue() - 3)
            self.setStyleSheet("background-color: rgb({},{},{})".format(self.color.red(), self.color.green(), self.color.blue()))
    def mousePressEvent(self, event):
        # Fungsi pencet dari user untuk memasuki menu
        self.clicked = True
        self.anim_3.stop()
        self.goMenu()
    def goMenu(self):
        # Fungsi memasuki menu
        self.parent.pages.setCurrentWidget(self.parent.Menu)
        self.anim_2.setStartValue(0)
        self.anim_2.setStartValue(1)
        self.anim_2.setDuration(1)
        self.anim_2.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    welcomePage = WelcomePage(WelcomePage)
    welcomePage.show()
    sys.exit(app.exec_())
