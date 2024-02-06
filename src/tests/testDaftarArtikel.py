import unittest
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QTextEdit
from daftarArtikel import *
from PyQt5.QtTest import QTest
import sys
from unittest.mock import Mock

class testDaftarArtikel(unittest.TestCase):
    def setUp(self):
        self.app = QApplication(sys.argv)
        parent = Mock()
        self.window = DaftarArtikel(parent)
        
    def tearDown(self):
        self.window.close()
        del self.window
        self.app.quit()
        
    def testSearchBar(self):
        self.expectedText = "Daftar Artikel"
        self.assertEqual(self.window.titleLabel.text(), self.expectedText)
