import unittest
from database.databaseFunc import *

class ModuleTesting(unittest.TestCase):

    def testGetIDResep(self):
        self.connection = connectToDatabase(r"./tests/test.db")
        self.assertEqual(getIdResep(self.connection, "Tempe Mendoan"), 14)
    
    def testGetIDAlat(self):
        self.connection = connectToDatabase(r"./tests/test.db")
        self.assertEqual(getIdAlat(self.connection, "Loyang"), 26)
    
    def testGetIDBahan(self):
        self.connection = connectToDatabase(r"./tests/test.db")
        self.assertEqual(getIdBahan(self.connection, "Garam"), 9)
    
    def testDeleteResep(self):
        self.connection = connectToDatabase(r"./tests/test.db")
        deleteResep(self.connection, 10)
        self.assertEqual(getResep(self.connection, 10), [])

    def testDeleteAlatResep(self):
        self.connection = connectToDatabase(r"./tests/test.db")
        deleteAlatResep(self.connection, 10)
        self.assertEqual(getAlatResep(self.connection, 10), [])
    
    def testDeleteBahanResep(self):
        self.connection = connectToDatabase(r"./tests/test.db")
        deleteBahanResep(self.connection, 10)
        self.assertEqual(getBahanResep(self.connection, 10), [])
    
    def testGetKomentar(self):
        self.connection = connectToDatabase(r"./tests/test.db")
        self.assertEqual(getKomentar(self.connection, 10), [])
    
    def testAddAlat(self):
        self.connection = connectToDatabase(r"./tests/test.db")
        # addAlat(self.connection, "tesgan") Udah di tambahin di unit testing pertama
        self.assertEqual(getIdAlat(self.connection, "tesgan"), 27)
    
    def testAddBahan(self):
        self.connection = connectToDatabase(r"./tests/test.db")
        # addBahan(self.connection, "tesgan") Udah ditambahin di unit testing pertama
        self.assertEqual(getIdBahan(self.connection, "tesgan"), 91)
