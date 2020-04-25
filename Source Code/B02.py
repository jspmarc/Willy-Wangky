# Muhammad Fahmi Alamsyah/16519300
# 19 April 2020
# Program Golden Account
# Program membuat user menjadi gold account jika syarat
# terpenuhi

import CONST_VARS

def up_gold(InfoUser):
    #Menerima informasi user
    Username = input("Masukkan username: ")

    found = False
    IndexUser = 0
    for user in InfoUser:
        if user[3] == Username:
            found = True
            #misal untuk menjadi golden ticket user harus membayar 50K
            if int(user[6]) >= 50000 and user[7] == "FALSE":
                user[7] = "TRUE"
                user[6] = int(user[6]) - 50000
                print("Akun Anda telah diupgrade.")
                break
            elif (user[7] == "TRUE"):
                print("Anda sudah gold user")
            else: # Saldo tidak cukup
                print("Saldo anda tidak cukup, silakan topup dahulu!")
                break
        IndexUser += 1
        
    if not found :
        print("Tidak ada username")
        return InfoUser
        
    # Mendapatkan index pemain baru
    # IndexUser = 1
    # row = InfoUser[IndexUser] # First element

    # while (row != CONST_VARS.MARK_4):
        # IndexUser += 1
        # row = InfoUser[IndexUser] # Next element

    InfoUser[IndexUser] = user
    return (InfoUser)

