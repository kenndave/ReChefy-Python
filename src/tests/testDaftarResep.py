import unittest
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QTextEdit
from daftarResep import *
from PyQt5.QtTest import QTest
import sys
from unittest.mock import Mock

class testDaftarResep(unittest.TestCase):
    def setUp(self):
        self.app = QApplication(sys.argv)
        parent = Mock()
        self.window = DaftarResep(parent)
        
    def tearDown(self):
        self.window.close()
        del self.window
        self.app.quit()
        
    def testSearchBar(self):
        if (self.window.searchBar.text() != ""):
            self.expectedText = "Hasil Pencarian"
        else:
            self.expectedText = "Daftar Resep"
        self.assertEqual(self.window.titleLabel.text(), self.expectedText)