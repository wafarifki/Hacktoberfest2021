print('''
		[ Saya akan menebak umur Anda ]
	[ Silahkan Anda masukkan tahun kelahiran Anda ]
	''')

tahun_kelahiran = input("  Masukkan tahun kelahiran : ")
tahun_sekarang = 2021 - int(tahun_kelahiran)
print("  Usia Anda " + str(tahun_sekarang) + " tahun") 