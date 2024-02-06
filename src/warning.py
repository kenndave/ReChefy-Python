from PyQt5.QtWidgets import *
from PyQt5 import uic
import fontLoader

class Warning(QDialog):
    def __init__(self, parent):
        super().__init__()
        # Set up the UI
        self.parent = parent
        self.layout = QVBoxLayout()
        uic.loadUi("warning.ui", self)

        self.setLayout(self.layout)
        self.deleteButton.clicked.connect(self.accept)
        self.cancelButton.clicked.connect(self.reject)
    
    def komentarDelete(self) :
        self.warningClass = Warning(self.parent)
        self.warningClass.setWindowTitle("Warning")
        self.warningClass.deleteButton.setText("Hapus")
        self.warningClass.deleteButton.setFont(fontLoader.load_custom_font('../font/Nunito-Medium.ttf'))
        self.warningClass.deleteButton.setStyleSheet("font: 16pt; background-color: #F75008; border-radius: 0px; color: #FFF6E5;")
        self.warningClass.cancelButton.setText("Batalkan")
        self.warningClass.cancelButton.setFont(fontLoader.load_custom_font('../font/Nunito-Medium.ttf'))
        self.warningClass.cancelButton.setStyleSheet("font: 16pt; background-color: #E5BB28; border-radius: 0px; color: #FFF6E5;")
        self.warningClass.warningLabel.setText("Apakah Anda yakin ingin \n menghapus komentar?")
        self.warningClass.warningLabel.setFont(fontLoader.load_custom_font('../font/Nunito-Medium.ttf'))
        self.warningClass.warningLabel.setStyleSheet("background-color: #F7EAD3; font: 18pt;")

    def resepDelete(self) :
        self.warningClass = Warning(self.parent)
        self.warningClass.setWindowTitle("Warning")
        self.warningClass.deleteButton.setText("Hapus")
        self.warningClass.deleteButton.setFont(fontLoader.load_custom_font('../font/Nunito-Medium.ttf'))
        self.warningClass.deleteButton.setStyleSheet("font: 16pt; background-color: #F75008; border-radius: 0px; color: #FFF6E5;")
        self.warningClass.cancelButton.setText("Batalkan")
        self.warningClass.cancelButton.setFont(fontLoader.load_custom_font('../font/Nunito-Medium.ttf'))
        self.warningClass.cancelButton.setStyleSheet("font: 16pt; background-color: #E5BB28; border-radius: 0px; color: #FFF6E5;")
        self.warningClass.warningLabel.setText("Apakah Anda yakin ingin \n menghapus resep?")
        self.warningClass.warningLabel.setFont(fontLoader.load_custom_font('../font/Nunito-Medium.ttf'))
        self.warningClass.warningLabel.setStyleSheet("background-color: #F7EAD3; font: 18pt;")
    
    def Back(self) :
        self.warningClass = Warning(self.parent)
        self.warningClass.setWindowTitle("Warning")
        self.warningClass.deleteButton.setText("Kembali")
        self.warningClass.deleteButton.setFont(fontLoader.load_custom_font('../font/Nunito-Medium.ttf'))
        self.warningClass.deleteButton.setStyleSheet("font: 16pt; background-color: #F75008; border-radius: 0px; color: #FFF6E5;")
        self.warningClass.cancelButton.setText("Batalkan")
        self.warningClass.cancelButton.setFont(fontLoader.load_custom_font('../font/Nunito-Medium.ttf'))
        self.warningClass.cancelButton.setStyleSheet("font: 16pt; background-color: #E5BB28; border-radius: 0px; color: #FFF6E5;")
        self.warningClass.warningLabel.setText("Apakah Anda yakin \ningin kembali?")
        self.warningClass.warningLabel.setFont(fontLoader.load_custom_font('../font/Nunito-Medium.ttf'))
        self.warningClass.warningLabel.setStyleSheet("font: 18pt; background-color: #F7EAD3;")
    
    def Validasi(self):
        self.warningClass = Warning(self.parent)
        self.warningClass.setWindowTitle("Warning")
        self.warningClass.warningLabel.setFont(fontLoader.load_custom_font('../font/Nunito-Medium.ttf'))
        self.warningClass.warningLabel.setStyleSheet("font: 14pt; background-color: #F7EAD3;")
        self.warningClass.warningLabel.setWordWrap(True)
        self.warningClass.deleteButton.deleteLater()
        self.warningClass.cancelButton.setText("Ok")
        self.warningClass.cancelButton.setFont(fontLoader.load_custom_font('../font/Nunito-Medium.ttf'))
        self.warningClass.cancelButton.setStyleSheet("font: 16pt; background-color: #F75008; border-radius: 0px; color: #FFF6E5;")
    def Exec(self):
        return self.warningClass.exec_()

if __name__ == '__main__':
    app = QApplication([])
    warning = Warning(Warning)
    warning.Back()
    warning.exec_()
