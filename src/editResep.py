from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QSize, Qt
from PyQt5 import uic, QtWidgets, QtCore, QtGui
from database import databaseFunc
import sys
import os
import fontLoader

class FormEditResep(QtWidgets.QMainWindow):
    def __init__(self, parent):
        # Konstruksi GUI
        super(FormEditResep, self).__init__()
        uic.loadUi("editResep.ui", self)
        self.parent = parent
        self.idResep = 1
        self.setFixedHeight(850)
        self.setFixedWidth(1200)
        self.inputGambar_resep.setIconSize(QSize(113, 98))
        self.inputGambar_resep.setStyleSheet("QPushButton{background-color: #EEC120; border: none;}")
        self.inputGambar_resep.clicked.connect(self.selectPicture)
        self.saveButton_resep.clicked.connect(self.inputValidation)

        self.inputJudul_resep.setFont(fontLoader.load_custom_font('../font/Nunito-ExtraBold.ttf'))
        self.inputJudul_resep.setStyleSheet("QTextEdit {font: 40px; background-color: #F7EAD3; border-radius: 29px; padding: 10px; text-align: center;}")
        self.inputDeskripsi_resep.setFont(fontLoader.load_custom_font('../font/Nunito-Medium.ttf'))
        self.inputDeskripsi_resep.setStyleSheet("QTextEdit {font: 16px; background-color: #F7EAD3; border-radius: 29px; padding: 10px; text-align: center;}")
        self.bahan_label.setFont(fontLoader.load_custom_font('../font/Nunito-ExtraBold.ttf'))
        self.bahan_label.setStyleSheet("font: 20px;")
        self.alat_label.setFont(fontLoader.load_custom_font('../font/Nunito-ExtraBold.ttf'))
        self.alat_label.setStyleSheet("font: 20px;")
        self.langkahMemasakLabel.setFont(fontLoader.load_custom_font('../font/Nunito-ExtraBold.ttf'))
        self.langkahMemasakLabel.setStyleSheet("font: 20px;")
        self.inputLangkahMemasak_resep.setFont(fontLoader.load_custom_font('../font/Nunito-Medium.ttf'))
        self.inputLangkahMemasak_resep.setStyleSheet("QTextEdit {font: 16px; background-color: #F7EAD3; border-radius: 29px; padding: 10px; text-align: center;}")
        
        self.addAlat_button.setFixedSize(30, 30)
        self.addBahan_button.setFixedSize(30, 30)
        self.addAlat_button.setIcon(QIcon(QPixmap("../img/icon/addIcon.png")))
        self.addBahan_button.setIcon(QIcon(QPixmap("../img/icon/addIcon.png")))
        self.addAlat_button.setStyleSheet("background-color: #F75008; border-radius: 15px")
        self.addBahan_button.setStyleSheet("background-color: #F75008; border-radius: 15px")
        self.scrollWidgetAlat = QtWidgets.QWidget()
        self.scrollWidgetBahan = QtWidgets.QWidget()

        self.scrollAlat.setWidget(self.scrollWidgetAlat)
        self.scrollAlat.verticalScrollBar().setStyleSheet("QScrollBar:vertical {background-color: #FDE7BD; border: none; border-radius: 15px; width: 8px; margin: 0px 0px 0px 0px;}\
                                                QScrollBar::handle:vertical {background-color: #EE9C20;border-radius: 15px; min-height: 20px;}\
                                                QScrollBar::add-line:vertical {border: none; background: none;}\
                                                QScrollBar::sub-line:vertical {border: none; background: none;}")
        self.scrollBahan.setWidget(self.scrollWidgetBahan)
        self.scrollBahan.verticalScrollBar().setStyleSheet("QScrollBar:vertical {background-color: #FDE7BD; border: none; border-radius: 15px; width: 8px; margin: 0px 0px 0px 0px;}\
                                                QScrollBar::handle:vertical {background-color: #EE9C20;border-radius: 15px; min-height: 20px;}\
                                                QScrollBar::add-line:vertical {border: none; background: none;}\
                                                QScrollBar::sub-line:vertical {border: none; background: none;}")
        self.scrollAlat.setStyleSheet("QScrollBar:vertical { width: 15px; }")
        self.scrollBahan.setStyleSheet("QScrollBar:vertical { width: 15px; }")
        
        # Inisialisasi data input dari database
        self.file = r".\database\rechefy.db"
        self.connection = databaseFunc.connectToDatabase(self.file)
        self.allAlat = databaseFunc.getAlat(self.connection)
        self.allBahan = databaseFunc.getBahan(self.connection)
        self.satuanBahan = databaseFunc.getSatuanKuantitasBahan(self.connection)
        self.addAlat_button.clicked.connect(lambda: self.addAlat(self.allAlat[0][1]))
        self.addBahan_button.clicked.connect(lambda: self.addBahan(self.allBahan[0][1], 0.1, self.satuanBahan[0][0]))

        # Inisialisasi penyimpanan masukan user
        self.verticalAlat = QtWidgets.QVBoxLayout()
        self.verticalBahan = QtWidgets.QVBoxLayout()
        self.verticalBahan.setSpacing(3)
        self.listAlat = []
        self.listBahan = []
        self.listLayoutAlat = []
        self.listLayoutBahan = []
        self.counterAlat = 1
        self.counterBahan = 1
        self.amountAlat = 0
        self.amountBahan = 0


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

    def readResep(self):
        ## Membaca data resep yang ingin disunting pada database
        self.file = r".\database\rechefy.db"
        self.connection = databaseFunc.connectToDatabase(self.file)
        self.dataResep = databaseFunc.getResep(self.connection, self.idResep)
        nama = self.dataResep[0][2]
        deskripsi = self.dataResep[0][3]
        langkah = self.dataResep[0][4]
        self.inputJudul_resep.setText(nama)
        self.inputDeskripsi_resep.setText(deskripsi)
        self.inputLangkahMemasak_resep.setText(langkah)
        self.filePath = databaseFunc.resepBlobToImage(self.connection, self.idResep)
        self.fotoPath = databaseFunc.resepBlobToImage(self.connection, self.idResep)
        self.inputGambar_resep.setIcon(QIcon(QPixmap(self.filePath)))
        self.inputGambar_resep.setIconSize(QSize(self.inputGambar_resep.width(), self.inputGambar_resep.height()))
        self.inputGambar_resep.setStyleSheet("QPushButton{background-color: #FFF6E5; border: none;}")

        y = databaseFunc.getAlatResep(self.connection, self.idResep)
        z = databaseFunc.getBahanResep(self.connection, self.idResep)
        for i in y:
            self.addAlat(i[1])
        for i in z:
            self.addBahan(i[1], i[2], i[3])



    def addAlat(self, opsi):
        # Penambahan alat dari templat sunting resep baik dari database maupun tambahan dari user
        horizontal_layout = QtWidgets.QHBoxLayout()
        horizontal_layout.setObjectName("Alat_"+str(self.counterAlat))

        dropdown = QtWidgets.QComboBox()
        for i in self.allAlat:
            dropdown.addItem(i[1])
        dropdown.setCurrentIndex(dropdown.findText(opsi))
        dropdown.view().setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        dropdown.setObjectName("DropdownAlat_"+str(self.counterAlat))
        dropdown.setFixedSize(125, 30)
        dropdown.setFont(fontLoader.load_custom_font('../font/Nunito-Medium.ttf'))
        dropdown.setStyleSheet("QComboBox{background-color: #F7EAD3; border: none; border-radius: 10px;} QComboBox::down-arrow {image: url(../img/icon/down_arrow.png); height: 30px;} ")
        horizontal_layout.addWidget(dropdown)

        delete = QtWidgets.QPushButton()
        delete.setFixedSize(30, 30)
        delete.setIcon(QIcon(QPixmap("../img/icon/deleteIcon.png")))
        delete.setStyleSheet("background-color: #F75008; border-radius: 15px;")
        delete.setObjectName("DeleteAlat_"+str(self.counterAlat))
        horizontal_layout.addWidget(delete)
        horizontal_layout.id = self.counterAlat

        self.listLayoutAlat.append(horizontal_layout)
        self.listAlat.append(self.counterAlat)
        delete.clicked.connect(lambda _, layout=horizontal_layout: self.deleteAlat(layout))
        self.verticalAlat.insertLayout(self.amountAlat, horizontal_layout)
        self.scrollWidgetAlat.setLayout(self.verticalAlat)
        self.counterAlat += 1
        self.amountAlat += 1
        
    
    def addBahan(self, opsi, jumlah, satuan):
        # Penambahan bahan pada templat sunting resep baik dari database maupun tambahan user
        horizontal_layout = QtWidgets.QHBoxLayout()

        amount = QtWidgets.QDoubleSpinBox()
        amount.setObjectName("Jumlah_"+str(self.counterBahan))
        amount.setRange(0.1, 100000.0)
        amount.setValue(jumlah)
        amount.setFixedSize(45, 30)
        amount.setFont(fontLoader.load_custom_font('../font/Nunito-Medium.ttf'))
        amount.setStyleSheet("QSpinBox{background-color: #F7EAD3; border-radius: 10px;}QSpinBox::up-button{image: url(../img/icon/up_arrow.png); width: 7px;} QSpinBox::down-button{image: url(../img//icon/down_arrow.png); width: 7px;}")
        horizontal_layout.addWidget(amount)

        unit = QtWidgets.QComboBox()
        for i in self.satuanBahan:
            unit.addItem(i[0])
        unit.setObjectName("Satuan_"+str(self.counterBahan))
        unit.setCurrentIndex(unit.findText(satuan))
        unit.setFixedSize(72, 30)
        unit.setFont(fontLoader.load_custom_font('../font/Nunito-Medium.ttf'))
        unit.setStyleSheet("QComboBox{background-color: #F7EAD3; border: none; border-radius: 10px;} QComboBox::down-arrow {image: url(../img/icon/down_arrow.png); height: 5px; width: 5px}")
        horizontal_layout.addWidget(unit)

        dropdown = QtWidgets.QComboBox()
        for i in self.allBahan:
            dropdown.addItem(i[1])
        dropdown.setCurrentIndex(dropdown.findText(opsi))
        dropdown.setObjectName("DropdownBahan_"+str(self.counterBahan))
        dropdown.setFixedSize(125, 30)
        dropdown.setFont(fontLoader.load_custom_font('../font/Nunito-Medium.ttf'))
        dropdown.setStyleSheet("QComboBox{background-color: #F7EAD3; border: none; border-radius: 10px;} QComboBox::down-arrow {image: url(../img/icon/down_arrow.png); height: 30px;}")
        dropdown.view().setStyleSheet("QScrollBar:vertical {background-color: #FDE7BD; border: none; border-radius: 15px; width: 8px; margin: 0px 0px 0px 0px;}\
                                                QScrollBar::handle:vertical {background-color: #EE9C20;border-radius: 15px; min-height: 20px;}\
                                                QScrollBar::add-line:vertical {border: none; background: none;}\
                                                QScrollBar::sub-line:vertical {border: none; background: none;}")
        horizontal_layout.addWidget(dropdown)

        delete = QtWidgets.QPushButton()
        delete.setFixedSize(30, 30)
        delete.setIcon(QIcon(QPixmap("../img/icon/deleteIcon.png")))
        delete.setStyleSheet("background-color: #F75008; border-radius: 15px;")
        delete.setObjectName("DeleteBahan_"+str(self.counterBahan))
        horizontal_layout.addWidget(delete)
        horizontal_layout.id = self.counterBahan
        self.listBahan.append(self.counterBahan)
        self.listLayoutBahan.append(horizontal_layout)
        delete.clicked.connect(lambda _, layout=horizontal_layout: self.deleteBahan(layout))
        self.verticalBahan.insertLayout(self.amountBahan, horizontal_layout)
        self.scrollWidgetBahan.setLayout(self.verticalBahan)
        self.counterBahan += 1
        self.amountBahan += 1


    def selectPicture(self):
        # Fungsi menerima input gambar masakan
        self.filePath, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Image Files (*.png *.jpg *.bmp)")
        if self.filePath:
            self.inputGambar_resep.setIcon(QIcon(QPixmap(self.filePath)))
            self.inputGambar_resep.setIconSize(QSize(self.inputGambar_resep.width(), self.inputGambar_resep.height()))
            self.inputGambar_resep.setStyleSheet("QPushButton{background-color: #FFF6E5; border: none;}")
        else:
            self.inputGambar_resep.setIcon(QIcon(QPixmap("../img/icon/pilihFoto.png")))
            self.inputGambar_resep.setIconSize(QSize(113, 98))
            self.inputGambar_resep.setStyleSheet("QPushButton{background-color: #EEC120; border: none;}")

    def deleteAlat(self, layout):
        # Menghapus satu pilihan alat pada GUI
        layout_item = self.verticalAlat.itemAt(self.verticalAlat.indexOf(layout))
        self.listLayoutAlat.remove(layout)
        self.listAlat.remove(layout.id)
        self.verticalAlat.removeItem(layout_item)

        while layout.count():
            child_item = layout.takeAt(0)

            if child_item.widget():
                child_item.widget().deleteLater()

        self.scrollWidgetAlat.setLayout(self.verticalAlat)

        del layout
        self.amountAlat -= 1

    def deleteBahan(self, layout):
        # Menghapus satu bahan pada GUI, termasuk kuantitas, satuan, dan pilihan bahannya.
        layout_item = self.verticalBahan.itemAt(self.verticalBahan.indexOf(layout))
        self.verticalBahan.removeItem(layout_item)
        self.listBahan.remove(layout.id)
        while layout.count():
            child_item = layout.takeAt(0)

            if child_item.widget():
                child_item.widget().deleteLater()

        self.scrollWidgetBahan.setLayout(self.verticalBahan)
        self.listLayoutBahan.remove(layout)
        del layout
        self.amountBahan -= 1
    
    def clearAlat(self):
        for i in range(len(self.listLayoutAlat)):
            self.deleteAlat(self.listLayoutAlat[0])
        self.listLayoutAlat.clear()
        self.listAlat.clear()
    def clearBahan(self):
        for i in range(len(self.listLayoutBahan)):
            self.deleteBahan(self.listLayoutBahan[0])
        self.listLayoutBahan.clear()
        self.listBahan.clear()

    def clear(self):
        # Mengosongkan templat sebelum mengakses halaman lain
        self.clearAlat()
        self.clearBahan()
        self.inputJudul_resep.clear()
        self.inputDeskripsi_resep.clear()
        self.inputLangkahMemasak_resep.clear()
        self.inputGambar_resep.setIcon(QIcon(QPixmap("../img/icon/pilihFoto.png")))
        self.inputGambar_resep.setIconSize(QSize(113, 98))
        self.inputGambar_resep.setStyleSheet("QPushButton{background-color: #EEC120; border-radius: 25px;}")

    def alatValidation(self):
        alat = set()
        for count in self.listAlat:
            nama = self.findChild(QComboBox, f'DropdownAlat_{count}').currentText()
            if nama in alat: return False
            alat.add(nama)
        return True
    
    def bahanValidation(self):
        bahan = set()
        for count in self.listBahan:
            nama = self.findChild(QComboBox, f'DropdownBahan_{count}').currentText()
            if nama in bahan: return False
            bahan.add(nama)
        return True

    def inputValidation(self):
        # Validasi input, dilakukan pemunculan popup apabila tidak sesuai
        if self.inputJudul_resep.toPlainText() == "" or self.inputDeskripsi_resep.toPlainText() == "" or self.filePath == "" or self.inputLangkahMemasak_resep.toPlainText() == "" or len(self.listAlat) == 0 or len(self.listBahan) == 0 or not self.alatValidation() or not self.bahanValidation():
            self.parent.WarningValidasi.warningClass.warningLabel.setText("")
            print(str(self.parent.WarningValidasi.warningClass.warningLabel.text()))
            self.isiText = []
            self.isiTextSama = []
            if self.inputJudul_resep.toPlainText() == "":
                print("Judul masakan masih kosong")
                self.isiText.append("judul")
            if (self.inputDeskripsi_resep.toPlainText() == ""):
                print("Deskripsi masakan masih kosong")
                self.isiText.append("deskripsi")
            if self.filePath == "":
                print("Gambar masakan belum ada")
                self.isiText.append("gambar")
            if self.inputLangkahMemasak_resep.toPlainText() == "":
                print("Langkah memasak masakan masih kosong")
                self.isiText.append("langkah memasak")
            if len(self.listAlat) == 0:
                print("Alat masih kosong")
                self.isiText.append("alat")
            if len(self.listBahan) == 0:
                print("Bahan masih kosong")
                self.isiText.append("bahan")
            if not self.alatValidation():
                print("Terdapat alat yang sama")
                self.isiTextSama.append("alat")
            if not self.bahanValidation():
                print("Terdapat bahan yang sama")
                self.isiTextSama.append("bahan")
            if len(self.isiText):
                for i in range(len(self.isiText)):
                    if i > 0 and i < len(self.isiText):
                        self.parent.WarningValidasi.warningClass.warningLabel.setText(str(self.parent.WarningValidasi.warningClass.warningLabel.text()) + ", ")
                    self.parent.WarningValidasi.warningClass.warningLabel.setText(str(self.parent.WarningValidasi.warningClass.warningLabel.text()) + self.isiText[i])
                self.parent.WarningValidasi.warningClass.warningLabel.setText(str(self.parent.WarningValidasi.warningClass.warningLabel.text()) + " masih kosong\n")
            if len(self.isiTextSama):
                self.parent.WarningValidasi.warningClass.warningLabel.setText(str(self.parent.WarningValidasi.warningClass.warningLabel.text()) + "Terdapat ")
                for i in range(len(self.isiTextSama)):
                    if i > 0 and i < len(self.isiText)-1:
                        self.parent.WarningValidasi.warningClass.warningLabel.setText(str(self.parent.WarningValidasi.warningClass.warningLabel.text()) + ", ")
                    self.parent.WarningValidasi.warningClass.warningLabel.setText(str(self.parent.WarningValidasi.warningClass.warningLabel.text()) + self.isiTextSama[i])
                self.parent.WarningValidasi.warningClass.warningLabel.setText(str(self.parent.WarningValidasi.warningClass.warningLabel.text()) + " yang sama")

            self.parent.popup.setCurrentWidget(self.parent.WarningValidasi)
            if self.parent.WarningValidasi.Exec() != QDialog.Accepted:
                self.parent.WarningValidasi.warningClass.warningLabel.setText("")
            self.parent.WarningValidasi.warningClass.warningLabel.setText("")
        else:
            self.parent.WarningValidasi.warningClass.warningLabel.setText("Berhasil disunting")
            self.parent.popup.setCurrentWidget(self.parent.WarningValidasi)
            if self.parent.WarningValidasi.Exec() != QDialog.Accepted:
                self.parent.WarningValidasi.warningClass.warningLabel.setText("")
            self.parent.WarningValidasi.warningClass.warningLabel.setText("")
            self.editResep()
        # penambahan warning
    def editResep(self):
        # Jika tervalidasi, lakukan add resep.
        databaseFunc.editResep(self.connection, self.idResep, databaseFunc.imageToBlob(self.filePath), self.inputJudul_resep.toPlainText(), self.inputDeskripsi_resep.toPlainText(), self.inputLangkahMemasak_resep.toPlainText())
        databaseFunc.deleteAlatResep(self.connection, self.idResep)
        databaseFunc.deleteBahanResep(self.connection, self.idResep)
        fotoMasakanPath = self.fotoPath
        if os.path.exists(fotoMasakanPath) :
            os.remove(fotoMasakanPath)
        for count in self.listAlat:
            alat = self.findChild(QComboBox, f'DropdownAlat_{count}')
            idAlat = databaseFunc.getIdAlat(self.connection, alat.currentText())
            databaseFunc.addAlatResep(self.connection, self.idResep, idAlat)
        
        for count in self.listBahan:
            bahan = self.findChild(QComboBox, f'DropdownBahan_{count}')
            jumlahBahan = self.findChild(QDoubleSpinBox, f'Jumlah_{count}')
            satuanBahan = self.findChild(QComboBox, f'Satuan_{count}')
            idBahan = databaseFunc.getIdBahan(self.connection, bahan.currentText())
            databaseFunc.addBahanResep(self.connection, self.idResep, idBahan, jumlahBahan.value(), satuanBahan.currentText())

        self.parent.LihatResep.resetKomentar()
        self.parent.LihatResep.readDatabase()
        self.clear()
        self.parent.pages.setCurrentWidget(self.parent.LihatResep)
        self.parent.LihatResep.notifEditResep()

    def goBack(self):
        # Kembali ke tampilan resep
        self.parent.popup.setCurrentWidget(self.parent.WarningBack)
        if self.parent.WarningBack.Exec() == QDialog.Accepted:
              self.clear()
              self.parent.LihatResep.idResep = self.idResep
              self.parent.LihatResep.resetKomentar()
              self.parent.LihatResep.readDatabase()
              self.parent.pages.setCurrentWidget(self.parent.LihatResep)
    
    def goHome(self):
        # Kembali pada welcome page
        self.parent.popup.setCurrentWidget(self.parent.WarningBack)
        if self.parent.WarningBack.Exec() == QDialog.Accepted:
              self.clear()
              self.parent.pages.setCurrentWidget(self.parent.WelcomePage)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = FormEditResep(FormEditResep)
    MainWindow.readResep()
    MainWindow.show()
    sys.exit(app.exec_())
