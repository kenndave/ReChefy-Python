import unittest
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QTextEdit
from lihatResep import *
from PyQt5.QtTest import QTest
import sys
from unittest.mock import Mock

class testLihatResep(unittest.TestCase) :
    def setUp(self):
        self.app = QApplication(sys.argv)
        parent = Mock()
        self.window = LihatResep(parent)
    
    def tearDown(self):
        self.window.close()
        del self.window
        self.app.quit()

    def testSendButton(self):
        self.window.readDatabase()
        self.expectedText = "Hello World"
        komentarID = self.window.lastKomentarID+1
        self.window.textEdit.setPlainText(self.expectedText)
        QTest.mouseClick(self.window.sendButton, QtCore.Qt.LeftButton)
        isiKomentarName = "isiKomentar_" + str(komentarID)
        isiKomentar = self.window.findChild(QTextEdit, isiKomentarName)
        self.assertIsNotNone(isiKomentar, "QTextEdit not found")
        self.actualText = isiKomentar.toPlainText()
        self.assertEqual(self.actualText, self.expectedText)
    
    def testAlat(self):
        self.assertEqual(self.window.alat.text(), "Alat")

    def testBahan(self):
        self.assertEqual(self.window.bahan.text(), "Bahan")
    
    def testLangkahMemasak(self) :
        self.assertEqual(self.window.langkahMemasak.text(), "Langkah Memasak")
    
    def testKomentarCount(self) :
        self.window.readDatabase()
        expectedJudulKomentar = f"Komentar ({self.window.total})"
        actualJudulKomentar = self.window.judulKomentar.text()
        self.assertEqual(actualJudulKomentar, expectedJudulKomentar)
        
    
    

    

