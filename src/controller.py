from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtCore
import sys
import menu
import welcomePage
import daftarResep
import daftarArtikel
import lihatResep
import lihatArtikel
import addResep
import editResep
import warning

class Controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.pages = QtWidgets.QStackedWidget()
        self.pages.setFixedHeight(850)
        self.pages.setFixedWidth(1200)
        self.setMinimumSize(QtCore.QSize(1200, 850))
        self.setMaximumSize(QtCore.QSize(1200, 850))
        self.pages.setMaximumSize(QtCore.QSize(1200, 850))
        self.pages.setMinimumSize(QtCore.QSize(1200, 850))
        self.pages.setFixedSize(self.pages.size())
        self.pages.setSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed
        )
        self.setCentralWidget(self.pages)

        self.WelcomePage = welcomePage.WelcomePage(self)
        self.pages.addWidget(self.WelcomePage)
        
        self.Menu = menu.Menu(self)
        self.pages.addWidget(self.Menu)

        self.DaftarArtikel = daftarArtikel.DaftarArtikel(self)
        self.pages.addWidget(self.DaftarArtikel)

        self.DaftarResep = daftarResep.DaftarResep(self)
        self.pages.addWidget(self.DaftarResep)

        self.LihatResep = lihatResep.LihatResep(self)
        self.pages.addWidget(self.LihatResep)

        self.LihatArtikel = lihatArtikel.LihatArtikel(self)
        self.pages.addWidget(self.LihatArtikel)

        self.AddResep = addResep.FormAddResep(self)
        self.pages.addWidget(self.AddResep)

        self.EditResep = editResep.FormEditResep(self)
        self.pages.addWidget(self.EditResep)

        self.popup = QtWidgets.QStackedWidget()
        self.popup.setFixedWidth(515)
        self.popup.setFixedHeight(309)

        self.WarningKomentar = warning.Warning(self)
        self.WarningKomentar.komentarDelete()
        self.popup.addWidget(self.WarningKomentar)

        self.WarningResep = warning.Warning(self)
        self.WarningResep.resepDelete()
        self.popup.addWidget(self.WarningResep)

        self.WarningBack = warning.Warning(self)
        self.WarningBack.Back()
        self.popup.addWidget(self.WarningBack)

        self.WarningValidasi = warning.Warning(self)
        self.WarningValidasi.Validasi()
        self.popup.addWidget(self.WarningValidasi)

        self.pages.setCurrentWidget(self.WelcomePage)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Controller()
    main.show()
    sys.exit(app.exec_())
