import os
from database import databaseFunc
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtWidgets, QtCore, QtGui
from functools import partial
from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtCore import Qt
import fontLoader

class LihatResep(QMainWindow) :
    def __init__(self, parent) :
        super(LihatResep, self).__init__()
        uic.loadUi("lihatResep.ui", self)

        #initialize variables
        self.idResep = 1
        self.parent = parent
        self.listKomentar = []
        self.listKomentarDeleteAll = []

        #custom scrollbar
        self.scrollArea.verticalScrollBar().setStyleSheet("QScrollBar:vertical {background-color: #FDE7BD; border: none; border-radius: 15px; width: 8px; margin: 0px 0px 0px 0px;}\
                QScrollBar::handle:vertical {background-color: #EE9C20;border-radius: 15px; min-height: 20px;}\
                QScrollBar::add-line:vertical {border: none; background: none;}\
                QScrollBar::sub-line:vertical {border: none; background: none;}")
        self.scrollArea_2.verticalScrollBar().setStyleSheet("QScrollBar:vertical {background-color: #FDE7BD; border: none; border-radius: 15px; width: 8px; margin: 0px 0px 0px 0px;}\
                QScrollBar::handle:vertical {background-color: #EE9C20;border-radius: 15px; min-height: 20px;}\
                QScrollBar::add-line:vertical {border: none; background: none;}\
                QScrollBar::sub-line:vertical {border: none; background: none;}")
        self.scrollArea_3.verticalScrollBar().setStyleSheet("QScrollBar:vertical {background-color: #FDE7BD; border: none; border-radius: 15px; width: 8px; margin: 0px 0px 0px 0px;}\
                QScrollBar::handle:vertical {background-color: #EE9C20;border-radius: 15px; min-height: 20px;}\
                QScrollBar::add-line:vertical {border: none; background: none;}\
                QScrollBar::sub-line:vertical {border: none; background: none;}")
        self.scrollArea_4.verticalScrollBar().setStyleSheet("QScrollBar:vertical {background-color: #FDE7BD; border: none; border-radius: 15px; width: 8px; margin: 0px 0px 0px 0px;}\
                QScrollBar::handle:vertical {background-color: #EE9C20;border-radius: 15px; min-height: 20px;}\
                QScrollBar::add-line:vertical {border: none; background: none;}\
                QScrollBar::sub-line:vertical {border: none; background: none;}")
        self.scrollArea_5.verticalScrollBar().setStyleSheet("QScrollBar:vertical {background-color: #FDE7BD; border: none; border-radius: 15px; width: 8px; margin: 0px 0px 0px 0px;}\
                QScrollBar::handle:vertical {background-color: #EE9C20;border-radius: 15px; min-height: 20px;}\
                QScrollBar::add-line:vertical {border: none; background: none;}\
                QScrollBar::sub-line:vertical {border: none; background: none;}")

        #add notifikasi
        self.setStyleSheet("background-color: #FDE7BD;")
        self.notifikasi= QtWidgets.QLabel(self.scrollArea)
        self.notifikasi.setGeometry(QtCore.QRect(350, -5, 471, 31))
        self.notifikasi.setStyleSheet("background-color: rgb(238, 156, 32);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color : rgb(255, 255, 255);\n"
"border: 0px solid #555;\n"
"border-radius: 8px;\n"
"border-style: outset;\n"
"padding : 5px")
        self.notifikasi.setAlignment(QtCore.Qt.AlignCenter)
        self.notifikasi.setObjectName("notifikasi")
        self.notifikasi.hide()

        #initialize variables
        self.path = "../img/icon/noPhoto.jpg"
        self.text = ""
        
        #set font
        self.alat.setFont(fontLoader.load_custom_font('../font/Nunito-ExtraBold.ttf'))
        self.bahan.setFont(fontLoader.load_custom_font('../font/Nunito-ExtraBold.ttf'))
        self.langkahMemasak.setFont(fontLoader.load_custom_font('../font/Nunito-ExtraBold.ttf'))
        self.textEdit.setFont(fontLoader.load_custom_font('../font/Nunito-Regular.ttf'))

        #set button
        self.attachButton.setStyleSheet("border-image: url(../img/icon/attach.png);background-color:none;border: none")
        self.sendButton.clicked.connect(self.addKomentar)
        self.attachButton.clicked.connect(self.addFotoKomentar)
        self.backButton.clicked.connect(self.goBack)
        self.homeButton.clicked.connect(self.goHome)
        
    def readDatabase(self):
        self.file = r".\database\rechefy.db"
        self.connection = databaseFunc.connectToDatabase(self.file)
        self.resep = databaseFunc.getResep(self.connection, self.idResep)
        self.alatResep = databaseFunc.getAlatResep(self.connection, self.idResep)
        self.bahanResep = databaseFunc.getBahanResep(self.connection, self.idResep)
        self.fotoResep = databaseFunc.resepBlobToImage(self.connection, self.idResep)
        self.komentarResep = databaseFunc.getKomentar(self.connection, self.idResep)
        self.lastKomentarID = databaseFunc.getLastIdKomentar(self.connection)
        self.alatResepCombined = self.combineAlat()
        self.bahanResepCombined = self.combineBahan()
        self.defaultResep = self.resep[0][5]
        self.isResepBuatanSendiri()

        self.fotoMasakan.setPixmap(QtGui.QPixmap(self.fotoResep))
        self.namaMasakan.setText(self.resep[0][2])
        self.namaMasakan.setFont(fontLoader.load_custom_font('../font/Nunito-ExtraBold.ttf'))
        self.deskripsi.setText(self.resep[0][3])
        self.deskripsi.setFont(fontLoader.load_custom_font('../font/Nunito-Medium.ttf'))
        self.langkahMemasak_isi.setText(self.resep[0][4])
        self.langkahMemasak_isi.setFont(fontLoader.load_custom_font('../font/Nunito-Medium.ttf'))
        self.bahan_isi.setText(self.bahanResepCombined)
        self.bahan_isi.setFont(fontLoader.load_custom_font('../font/Nunito-Medium.ttf'))
        self.alat_isi.setText(self.alatResepCombined)
        self.alat_isi.setFont(fontLoader.load_custom_font('../font/Nunito-Medium.ttf'))
        self.total = len(self.komentarResep)
        if self.total > 0 :
                self.displayKomentar()
        self.judulKomentar.setText(f"Komentar ({self.total})")
        self.judulKomentar.setFont(fontLoader.load_custom_font('../font/Nunito-ExtraBold.ttf'))
        self.setFixedWidth(1200)
        self.setFixedHeight(850)

        #responsive namaMasakan font size
        nNamaMasakan = len(self.resep[0][2])
        self.namaMasakan.setFont(fontLoader.load_custom_font('../font/Nunito-Black.ttf'))
        if nNamaMasakan > 45 :
              self.namaMasakan.setStyleSheet("font: 8pt;")
        elif nNamaMasakan > 30 :
              self.namaMasakan.setStyleSheet("font: 10pt;")
        elif nNamaMasakan > 20 :
              self.namaMasakan.setStyleSheet("font: 16pt;")

        if self.total == 0 :
                self.komentar.setMinimumSize(QtCore.QSize(1000, 300))

    def isResepBuatanSendiri(self) :
        if int(self.defaultResep) == 1 :

                #add deleteResepButton
                self.deleteResepButton = QtWidgets.QPushButton(self.infoResep)
                self.deleteResepButton.setGeometry(QtCore.QRect(1060, 40, 81, 21))
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.deleteResepButton.sizePolicy().hasHeightForWidth())
                self.deleteResepButton.setSizePolicy(sizePolicy)
                self.deleteResepButton.setText("")
                icon2 = QtGui.QIcon()
                icon2.addPixmap(QtGui.QPixmap("../img/icon/hapus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.deleteResepButton.setIcon(icon2)
                self.deleteResepButton.setIconSize(QtCore.QSize(100, 30))
                self.deleteResepButton.setAutoDefault(False)
                self.deleteResepButton.setObjectName("deleteResepButton")

                #add editResepButton
                self.editResepButton = QtWidgets.QPushButton(self.infoResep)
                self.editResepButton.setGeometry(QtCore.QRect(960, 40, 81, 21))
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.editResepButton.sizePolicy().hasHeightForWidth())
                self.editResepButton.setSizePolicy(sizePolicy)
                self.editResepButton.setText("")
                icon3 = QtGui.QIcon()
                icon3.addPixmap(QtGui.QPixmap("../img/icon/sunting.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.editResepButton.setIcon(icon3)
                self.editResepButton.setIconSize(QtCore.QSize(100, 30))
                self.editResepButton.setAutoDefault(False)
                self.editResepButton.setObjectName("editResepButton")

                #add functional button
                self.deleteResepButton.clicked.connect(self.deleteResep)
                self.editResepButton.clicked.connect(self.editResep)

        elif int(self.defaultResep) == 0:
                self.editResepButton = QtWidgets.QPushButton(self.infoResep)
                self.deleteResepButton = QtWidgets.QPushButton(self.infoResep)
                self.deleteResepButton.setParent(None)
                self.deleteResepButton.deleteLater()
                self.editResepButton.setParent(None)
                self.editResepButton.deleteLater()


    def combineBahan(self) :
        row = len(self.bahanResep)
        column = len(self.bahanResep[0])
        result = ""
        number = 1

        #combine bahan in Resep into string
        for i in range(row) :
                if i != 0 :
                        result += "\n"
                result += f"{number}. "
                for j in range (column) :
                        if j != 0 :
                                if j == 2 :
                                        kuantitas = str(self.bahanResep[i][j])
                                        check = ".0"
                                        if check in kuantitas :
                                                result += str(int(self.bahanResep[i][j]))
                                        else :
                                                result += str(self.bahanResep[i][j])
                                else :
                                        result += str(self.bahanResep[i][j])
                                if j != column-1 :
                                        result += " "
                number +=1
        return result
                  
         
    
    def combineAlat(self) :
        row = len(self.alatResep)
        column = len(self.alatResep[0])
        result = ""
        number = 1

        #combine alat in Resep into string
        for i in range(row) :
                if i != 0 :
                        result += "\n"
                result += f"{number}. "
                for j in range (column) :
                        if j != 0 :
                                result += str(self.alatResep[i][j])
                                if j != column-1 :
                                        result += " "
                number +=1
        return result
         

    def deleteResep(self) :

        #warning popup
        self.parent.popup.setCurrentWidget(self.parent.WarningResep)
        if self.parent.WarningResep.Exec() == QDialog.Accepted:
              
              #delete all komentar in resep
              self.deleteAllKomentar()

              #delete deleteResepButton and editResepButton
              if self.defaultResep == 1 :
                self.deleteResepButton.setParent(None)
                self.deleteResepButton.deleteLater()
                self.editResepButton.setParent(None)
                self.editResepButton.deleteLater()
        
              #delete photo of Resep in directory img/resep
              fotoMasakanPath = self.fotoResep
              if os.path.exists(fotoMasakanPath) :
                    os.remove(fotoMasakanPath)
                
              #delete resep in database  
              databaseFunc.deleteResep(self.connection,self.idResep)

              #reset variables and go to daftarResep page
              self.listKomentar = []
              self.listKomentarDeleteAll = []
              self.parent.DaftarResep.clearGrid()
              self.parent.DaftarResep.readDatabase()
              self.parent.pages.setCurrentWidget(self.parent.DaftarResep)
              self.parent.DaftarResep.notifDeleteResep()

    def notifDeleteKomentar(self) :
        self.notifikasi.setText("Komentar telah dihapus")
        timer = QTimer(self)
        self.notifikasi.show()
        timer.timeout.connect(self.notifikasi.hide)
        timer.start(5000)
          
    def notifAddKomentar(self) :
        self.notifikasi.setText("Komentar telah ditambahkan")
        timer = QTimer(self)
        self.notifikasi.show()
        timer.timeout.connect(self.notifikasi.hide)
        timer.start(5000)

    def notifEditResep(self) :
        self.notifikasi.setText("Resep telah diedit")
        timer = QTimer(self)
        self.notifikasi.show()
        timer.timeout.connect(self.notifikasi.hide)
        timer.start(5000)

    def addFotoKomentar(self) :
        filter = "Image Files (*.jpg; *.jpeg; *.png)"
        filePath, _ = QFileDialog.getOpenFileName(self, filter=filter)
        if filePath:
            self.path = filePath
            self.fileName = os.path.basename(self.path)
            self.pathText.setText(self.fileName)
        else :
             self.path = "../img/icon/noPhoto.jpg"

    def resetKomentar(self) :
        nListKomentar = len(self.listKomentar)
        for i in range (nListKomentar) :
                frame = self.findChild(QFrame, f'komentarFrame_{self.listKomentar[i]}')
                if frame is not None :
                    frame.deleteLater()
        
    def deleteAllKomentar(self) :
        nListKomentarDeleteAll = len(self.listKomentarDeleteAll) 
        self.resetKomentar()
        if nListKomentarDeleteAll > 0 :
                for i in range  (nListKomentarDeleteAll) :
                        self.fotoKomentar = databaseFunc.komentarBlobToImage(self.connection, self.listKomentarDeleteAll[i])
                        fotoKomentarPath = self.fotoKomentar
                        if os.path.exists(fotoKomentarPath) :
                                os.remove(fotoKomentarPath)
                        databaseFunc.deleteKomentar(self.connection, self.listKomentarDeleteAll[i])
                        self.komentarResep = databaseFunc.getKomentar(self.connection, self.idResep)

    def deleteKomentar(self,count):
        
        #warning popup
        self.parent.popup.setCurrentWidget(self.parent.WarningKomentar)
        if self.parent.WarningKomentar.Exec() == QDialog.Accepted:
                fotoKomentarPath = databaseFunc.komentarBlobToImage(self.connection, count)

                #delete photo of komentar in directory img/komentar
                if os.path.exists(fotoKomentarPath) :
                        os.remove(fotoKomentarPath)

                frame = self.findChild(QFrame, f'komentarFrame_{count}')
                if frame is not None :
                        frame.deleteLater()
                        self.total-=1
                        self.judulKomentar.setText(f"Komentar ({self.total})")
                        self.listKomentarDeleteAll.remove(count)
                        databaseFunc.deleteKomentar(self.connection, count)
                        self.komentarResep = databaseFunc.getKomentar(self.connection, self.idResep)
                if self.total == 0 :
                        self.komentar.setMinimumSize(QtCore.QSize(1000, 300))
                self.notifDeleteKomentar()

    def displayKomentar(self):
        self.listKomentar = []
        self.listKomentarDeleteAll = []

        #construct a komentar based on the database
        for i in range (self.total) :
                self.komentar_isi.verticalScrollBar().setStyleSheet("QScrollBar:vertical {background-color: #FDE7BD; border: none; border-radius: 15px; width: 8px; margin: 0px 0px 0px 0px;}\
                        QScrollBar::handle:vertical {background-color: #EE9C20;border-radius: 15px; min-height: 20px;}\
                        QScrollBar::add-line:vertical {border: none; background: none;}\
                        QScrollBar::sub-line:vertical {border: none; background: none;}")
                self.komentarID = int(self.komentarResep[i][0])
                self.komentarTeks = self.komentarResep[i][2]
                self.komentarTanggal = self.komentarResep[i][3]
                self.fotoKomentar = databaseFunc.komentarBlobToImage(self.connection, self.komentarID)

                self.komentar.setMinimumSize(QtCore.QSize(1000, 725))
                self.komentarFrame_0 = QtWidgets.QFrame(self.scrollAreaWidgetContents_8)
                self.komentarFrame_0.setMinimumSize(QtCore.QSize(0, 245))
                self.komentarFrame_0.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.komentarFrame_0.setFrameShadow(QtWidgets.QFrame.Raised)
                self.komentarFrame_0.setObjectName("komentarFrame_" + str(self.komentarID))
                self.tanggalKomentar_0 = QtWidgets.QLabel(self.komentarFrame_0)
                self.tanggalKomentar_0.setGeometry(QtCore.QRect(30, 20, 131, 51))
                self.tanggalKomentar_0.setText(self.komentarTanggal)
                self.tanggalKomentar_0.setFont(fontLoader.load_custom_font('../font/Nunito-Light.ttf'))
                self.tanggalKomentar_0.setStyleSheet("font: 8pt;\n"
        "color: rgb(211, 164, 145);")
                self.tanggalKomentar_0.setScaledContents(False)
                self.tanggalKomentar_0.setWordWrap(False)
                self.tanggalKomentar_0.setObjectName("namaKomentar_" + str(self.komentarID))
                self.isiKomentar_0 = QtWidgets.QTextEdit(self.komentarFrame_0)
                self.isiKomentar_0.setGeometry(QtCore.QRect(0, 70, 661, 181))
                self.isiKomentar_0.setStyleSheet("border: 0px solid #555;\n"
        "border-radius: 8px;\n"
        "border-style: outset;\n"
        "background-color: rgb(253, 231, 189);\n"
        "padding: 10px;")
                self.isiKomentar_0.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
                self.isiKomentar_0.setWordWrapMode(True)
                self.isiKomentar_0.setReadOnly(True)
                self.isiKomentar_0.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
                self.isiKomentar_0.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
                self.isiKomentar_0.setObjectName("isiKomentar_" + str(self.komentarID))
                self.isiKomentar_0.setText(self.komentarTeks)
                self.isiKomentar_0.setFont(fontLoader.load_custom_font('../font/Nunito-Regular.ttf'))
                self.isiKomentar_0.setLineWrapMode(QTextEdit.WidgetWidth)
                self.fotoKomentar_0 = QtWidgets.QLabel(self.komentarFrame_0)
                self.fotoKomentar_0.setGeometry(QtCore.QRect(670, 70, 361, 181))
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.fotoKomentar_0.sizePolicy().hasHeightForWidth())
                self.fotoKomentar_0.setSizePolicy(sizePolicy)
                self.fotoKomentar_0.setStyleSheet("border-radius: 8px;\n"
        "border-style: outset;")
                self.fotoKomentar_0.setText("")
                self.fotoKomentar_0.setPixmap(QtGui.QPixmap(self.fotoKomentar))
                self.fotoKomentar_0.setScaledContents(True)
                self.fotoKomentar_0.setObjectName("fotoKomentar_" + str(self.komentarID))

                self.deleteButton_0 = QtWidgets.QPushButton(self.komentarFrame_0)
                self.deleteButton_0.setGeometry(QtCore.QRect(940, 40, 81, 21))
                self.deleteButton_0.setStyleSheet("border-radius: 8px;\n"
        "border-style: outset;")
                icon2 = QtGui.QIcon()
                icon2.addPixmap(QtGui.QPixmap("../img/icon/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.deleteButton_0.setIcon(icon2)
                self.deleteButton_0.setIconSize(QtCore.QSize(100, 30))
                self.deleteButton_0.setAutoDefault(False)
                self.deleteButton_0.setText("")
                self.deleteButton_0.setObjectName("deleteButton_" + str(self.komentarID) )
                self.deleteButton_0.clicked.connect(partial(self.deleteKomentar, self.komentarID))
                
                self.line_0 = QtWidgets.QFrame(self.komentarFrame_0)
                self.line_0.setGeometry(QtCore.QRect(0, 10, 1057, 16))
                self.line_0.setStyleSheet("border-color: rgb(212, 183, 127);")
                self.line_0.setFrameShape(QtWidgets.QFrame.HLine)
                self.line_0.setFrameShadow(QtWidgets.QFrame.Sunken)
                self.line_0.setObjectName("line_" + str(self.komentarID))
                self.verticalLayout_4.addWidget(self.komentarFrame_0)

                self.listKomentar.append(int(self.komentarResep[i][0]))
                self.listKomentarDeleteAll.append(int(self.komentarResep[i][0]))
              

    def addKomentar(self, event):
        self.text = self.textEdit.toPlainText()
        self.lastKomentarID +=1

        #construct a new komentar based on user input
        if (self.path != "../img/icon/noPhoto.jpg" and self.text == "") or (self.path == "../img/icon/noPhoto.jpg" and self.text != "") or ((self.path != "../img/icon/noPhoto.jpg" and self.text != ""))  :
                self.komentar_isi.verticalScrollBar().setStyleSheet("QScrollBar:vertical {background-color: #FDE7BD; border: none; border-radius: 15px; width: 8px; margin: 0px 0px 0px 0px;}\
                        QScrollBar::handle:vertical {background-color: #EE9C20;border-radius: 15px; min-height: 20px;}\
                        QScrollBar::add-line:vertical {border: none; background: none;}\
                        QScrollBar::sub-line:vertical {border: none; background: none;}")
                self.fotoKomentarBlob = databaseFunc.imageToBlob(self.path)
                self.komentar.setMinimumSize(QtCore.QSize(1000, 725))
                self.komentarFrame_0 = QtWidgets.QFrame(self.scrollAreaWidgetContents_8)
                self.komentarFrame_0.setMinimumSize(QtCore.QSize(0, 245))
                self.komentarFrame_0.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.komentarFrame_0.setFrameShadow(QtWidgets.QFrame.Raised)
                self.komentarFrame_0.setObjectName("komentarFrame_" + str(self.lastKomentarID))
                self.tanggalKomentar_0 = QtWidgets.QLabel(self.komentarFrame_0)
                self.tanggalKomentar_0.setGeometry(QtCore.QRect(30, 20, 131, 51))
                current_datetime = QDateTime.currentDateTime()
                self.tanggalKomentar_0.setText(f"{current_datetime.toString('yyyy-MM-dd hh:mm:ss')}")
                self.tanggalKomentar_0.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
        "color: rgb(211, 164, 145);")
                self.tanggalKomentar_0.setScaledContents(False)
                self.tanggalKomentar_0.setWordWrap(False)
                self.tanggalKomentar_0.setObjectName("namaKomentar_" + str(self.lastKomentarID))
                self.isiKomentar_0 = QtWidgets.QTextEdit(self.komentarFrame_0)
                self.isiKomentar_0.setGeometry(QtCore.QRect(0, 70, 661, 181))
                self.isiKomentar_0.setStyleSheet("border: 0px solid #555;\n"
        "border-radius: 8px;\n"
        "border-style: outset;\n"
        "background-color: rgb(253, 231, 189);\n"
        "padding: 10px;")
                self.isiKomentar_0.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
                self.isiKomentar_0.setWordWrapMode(True)
                self.isiKomentar_0.setReadOnly(True)
                self.isiKomentar_0.setObjectName("isiKomentar_" + str(self.lastKomentarID))
                self.isiKomentar_0.setText(self.text)
                self.fotoKomentar_0 = QtWidgets.QLabel(self.komentarFrame_0)
                self.fotoKomentar_0.setGeometry(QtCore.QRect(670, 70, 361, 181))
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.fotoKomentar_0.sizePolicy().hasHeightForWidth())
                self.fotoKomentar_0.setSizePolicy(sizePolicy)
                self.fotoKomentar_0.setStyleSheet("border-radius: 8px;\n"
        "border-style: outset;")
                self.fotoKomentar_0.setText("")
                self.fotoKomentar_0.setScaledContents(True)
                self.deleteButton_0 = QtWidgets.QPushButton(self.komentarFrame_0)
                self.deleteButton_0.setGeometry(QtCore.QRect(940, 40, 81, 21))
                self.deleteButton_0.setStyleSheet("border-radius: 8px;\n"
        "border-style: outset;")
                icon2 = QtGui.QIcon()
                icon2.addPixmap(QtGui.QPixmap("../img/icon/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.deleteButton_0.setIcon(icon2)
                self.deleteButton_0.setIconSize(QtCore.QSize(100, 30))
                self.deleteButton_0.setAutoDefault(False)
                self.deleteButton_0.setText("")
                self.deleteButton_0.setObjectName("deleteButton_" + str(self.lastKomentarID) )
                self.deleteButton_0.clicked.connect(partial(self.deleteKomentar, self.lastKomentarID))
                
                self.line_0 = QtWidgets.QFrame(self.komentarFrame_0)
                self.line_0.setGeometry(QtCore.QRect(0, 10, 1057, 16))
                self.line_0.setStyleSheet("border-color: rgb(212, 183, 127);")
                self.line_0.setFrameShape(QtWidgets.QFrame.HLine)
                self.line_0.setFrameShadow(QtWidgets.QFrame.Sunken)
                self.line_0.setObjectName("line_" + str(self.lastKomentarID))
                self.verticalLayout_4.addWidget(self.komentarFrame_0)

                databaseFunc.addKomentar(self.connection, self.fotoKomentarBlob, self.text,self.idResep)
                self.komentarResep = databaseFunc.getKomentar(self.connection, self.idResep)
                nKomentarResep = len(self.komentarResep)
                self.lastKomentarID = databaseFunc.getLastIdKomentar(self.connection)
                self.fotoKomentar = databaseFunc.komentarBlobToImage(self.connection, self.lastKomentarID)
                self.fotoKomentar_0.setPixmap(QtGui.QPixmap(self.fotoKomentar))
                self.fotoKomentar_0.setObjectName("fotoKomentar_" + str(self.lastKomentarID))

                self.komentarResep = databaseFunc.getKomentar(self.connection, self.idResep)
                self.listKomentar.append(self.lastKomentarID)
                self.listKomentarDeleteAll.append(self.lastKomentarID)
                self.total +=1
                self.judulKomentar.setText(f"Komentar ({self.total})")
                self.textEdit.setText("")
                self.pathText.setText("")
                self.text = ""
                self.path = "../img/icon/noPhoto.jpg"

                self.notifAddKomentar()

    def editResep(self):

        #reset variables
        if self.defaultResep == 1 :
                self.deleteResepButton.setParent(None)
                self.deleteResepButton.deleteLater()
                self.editResepButton.setParent(None)
                self.editResepButton.deleteLater()
        self.textEdit.setText("")
        self.pathText.setText("")
        self.text = ""
        self.path = "../img/icon/noPhoto.jpg"
        self.parent.LihatResep.resetKomentar()
        self.listKomentar = []
        self.listKomentarDeleteAll = []

        #go to EditResep page
        self.parent.EditResep.idResep = self.idResep
        self.parent.EditResep.clear()
        self.parent.EditResep.readResep()
        self.parent.pages.setCurrentWidget(self.parent.EditResep)

    def goBack(self):

        #reset variables
        self.parent.LihatResep.resetKomentar()
        if self.defaultResep == 1 :
                self.deleteResepButton.setParent(None)
                self.deleteResepButton.deleteLater()
                self.editResepButton.setParent(None)
                self.editResepButton.deleteLater()
        self.textEdit.setText("")
        self.pathText.setText("")
        self.text = ""
        self.path = "../img/icon/noPhoto.jpg"
        self.listKomentar = []
        self.listKomentarDeleteAll = []

        #go to DaftarResep page
        self.parent.DaftarResep.readDatabase()
        self.parent.pages.setCurrentWidget(self.parent.DaftarResep)

    def goHome(self):

        #reset variables
        self.parent.LihatResep.resetKomentar()
        if self.defaultResep == 1 :
                self.deleteResepButton.setParent(None)
                self.deleteResepButton.deleteLater()
                self.editResepButton.setParent(None)
                self.editResepButton.deleteLater()
        self.textEdit.setText("")
        self.pathText.setText("")
        self.text = ""
        self.path = "../img/icon/noPhoto.jpg"
        self.listKomentar = []
        self.listKomentarDeleteAll = []

        #go to WelcomePage
        self.parent.DaftarResep.readDatabase()
        self.parent.pages.setCurrentWidget(self.parent.WelcomePage)

def main() :
    app = QApplication([])
    window = LihatResep()
    app.exec_()



if __name__== '__main__' :
    main ()