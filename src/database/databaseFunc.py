import sqlite3
import os
from sqlite3 import Error
from datetime import datetime

# Function to connect to the database file
def connectToDatabase(databaseFile):
    if (os.path.exists(databaseFile)):
        try:
            connection = sqlite3.connect(databaseFile)
            return connection
        except Error as e:
            print(e)
    return None

# Function to initialize all tables for the databases
def initializeTable(connection):
    create_table_resep = """CREATE TABLE IF NOT EXISTS Resep (
                            idResep INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                            gambarMasakan BLOB NOT NULL,
                            namaMasakan TEXT NOT NULL,
                            deskripsiMasakan TEXT NOT NULL,
                            langkahMemasak TEXT NOT NULL,
                            isDefault INTEGER NOT NULL DEFAULT 0,
                            CHECK (isDefault = 0 OR isDefault = 1)
                        ); """
    
    create_table_bahan = """CREATE TABLE IF NOT EXISTS Bahan (
                            idBahan INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                            namaBahan TEXT NOT NULL
                        ); """
    
    create_table_alat = """CREATE TABLE IF NOT EXISTS Alat (
                            idAlat INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                            namaAlat TEXT NOT NULL
                        ); """
    
    create_table_alatresep = """CREATE TABLE IF NOT EXISTS AlatResep (
                                idResep INTEGER NOT NULL,
                                idAlat INTEGER NOT NULL,
                                PRIMARY KEY (idResep, idAlat),
                                FOREIGN KEY (idResep) REFERENCES Resep(idResep),
                                FOREIGN KEY (idAlat) REFERENCES Alat(idAlat)
                            );"""
    
    create_table_bahanresep = """CREATE TABLE IF NOT EXISTS BahanResep (
                                idResep INTEGER NOT NULL,
                                idBahan INTEGER NOT NULL,
                                kuantitasBahan REAL NOT NULL,
                                satuanKuantitasBahan TEXT NOT NULL,
                                PRIMARY KEY (idResep, idBahan),
                                FOREIGN KEY (idResep) REFERENCES Resep(idResep),
                                FOREIGN KEY (idBahan) REFERENCES Bahan(idBahan)
                            );"""
    
    create_table_komentar = """CREATE TABLE IF NOT EXISTS Komentar (
                            idKomentar INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                            komentarFoto BLOB NOT NULL,
                            komentarTeks TEXT NOT NULL,
                            tanggalKomentar TEXT NOT NULL,
                            idResep INTEGER NOT NULL,
                            FOREIGN KEY (idResep) REFERENCES Resep(idResep)
                            ); """
    
    create_table_artikel = """CREATE TABLE IF NOT EXISTS Artikel (
                            idArtikel INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                            fotoArtikel BLOB NOT NULL,
                            judulArtikel TEXT NOT NULL,
                            isiArtikel TEXT NOT NULL,
                            tanggalPublikasi TEXT NOT NULL
                        ); """
    
    # Execute all commands above
    try: 
        connect = connection.cursor()
        connect.execute(create_table_resep)
        connect.execute(create_table_alat)
        connect.execute(create_table_bahan)
        connect.execute(create_table_alatresep)
        connect.execute(create_table_bahanresep)
        connect.execute(create_table_komentar)
        connect.execute(create_table_artikel)
    except Error as e:
        print(e)

# Function to change image to BLOB 
def imageToBlob(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

# Function to write blob data back to image
def writeTofile(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)

# Function to change blob data back to image for Resep and store the file in img/resep folder and return the path for the image
def resepBlobToImage(connection, id_resep):
    connect = connection.cursor()
    connect.execute("SELECT * FROM Resep WHERE idResep = ?", (id_resep,))
    data = connect.fetchall()
    path = r"..\img\resep"
    for row in data:
        name = row[2].replace(" ", "")
        path += "\\" + name + ".png"
        writeTofile(row[1], path)
    return path

# Function to change blob data back to image for artikel and store the file in img/artikel folder and return the path for the image
def artikelBlobToImage(connection, id_artikel):
    connect = connection.cursor()
    connect.execute("SELECT * FROM Artikel WHERE idArtikel = ?", (id_artikel,))
    data = connect.fetchall()
    path = r"..\img\artikel"
    for row in data:
        path += "\\artikel" + str(row[0]) + ".png"
        writeTofile(row[1], path)
    return path

# Function to change blob data back to image for komentar and store the file in img/komentar folder and return the path for the image
def komentarBlobToImage(connection, id_komentar):
    connect = connection.cursor()
    connect.execute("SELECT * FROM Komentar WHERE idKomentar = ?", (id_komentar,))
    data = connect.fetchall()
    path = r"..\img\komentar"
    for row in data:
        path += "\\komentar" + str(row[0]) + ".png"
        writeTofile(row[1], path)
    return path

# Function to convert string to datetime format
def stringToDatetime(date):
    return datetime.strptime(date, "%Y-%m-%d %H:%M:%S")

# Function to add rows or tuple to Resep table
def addResep(connection, nama_masakan, deskripsi_masakan, gambar_masakan, langkah_memasak, isDefault):
    add_new_resep = """INSERT INTO Resep (gambarMasakan, namaMasakan, deskripsiMasakan, langkahMemasak, isDefault) VALUES (?, ?, ?, ?, ?);"""
    connect = connection.cursor()
    connect.execute(add_new_resep, (gambar_masakan, nama_masakan, deskripsi_masakan, langkah_memasak, isDefault))
    connection.commit()

# Function to add rows or tuple to Alat table
def addAlat(connection, nama_alat):
    add_new_alat = """INSERT INTO Alat (namaAlat) VALUES (?);"""
    connect = connection.cursor()
    connect.execute(add_new_alat, (nama_alat,))
    connection.commit()

# Function to add rows or tuple to Bahan table
def addBahan(connection, nama_bahan):
    add_new_bahan = """INSERT INTO Bahan (namaBahan) VALUES (?);"""
    connect = connection.cursor()
    connect.execute(add_new_bahan, (nama_bahan,))
    connection.commit()

# Function to add rows or tuple to AlatResep table
def addAlatResep(connection, id_resep, id_alat):
    add_new_alatresep = """INSERT INTO AlatResep (idResep, idAlat) VALUES (?, ?);"""
    connect = connection.cursor()
    connect.execute(add_new_alatresep, (id_resep, id_alat))
    connection.commit()

# Function to add rows or tuple to BahanResep table
def addBahanResep(connection, id_resep, id_bahan, kuantitas_bahan, satuan_kuantitas_bahan):
    add_new_bahanresep = """INSERT INTO BahanResep (idResep, idBahan, kuantitasBahan, satuanKuantitasBahan) VALUES (?, ?, ?, ?);"""
    connect = connection.cursor()
    connect.execute(add_new_bahanresep, (id_resep, id_bahan, kuantitas_bahan, satuan_kuantitas_bahan))
    connection.commit()

# Function to add rows or tuple to Komentar table
def addKomentar(connection, komentar_foto, komentar_teks, id_resep):
    add_new_komentar = """INSERT INTO Komentar (komentarFoto, komentarTeks, tanggalKomentar, idResep) VALUES (?, ?, ?, ?);"""
    connect = connection.cursor()
    time = datetime.now()
    connect.execute(add_new_komentar, (komentar_foto, komentar_teks, time.strftime("%Y-%m-%d %H:%M:%S"), id_resep))
    connection.commit()

# Function to add rows or tuple to Artikel table
def addArtikel(connection, foto_artikel, judul_artikel, isi_artikel, tanggal_publikasi):
    add_new_artikel = """INSERT INTO Artikel (fotoArtikel, judulArtikel, isiArtikel, tanggalPublikasi) VALUES (?, ?, ?, ?);"""
    connect = connection.cursor()
    connect.execute(add_new_artikel, (foto_artikel, judul_artikel, isi_artikel, tanggal_publikasi))
    connection.commit()

# Function to get every data in Resep
def getDaftarResep(connection):
    connect = connection.cursor()
    connect.execute("SELECT * FROM Resep;")
    data = connect.fetchall()
    return data

# Function to get data with idResep = resep_id in Resep
def getResep(connection, resep_id):
    connect = connection.cursor()
    connect.execute("SELECT * FROM Resep WHERE idResep = ?;" , (resep_id,))
    data = connect.fetchall()
    return data

# Function to get all data from Alat table
def getAlat(connection):
    connect = connection.cursor()
    connect.execute("SELECT * FROM Alat;")
    data = connect.fetchall()
    return data

# Function to get all data from Bahan table
def getBahan(connection):
    connect = connection.cursor()
    connect.execute("SELECT * FROM Bahan;")
    data = connect.fetchall()
    return data

# Function to get every tool needed in a recipe from Alat table
def getAlatResep(connection, resep_id):
    connect = connection.cursor()
    connect.execute("SELECT idAlat, namaAlat FROM Resep NATURAL JOIN AlatResep NATURAL JOIN Alat WHERE idResep = ?;", (resep_id,))
    data = connect.fetchall()
    return data

# Function to get every material needed in a recipe from Bahan table
def getBahanResep(connection, resep_id):
    connect = connection.cursor()
    connect.execute("SELECT idBahan, namaBahan, kuantitasBahan, satuanKuantitasBahan FROM Resep NATURAL JOIN BahanResep NATURAL JOIN Bahan WHERE idResep = ?;", (resep_id,))
    data = connect.fetchall()
    return data

# Function to get every data in Artikel table
def getDaftarArtikel(connection):
    connect = connection.cursor()
    connect.execute("SELECT * FROM Artikel;")
    data = connect.fetchall()
    return data

# Function to get data with idArtikel = artikel_id in Artikel table
def getArtikel(connection, artikel_id):
    connect = connection.cursor()
    connect.execute("SELECT * FROM Artikel WHERE idArtikel = ?;", (artikel_id, ))
    data = connect.fetchone()
    return data

# Function to get every data with idResep = resep_id in Komentar table
def getKomentar(connection, resep_id):
    connect = connection.cursor()
    connect.execute("SELECT * FROM KOMENTAR WHERE idResep = ?;", (resep_id, ))
    data = connect.fetchall()
    return data

# Function to get idAlat where namaAlat = alat_name in Alat table
def getIdAlat(connection, alat_name):
    connect = connection.cursor()
    connect.execute("SELECT idAlat FROM Alat WHERE namaAlat = ?;", (alat_name, ))
    data = connect.fetchone()
    return data[0]

# Function to get idBahan where namaBahan = bahan_name in Bahan table
def getIdBahan(connection, bahan_name):
    connect = connection.cursor()
    connect.execute("SELECT idBahan FROM Bahan WHERE namaBahan = ?;", (bahan_name, ))
    data = connect.fetchone()
    return data[0]

# Funciton to get idResep where namaMasakan = resep_name in Resep table
def getIdResep(connection, resep_name):
    connect = connection.cursor()
    connect.execute("SELECT idResep FROM Resep WHERE namaMasakan = ?;", (resep_name, ))
    data = connect.fetchone()
    return data[0]

# Function to get idKomentar where idResep = resep_id in Komentar table
def getIdKomentar(connection, resep_id):
    connect = connection.cursor()
    connect.execute("SELECT idKomentar FROM Komentar WHERE idResep = ?;", (resep_id, ))
    data = connect.fetchall()
    return data

# Function to get the last ID Resep in database
def getLastIdResep(connection):
    connect = connection.cursor()
    connect.execute("SELECT seq FROM sqlite_sequence WHERE name ='Resep';")
    data = connect.fetchone()
    return data[0]

def getLastIdKomentar(connection):
    connect = connection.cursor()
    connect.execute("SELECT seq FROM sqlite_sequence WHERE name ='Komentar';")
    data = connect.fetchone()
    if data is not None and data[0] is not None:
        return data[0]
    else :
        return 0

# Function to get all satuanKuantitasBahan that is unique in BahanResep
def getSatuanKuantitasBahan(connection):
    connect = connection.cursor()
    connect.execute("SELECT DISTINCT satuanKuantitasBahan FROM BahanResep;")
    data = connect.fetchall()
    return data

# Function to get komentarFoto path

# Function to create view for every data with namaResep contains keyword substring in Resep table
def searchResepView(connection, keyword):
    connect = connection.cursor()
    connect.execute("DROP VIEW IF EXISTS SearchResepView;")
    query = "CREATE VIEW SearchResepView AS SELECT * FROM Resep WHERE namaMasakan LIKE " + "'%" + keyword + "%';"
    connect.execute(query)
    connect.execute("SELECT * FROM SearchResepView;")
    data = connect.fetchall()
    connection.commit()
    return data

# Function to delete tuples from AlatResep table
def deleteAlatResep(connection, resep_id):
    connect = connection.cursor()
    connect.execute("DELETE FROM AlatResep WHERE idResep = ?;", (resep_id, ))
    connection.commit()

# Function to delete tuples from BahanResep table
def deleteBahanResep(connection, resep_id):
    connect = connection.cursor()
    connect.execute("DELETE FROM BahanResep WHERE idResep = ?;", (resep_id, ))
    connection.commit()

# Function to delete all komentar with idResep = resep_idt
def deleteKomentarResep(connection, resep_id):
    connect = connection.cursor()
    connect.execute("DELETE FROM Komentar WHERE idResep = ?;", (resep_id, ))
    connection.commit()

# Function to delete a tuple from Resep table
def deleteResep(connection, resep_id):
    connect = connection.cursor()
    deleteAlatResep(connection, resep_id)
    deleteBahanResep(connection, resep_id)
    connect.execute("DELETE FROM Resep WHERE idResep = ?;", (resep_id, ))
    connection.commit()

# Function to delete a tuple from Komentar table
def deleteKomentar(connection, komentar_id):
    connect = connection.cursor()
    connect.execute("DELETE FROM Komentar WHERE idKomentar = ?;", (komentar_id, ))
    connection.commit()

# Function to update a tuple in Resep table
def editResep(connection, resep_id, gambar_masakan, nama_masakan, deskripsi_masakan, langkah_memasak):
    connect = connection.cursor()
    connect.execute("UPDATE Resep SET gambarMasakan = ?, namaMasakan = ?, deskripsiMasakan = ?, langkahMemasak = ? WHERE idResep = ?;", (gambar_masakan, nama_masakan, deskripsi_masakan, langkah_memasak, resep_id))
    connection.commit()





