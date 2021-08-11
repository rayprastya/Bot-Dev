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

# Definisi Prodi Per Semester D4TI
MT11 = [MT111, MT112, MT113, MT114, MT115, MT116, MT117]
MT12 = [MT121, MT122, MT123, MT124, MT125, MT126, MT127]

MT21 = [MT211, MT212, MT213, MT214, MT215, MT216, MT217, MT218]
MT22 = [MT221, MT222, MT223, MT224, MT225, MT226, MT227]

MT31 = [MT311, MT312, MT313, MT314, MT315, MT316]
MT32 = [MT321, MT322, MT323, MT324, MT325, MT326, MT327, MT328]

# Definisi Tingkat D4TI
D4_TI_1 = [MT11, MT12]
D4_TI_2 = [MT21, MT22]
D4_TI_3 = [MT31, MT32]

# Deklarasi Variabel
daftarProdi = [D4TI,D3TI,D3MI,D3A,D4AK,D3MP,D4MP,D3AL,D4LB,D4LN]
inProdi = ""
inTingkat = ""
inSemester = ""
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

# Cek Semester
def cekSemester():
    semesterBenar = False
    pilihSemester = input("Semester berapa Anda?: ")
    while semesterBenar == False:
        if int(pilihSemester)>2 or int(pilihSemester)<1:
            pilihSemester = input("Masukkan semester dengan benar! (1 atau 2): ")
        else:
            semesterBenar = True
    return pilihSemester
# Cek Semester\

# Get Daftar Matkul
def getMatkul(prodi,tingkat,semester):
    if tingkat == 1:
        if semester == 1:
            return MT11
        elif semester == 2:
            return MT12
    elif tingkat == 2:
        if semester == 1:
            return MT21
        elif semester == 2:
            return MT22
    elif tingkat == 3:
        if semester == 1:
            return MT31
        elif semester == 2:
            return MT32
# Get Daftar Matkul\

# Definisi Tugas

tugasAktif = { 1: {"matkul": MT117, "tugas": "Kerjakan Modul Oracle DD 5-1"},
               2: {"matkul": MT116, "tugas": "Latihan Excersice 1"}}

# Definisi Tugas\

# Cek & Kumpul Tugas

def operasiTugas(inState):
    if 'cek' in inState:
        print('Daftar Tugas yang aktif: ')
        for taktif in range(len(tugasAktif)):
            print(str(taktif+1) + '. ' + tugasAktif[taktif+1]['matkul'] + ' | ' + tugasAktif[taktif+1]['tugas'])
    elif 'kumpul' in inState:
        print('coming soon')

# Cek & Kumpul Tugas\

# Program
inProdi = cekProdi()
print('')
inTingkat = cekTingkat()
print('')
inSemester = cekSemester()
inSemester = int(inSemester)
print('Anda merupakan anggota dari '+ inProdi+' Tingkat '+str(inTingkat)+' Semester '+str(inSemester))
print('Daftar Mata Kuliah yang Anda tempuh saat ini: ')
daftarMatkul = getMatkul(inProdi,inTingkat,inSemester)
for dm in range(len(daftarMatkul)):
    print(str(dm+1)+'. '+daftarMatkul[dm])

state = input("Silakan ketikkan yang akan anda lakukan (cek tugas, kumpul tugas [kode matkul], exit): ")
operasiTugas(state)