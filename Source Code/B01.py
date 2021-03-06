# Josep Marcello / 16519170
# 8 April 2020
# Program hashing
# Program untuk meng-hash password (dan salt) serta mencocokan password sebenarnya dengan input

# TODO

# KAMUS
# function hash(Password : string) --> string
# fungsi akan mengubah string Password menjadi sebuah string yang sudah di-hash dengan salt

# function check_password(PasswordInput : string, PasswordUser : string) --> boolean
# fungsi akan mencocokan PasswordInput dengan PasswordUser dan menghasilkan True jika sama

# ALGORTIMA 

# Menyiapkan library yang dibutuhkan
from hashlib import sha512
from uuid import uuid1

# Realisasi fungsi dan prosedur
def hash(Password):
    # KAMUS LOKAL
	# salt : string

    # ALGORITMA FUNGSI
	# Membuat salt (pengaman password) dengan random number generator
    salt = uuid1().hex
	# Menyimpan salt dengan password
    Password = sha512(Password.encode()+salt.encode()).hexdigest() + ":" + salt
    return Password

def check_password(PasswordInput,PasswordUser):
	# KAMUS LOKAL
	# Salt : string
	
	# ALGORITMA FUNGSI
	# Memisahkan password yang sudah ditambahkan salt dengan salt-nya
    PasswordUser,Salt = PasswordUser.split(":")
	# Mencocokan password yang sudah ditambahkan salt dengan password yang diinput kemudian ditambah salt
    return PasswordUser == sha512(PasswordInput.encode()+Salt.encode()).hexdigest()