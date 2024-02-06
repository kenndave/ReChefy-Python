import unittest
from PyQt5.QtWidgets import QApplication
from lihatArtikel import *
import sys
from unittest.mock import Mock

class testLihatArtikel(unittest.TestCase) :
    def setUp(self):
        self.app = QApplication(sys.argv)
        parent = Mock()
        self.window = LihatArtikel(parent)
    
    def tearDown(self):
        self.window.close()
        del self.window
        self.app.quit()
    
    def testFotoArtikel(self) :
        self.assertIsNotNone(self.window.fotoArtikel, "QLabel not found")
    
    def testNamaArtikel(self) :
        self.assertIsNotNone(self.window.namaArtikel, "QLabel not found")

    def testTextEditArtikel(self) :
        self.assertIsNotNone(self.window.textEdit, "QTextEdit not found")

    def testTanggalArtikel(self) :
        self.assertIsNotNone(self.window.tanggal, "QLabel not found")

    
    # def 