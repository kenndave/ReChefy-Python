from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QSize, Qt
from PyQt5 import uic, QtWidgets, QtGui, QtCore
import sys
from database import databaseFunc
import fontLoader

class DaftarArtikel(QtWidgets.QMainWindow):
    def __init__(self, parent):
        super(DaftarArtikel, self).__init__()
        uic.loadUi(r".\daftarArtikel.ui", self)
        self.parent = parent
        # load database
        file = r".\database\rechefy.db"
        connection = databaseFunc.connectToDatabase(file)
        databaseFunc.initializeTable(connection)
        
        # load header and back button
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../img/icon/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.homeButton.setIcon(icon1)
        self.homeButton.setIconSize(QtCore.QSize(190, 80))
        self.homeButton.setObjectName("homeButton")
        self.homeButton.clicked.connect(self.goHome)
        self.verticalLayout_1.addWidget(self.Navbar)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.raise_()
        
        # load title "Daftar Artikel" label
        self.titleLabel = QtWidgets.QLabel(self)
        self.titleLabel.setGeometry(70,108,320,70)
        self.titleLabel.setText("Daftar Artikel")
        self.titleLabel.setFont(fontLoader.load_custom_font('../font/Nunito-Black.ttf'))
        self.titleLabel.setStyleSheet("font: 28pt;background-color:none;")
        
        self.scrollArtikel = QtWidgets.QWidget()    
        self.layoutScroll = QtWidgets.QVBoxLayout()    
        self.scrollArea.setWidget(self.scrollArtikel)
        self.scrollArea.verticalScrollBar().setStyleSheet("QScrollBar:vertical {background-color: #FDE7BD; border: none; border-radius: 15px; width: 8px; margin: 0px 0px 0px 0px;}\
                                                        QScrollBar::handle:vertical {background-color: #EE9C20;border-radius: 15px; min-height: 20px;}\
                                                        QScrollBar::add-line:vertical {border: none; background: none;}\
                                                        QScrollBar::sub-line:vertical {border: none; background: none;}")
        
        # load daftar artikel
        dataArtikel = databaseFunc.getDaftarArtikel(connection)
        self.counter = 0
        self.loadArtikel(connection, dataArtikel)
    
    def loadArtikel(self, connection, dataArtikel):
        # load all artikel
        for idx in range (len(dataArtikel)):
            self.createArtikel(connection, dataArtikel[idx])
    
    def createArtikel(self, connection, artikel):
        # create each artikel
        artikelLayout = QtWidgets.QHBoxLayout()
        artikelWidget = QtWidgets.QWidget()
        artikelWidget.setFixedSize(1000,260)
        artikelWidget.setStyleSheet("background-color: #FDE7BD;border-radius: 15px;")
        
        horizontalBox = QtWidgets.QHBoxLayout()
        
        image_artikel = QtWidgets.QLabel()
        image_artikel.setFixedSize(470,230)
        gambar = databaseFunc.artikelBlobToImage(connection, artikel[0])
        pixmap = QPixmap(gambar)
        pixmap = pixmap.scaled(image_artikel.width(), image_artikel.height()) # scale the pixmap to the size of the label
        image_artikel.setPixmap(pixmap)
        image_artikel.setPixmap(QPixmap(gambar))
        image_artikel.setScaledContents(True)
        image_artikel.setStyleSheet("background-color: #EE9C20;border-radius: 15px;")
        image_artikel.mousePressEvent = lambda event, id=artikel[0]: self.tampilanArtikel(id)
        horizontalBox.addWidget(image_artikel)
        
        verticalWidget = QtWidgets.QWidget()
        verticalBox = QtWidgets.QVBoxLayout()
        label_judul = QtWidgets.QLabel(artikel[2])
        label_judul.setFixedWidth(470)
        label_judul.setAlignment(Qt.AlignTop)
        self.writeLabelLimited(label_judul)
        label_judul.setWordWrap(True)
        label_judul.setFont(fontLoader.load_custom_font('../font/Nunito-ExtraBold.ttf'))
        label_judul.setStyleSheet("font: 16pt;")
        verticalBox.addWidget(label_judul)
        
        label_tanggal = QtWidgets.QLabel()
        label_tanggal.setText(artikel[4])
        label_tanggal.setFont(fontLoader.load_custom_font('../font/Nunito-Light.ttf'))
        label_tanggal.setStyleSheet("font: 8pt;")
        verticalBox.addWidget(label_tanggal)
        
        label_preview = QtWidgets.QLabel(artikel[3])
        self.writeLabelLimited(label_preview)
        label_preview.setMaximumWidth(400)
        label_preview.setWordWrap(True)
        label_preview.setFont(fontLoader.load_custom_font('../font/Nunito-Regular.ttf'))
        label_preview.setStyleSheet("font: 11pt;")
        verticalBox.addWidget(label_preview)
        verticalWidget.setLayout(verticalBox)
        
        horizontalBox.addWidget(verticalWidget)
        artikelWidget.setLayout(horizontalBox)
        artikelLayout.addWidget(artikelWidget)
        
        self.layoutScroll.insertLayout(self.counter, artikelLayout)
        self.scrollArtikel.setLayout(self.layoutScroll)
        self.counter += 1
    
    def writeLabelLimited(self, label):
        text = label.text()
        elided_text = label.fontMetrics().elidedText(text, Qt.ElideRight, label.width())
        label.setText(elided_text)
    
    def goBack(self):
        self.parent.pages.setCurrentWidget(self.parent.Menu)
    
    def goHome(self):
        self.parent.pages.setCurrentWidget(self.parent.WelcomePage)

    def tampilanArtikel(self, id):
        self.parent.LihatArtikel.idArtikel = id
        self.parent.LihatArtikel.readDatabase()
        self.parent.pages.setCurrentWidget(self.parent.LihatArtikel)
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    DaftarArtikel = DaftarArtikel()
    DaftarArtikel.show()
    sys.exit(app.exec_())