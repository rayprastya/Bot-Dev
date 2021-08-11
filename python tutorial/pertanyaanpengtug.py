# Definisi Prodi
D3TI = 'D3 Teknik Informatika'
D4TI = 'D4 Teknik Informatika'
D3MI = 'D3 Manajemen Informatika'
D3A = 'D3 Akutansi'
D4AK = 'D4 Akutansi Keuangan'
D3MP = 'D3 Manajemen Pemasaran'
D4MP = 'D4 Manajemen Perusahaan'
D3AL = 'D3 Administrasi Logistik'
D4LB = 'D4 Logistik Bisnis'
D4LN = 'D4 Logistik Niaga'

# Definisi Matkul D4TI
MT111 = 'Matematika Diskrit'
MT112 = 'Bahasa Indonesia'
MT113 = 'Pendidikan Pancasila dan Kewarganegaraan'
MT114 = 'Arsitektur Komputer'
MT115 = 'Pemrograman I'
MT116 = 'General English I'
MT117 = 'Algoritma I'

MT121 = 'Aljabar Linear'
MT122 = 'Database I'
MT123 = 'Sistem Operasi'
MT124 = 'Analisis dan Perancangan Sistem Informasi'
MT125 = 'General English II'
MT126 = 'Algoritam II'
MT127 = 'Proyek I'

MT211 = 'Jaringan Komputer'
MT212 = 'Pemrograman II'
MT213 = 'Desain Interaksi'
MT214 = 'General English III'
MT215 = 'Rekayasa Perangkat Lunak I'
MT216 = 'Database II'
MT217 = 'Metodologi Penelitian'
MT218 = 'Proyek II'

MT221 = 'Manajemen Distribusi'
MT222 = 'Manajemen Proyek'
MT223 = 'Administrasi Jaringan Komputer'
MT224 = 'Sistem ERP I'
MT225 = 'Cyberpreneurship'
MT226 = 'Etika dan Manajemen Profesi IT'
MT227 = 'Pemrograman III'

MT311 = 'Pemrograman IV'
MT312 = 'Keamanan Jaringan'
MT313 = 'Sistem ERP 2'
MT314 = 'Sistem Informasi Geografis'
MT315 = 'Supply Chain Management'
MT316 = 'Proyek III'

MT321 = 'Expert System'
MT322 = 'Data Mining'
MT323 = 'Statistika Probabilitas'
MT324 = 'Kapita Selekta'
MT325 = 'Artificial Intelligence'
MT326 = 'General English IV'
MT327 = 'Multimedia System'
MT328 = 'Distributor System'

# Definisi Prodi Per Semester
SEMESTER_1_TINGKAT_1 = [MT111, MT112, MT113, MT114, MT115, MT116, MT117]
SEMESTER_2_TINGKAT_1 = [MT121, MT122, MT123, MT124, MT125, MT126, MT127]

SEMESTER_1_TINGKAT_2 = [MT211, MT212, MT213, MT214, MT215, MT216, MT217, MT218]
SEMESTER_2_TINGKAT_2 = [MT221, MT222, MT223, MT224, MT225, MT226, MT227]

SEMESTER_1_TINGKAT_3 = [MT311, MT312, MT313, MT314, MT315, MT316]
SEMESTER_2_TINGKAT_3 = [MT321, MT322, MT323, MT324, MT325, MT326, MT327, MT328]

# Definisi Tingkat D4TI
D4_TI_1 = [SEMESTER_1_TINGKAT_1, SEMESTER_2_TINGKAT_1]
D4_TI_2 = [SEMESTER_1_TINGKAT_2, SEMESTER_2_TINGKAT_2]
D4_TI_3 = [SEMESTER_1_TINGKAT_3, SEMESTER_2_TINGKAT_3]

# Deklarasi Variabel
daftarProdi = [D4TI,D3TI,D3MI,D3A,D4AK,D3MP,D4MP,D3AL,D4LB,D4LN]
inProdi = ""
inTingkat = ""
# Deklarasi Variabel\

# Cek Prodi
def cekProdi():
    print('Daftar Prodi')
    for dp in range(len(daftarProdi)):
        print(str(dp+1)+'. '+daftarProdi[dp])
    pilih = int(input('Masukkan Pilihan Prodi Anda: '))
    inProdi = str(daftarProdi[pilih-1])
    return inProdi
# Cek Prodi\

# Cek Tingkat
def cekTingkat():
    print('Daftar Tingkat Prodi: \nA. Tingkat 1\nB. Tingkat 2\nC. Tingkat 3')
    pilihTingkat = input('Masukkan Pilihan Prodi Anda: ')
    if pilihTingkat == 'a' or pilihTingkat == 'A':
        inTingkat = 1
    elif pilihTingkat == 'b' or pilihTingkat == 'B':
        inTingkat = 2
    elif pilihTingkat == 'c' or pilihTingkat == 'C':
        inTingkat = 3
    return inTingkat
# Cek Tingkat\

# Program
inProdi = cekProdi()
print('')
inTingkat = cekTingkat()
print('')
print('Anda merupakan anggota dari '+ inProdi+' Tingkat '+str(inTingkat))