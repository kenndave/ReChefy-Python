from PyQt5.QtWidgets import *
from PyQt5 import uic, QtWidgets, QtGui, QtCore
import sys
import fontLoader

class Menu(QtWidgets.QMainWindow):
    
    def __init__(self, parent):
        super(Menu, self).__init__()
        uic.loadUi("menu.ui", self)
        self.parent = parent
        self.setFixedWidth(1200)
        self.setFixedHeight(850)
        self.resepButton.clicked.connect(self.gotoResep)
        self.artikelButton.clicked.connect(self.gotoArtikel)
        
        self.artikelLabel.setFont(fontLoader.load_custom_font('../font/Nunito-ExtraBold.ttf'))
        self.artikelLabel.setStyleSheet("font: 28px;")
        self.resepLabel.setFont(fontLoader.load_custom_font('../font/Nunito-ExtraBold.ttf'))
        self.resepLabel.setStyleSheet("font: 28px;")

        # Navbar
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1201, 111))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_1 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_1.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_1.setObjectName("verticalLayout_1")
        self.Navbar = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.Navbar.setStyleSheet("background-color:rgb(253, 231, 189)")
        self.Navbar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Navbar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Navbar.setObjectName("Navbar")
        self.backButton = QtWidgets.QPushButton(self.Navbar)
        self.backButton.setGeometry(QtCore.QRect(40, 30, 51, 51))
        self.backButton.setStyleSheet("border : None;")
        self.backButton.setText("")
        self.backButton.clicked.connect(self.goBack)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../img/icon/button_back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backButton.setIcon(icon)
        self.backButton.setIconSize(QtCore.QSize(50, 70))
        self.backButton.setObjectName("backButton")
        self.homeButton = QtWidgets.QPushButton(self.Navbar)
        self.homeButton.setGeometry(QtCore.QRect(460, 0, 231, 101))
        self.homeButton.setStyleSheet("border : None;")
        self.homeButton.setText("")
        self.homeButton.clicked.connect(self.goHome)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../img/icon/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.homeButton.setIcon(icon1)
        self.homeButton.setIconSize(QtCore.QSize(190, 80))
        self.homeButton.setObjectName("homeButton")
        self.verticalLayout_1.addWidget(self.Navbar)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.raise_()

    def gotoArtikel(self):
        self.parent.pages.setCurrentWidget(self.parent.DaftarArtikel)

    def gotoResep(self):
        self.parent.DaftarResep.clearGrid()
        self.parent.DaftarResep.readDatabase()
        self.parent.pages.setCurrentWidget(self.parent.DaftarResep)
    
    def goBack(self):
        self.parent.pages.setCurrentWidget(self.parent.WelcomePage)

    def goHome(self):
        self.goBack()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    menu = Menu(Menu)
    menu.show()
    sys.exit(app.exec_())