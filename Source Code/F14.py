#Clarisa Natalia Edelin 16519420
#F14 Melihat riwayat penggunaan DatabaseWahana
#Admin dapat melihat riwayat penggunaan DatabaseWahana

#Kamus
import CONST_VARS

#Algoritma
def lihatriwayatwahana (DatabasePenggunaan):
    #bagian input username pemain
    Id_wahana = input('Masukkan ID Wahana: ')

    Id_DatabaseWahana_ygsama = [['' for i in range(4)] for j in range(CONST_VARS.N)]

    #bagian cek DatabasePenggunaan
    idx = 0
    for row in DatabasePenggunaan:
        if Id_wahana == row[2]: #kalau sama
            Id_DatabaseWahana_ygsama[idx] = row #dimasukin ke array baru
            idx += 1


    for i in range(idx):
        # tanggal   |   username    |   jumlah
        print(Id_DatabaseWahana_ygsama[i][1] + '\t|\t' + Id_DatabaseWahana_ygsama[i][0] + '\t|\t' + Id_DatabaseWahana_ygsama[i][3])
