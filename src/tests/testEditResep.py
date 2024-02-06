import unittest
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QTextEdit
from editResep import *
from PyQt5.QtTest import QTest
import sys
from unittest.mock import Mock

class testAddResep(unittest.TestCase) :
    def setUp(self):
        self.app = QApplication(sys.argv)
        parent = Mock()
        self.window = FormEditResep(parent)
    
    def tearDown(self):
        self.window.close()
        del self.window
        self.app.quit()

    def testEditJudul(self):
        self.expectedText = "Rendang"
        self.window.inputJudul_resep.setPlainText(self.expectedText)
        judulMasakan = self.window.inputJudul_resep.toPlainText()
        self.assertIsNotNone(judulMasakan, "QTextEdit not found")
        self.assertEqual(judulMasakan, self.expectedText)
    
    def testEditDeskripsi(self):
        self.expectedText = "Masakan wuenak"
        self.window.inputDeskripsi_resep.setPlainText(self.expectedText)
        deskripsiMasakan = self.window.inputDeskripsi_resep.toPlainText()
        self.assertIsNotNone(deskripsiMasakan, "QTextEdit not found")
        self.assertEqual(deskripsiMasakan, self.expectedText)

    def testAlatLabel(self):
        self.assertEqual(self.window.alat_label.text(), "Alat")

    def testBahanLabel(self):
        self.assertEqual(self.window.bahan_label.text(), "Bahan")