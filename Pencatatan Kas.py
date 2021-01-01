import sqlite3
nama = 'admin'
password = 'admin'

class DataManager:
    def __init__(self):
        self.con = sqlite3.connect('F:/database/nabungyuk.sqlite3')
        self.cursor = self.con.cursor() 
    def executeQuery(self, query, retVal=False):
        self.cursor.execute(query)
        all_results = self.cursor.fetchall()
        self.con.commit()
        if retVal:
            return all_results

class User(DataManager):
    def setDataUser(self, nama, password):
        self.query = 'INSERT INTO User (nama, password) \
            VALUES (\'%s\', \'%s\')' 
        self.query = self.query % (nama, password)
        print('self.query : ', self.query )
        self.executeQuery(self.query)

    def getDataUser(self, nama, password):
        self.query = 'SELECT id_user FROM User \
            where nama=\'%s\' and password=\'%s\'' 
        self.query = self.query % (nama, password)
        print('self.query : ', self.query )
        id_user = self.executeQuery(self.query, retVal=True)
        return id_user

class Pemasukan(User):
    def setDataPemasukan(self, pemasukan, keterangan):
        self.setDataUser(nama, password)
        id_user = self.getDataUser(nama, password)
        self.query = 'INSERT INTO pemasukan (id_user, pemasukan, keterangan)\
            values (%s, \'%s\', \'%s\')' 
        self.query = self.query % (id_user[0][0], pemasukan, keterangan)
        print('self.query : ', self.query )
        self.executeQuery(self.query)

    def getPemasukan(self):
        self.query = 'SELECT pemasukan, keterangan FROM pemasukan '
        data = self.executeQuery(self.query, True)
        return data


class Pengeluaran(User):        
     def setDataPengeluaran(self, pengeluaran, keterangan):
        self.setDataUser(nama, password)
        id_user = self.getDataUser(nama, password)
        self.query = 'INSERT INTO pengeluaran (id_user, pengeluaran, keterangan)\
            values (%s, \'%s\', \'%s\')' 
        self.query = self.query % (id_user[0][0], pengeluaran, keterangan)
        print('self.query : ', self.query )
        self.executeQuery(self.query)

     def getPengeluaran(self):
        self.query = 'SELECT *FROM pengeluaran '
        data = self.executeQuery(self.query, True)
        return data

class Balance(DataManager):
    def saldo(self):
        self.query = 'SELECT (SELECT sum(pemasukan) FROM pemasukan) + \
        (SELECT (-sum(pengeluaran)) FROM pengeluaran) as saldo'
        data = self.executeQuery(self.query, True)
        return data


pms = Pemasukan()
png = Pengeluaran()
sld = Balance()
jalan = True


class Main(object):
    def tampilkanPilihan():
        print ('selamat datang')
        print('-----------------')
        print('Pilih menu:')
        print('1. Tambah pemasukan')
        print('2. Tambah Pengeluaran')
        print('3. Lihat Pemasukan')
        print('4. Lihat Pengeluaran')
        print('5. Melihat Saldo')
        pilihan = input('Masukkan pilihan: ')
        return pilihan

    def tambahDataPemasukan():
        global pms
        print('\nTambah data pemasukan:')
        pemasukan = input('Masukkan pemasukan: ')
        print('pemasukan: ', pemasukan)
        keterangan = input('Masukkan keterangan: ')
        print ('keterangan: ', keterangan)
        pms.setDataPemasukan(pemasukan, keterangan)
        print('\n')

    def tambahDataPengeluaran():
        global png
        print('\nTambah data pengeluaran:')
        pengeluaran = input('Masukkan pengeluaran: ')
        print('pengeluaran: ', pengeluaran)
        keterangan = input('Masukkan keterangan: ')
        print ('keterangan: ', keterangan)
        png.setDataPengeluaran(pengeluaran, keterangan)
        print('\n')

    def tampilkanDataPemasukan():
        print('\npemasukan:')
        dataPemasukan =pms.getPemasukan()
        for row in dataPemasukan:
            print(row)
        print('\n')

    def tampilkanDataPengeluaran():
        print('\npengeluaran:')
        dataPengeluaran =png.getPengeluaran()
        for row in dataPengeluaran:
            print(row)
        print('\n')

    def melihatSaldo():
        print('\nSaldo Tersisa:')
        saldoo = sld.saldo()
        for row in saldoo:
            print(row)
        print('\n')


    while jalan:
        pilihan = tampilkanPilihan()
        if pilihan == '1':
            tambahDataPemasukan()
            
        elif pilihan == '2':
            tambahDataPengeluaran()

        elif pilihan == '3':
            tampilkanDataPemasukan()

        elif pilihan == '4':
            tampilkanDataPengeluaran()

        elif pilihan == '5':
            melihatSaldo()


main()
