"""
Tugas Mandiri OOP Python - Sistem Penggajian Karyawan (Payroll System)
Versi dengan penjelasan di samping setiap baris kode.
"""


# =====================================================================
# CLASS KARYAWAN (SUPERCLASS / INDUK)
# =====================================================================
class Karyawan:  # membuat cetakan (class) bernama Karyawan; isinya adalah baris yang menjorok di bawahnya

    def __init__(self, nama, id_karyawan, gaji_pokok):  # constructor: otomatis jalan saat objek dibuat; self = objek itu sendiri
        self.nama = nama                    # simpan nama ke atribut public 'nama' milik objek
        self.id_karyawan = id_karyawan      # simpan ID ke atribut public 'id_karyawan'
        self.__gaji_pokok = 0               # atribut PRIVATE (awalan __), diberi nilai awal 0 supaya atributnya pasti ada
        self.gaji_pokok = gaji_pokok        # tanpa __ -> memanggil SETTER, jadi gaji awal ikut divalidasi

    # ---------------- GETTER & SETTER (ENCAPSULATION) ----------------
    @property                               # menandai method di bawah sebagai GETTER (untuk membaca nilai)
    def gaji_pokok(self):                   # nama getter; dari luar dipakai seperti atribut: objek.gaji_pokok
        return self.__gaji_pokok            # kembalikan isi atribut private (di dalam class boleh dibaca)

    @gaji_pokok.setter                      # menandai method di bawah sebagai SETTER (untuk mengubah nilai)
    def gaji_pokok(self, nilai):            # 'nilai' = angka baru yang ingin disimpan
        if nilai <= 0:                      # cek validasi: nilai nol atau negatif dianggap tidak valid
            print(f"[PERINGATAN] Gaji pokok tidak valid ({nilai}). "     # tampilkan peringatan; {nilai} diganti isi variabel
                  f"Nilai harus lebih dari 0. Gaji pokok tidak diubah.")  # lanjutan pesan; gaji lama tetap aman
        else:                               # jika nilai valid (lebih dari 0)
            self.__gaji_pokok = nilai       # barulah gaji pokok diubah; satu-satunya tempat yang boleh mengubahnya

    # ---------------- METHOD LAIN ----------------
    def hitung_gaji_total(self):            # method penghitung gaji total (implementasi dasar)
        return self.__gaji_pokok            # di induk: total gaji = gaji pokok saja

    def tampilkan_info(self):               # method untuk menampilkan data karyawan
        print(f"Nama          : {self.nama}")                       # cetak nama
        print(f"ID Karyawan   : {self.id_karyawan}")                # cetak ID
        print(f"Gaji Pokok    : Rp{self.__gaji_pokok:,.0f}")        # cetak gaji; ':,.0f' = pemisah ribuan, tanpa desimal


# =====================================================================
# CLASS KARYAWANTETAP (CHILD / ANAK DARI KARYAWAN)
# =====================================================================
class KaryawanTetap(Karyawan):              # (Karyawan) = INHERITANCE: mewarisi semua atribut & method induk

    def __init__(self, nama, id_karyawan, gaji_pokok, tunjangan):  # constructor; ada tambahan parameter 'tunjangan'
        super().__init__(nama, id_karyawan, gaji_pokok)  # panggil constructor induk untuk mengisi nama, ID, gaji pokok
        self.tunjangan = tunjangan          # atribut tambahan (public) khusus karyawan tetap

    def hitung_gaji_total(self):            # OVERRIDING: method bernama sama dengan induk, isinya diganti
        return self.gaji_pokok + self.tunjangan  # rumus: gaji pokok + tunjangan (pakai getter, bukan __gaji_pokok)

    def tampilkan_info(self):               # OVERRIDING: tampilan khusus karyawan tetap
        print("--- Karyawan Tetap ---")     # judul penanda jenis karyawan
        super().tampilkan_info()            # jalankan versi induk (nama, ID, gaji pokok) agar tidak menulis ulang
        print(f"Tunjangan     : Rp{self.tunjangan:,.0f}")                    # cetak tunjangan
        print(f"Total Gaji    : Rp{self.hitung_gaji_total():,.0f}")          # cetak total gaji (versi karyawan tetap)


# =====================================================================
# CLASS KARYAWANKONTRAK (CHILD / ANAK DARI KARYAWAN)
# =====================================================================
class KaryawanKontrak(Karyawan):            # juga mewarisi Karyawan

    def __init__(self, nama, id_karyawan, gaji_pokok, jam_lembur, tarif_lembur):  # constructor; tambahan: jam & tarif lembur
        super().__init__(nama, id_karyawan, gaji_pokok)  # panggil constructor induk untuk data dasar
        self.jam_lembur = jam_lembur        # total jam lembur sebulan (public)
        self.tarif_lembur = tarif_lembur    # tarif lembur per jam (public)

    def hitung_gaji_total(self):            # OVERRIDING dengan rumus untuk karyawan kontrak
        return self.gaji_pokok + (self.jam_lembur * self.tarif_lembur)  # gaji pokok + (jam x tarif); kurung dihitung dulu

    def tampilkan_info(self):               # OVERRIDING: tampilan khusus karyawan kontrak
        print("--- Karyawan Kontrak ---")   # judul penanda jenis karyawan
        super().tampilkan_info()            # cetak nama, ID, gaji pokok lewat method induk
        print(f"Jam Lembur    : {self.jam_lembur} jam")                      # cetak jam lembur
        print(f"Tarif Lembur  : Rp{self.tarif_lembur:,.0f}/jam")             # cetak tarif per jam
        print(f"Total Lembur  : Rp{self.jam_lembur * self.tarif_lembur:,.0f}")  # uang lembur = jam x tarif
        print(f"Total Gaji    : Rp{self.hitung_gaji_total():,.0f}")          # cetak total gaji (versi kontrak)


# =====================================================================
# MAIN PROGRAM (DI SINILAH PROGRAM BENAR-BENAR BERJALAN)
# =====================================================================
if __name__ == "__main__":                  # blok ini hanya jalan jika file dijalankan langsung (bukan di-import)

    # 1. Buat objek
    tetap = KaryawanTetap("Budi Santoso", "KT-001", 7_000_000, 1_500_000)  # objek karyawan tetap; gaji 7 juta, tunjangan 1,5 juta
    kontrak = KaryawanKontrak("Siti Aminah", "KK-001", 4_500_000, 20, 50_000)  # objek kontrak; gaji 4,5 juta, lembur 20 jam @50 ribu

    # 2. Simpan dalam list
    daftar_karyawan = [tetap, kontrak]      # list berisi 2 objek; indeks 0 = Budi, indeks 1 = Siti

    # 3. Polymorphism: method yang sama, perilaku berbeda
    print("=" * 40)                         # cetak karakter '=' sebanyak 40 kali sebagai garis pembatas
    print("DAFTAR KARYAWAN (POLYMORPHISM)")  # judul bagian
    print("=" * 40)                         # garis pembatas
    for k in daftar_karyawan:               # ulangi untuk tiap isi list; k = Budi di putaran 1, Siti di putaran 2
        k.tampilkan_info()                  # satu perintah sama, hasil berbeda sesuai jenis objek (POLYMORPHISM)
        print()                             # cetak baris kosong sebagai pemisah

    # 4. Encapsulation: ubah gaji pokok
    print("=" * 40)                         # garis pembatas
    print("DEMO ENCAPSULATION")             # judul bagian demo
    print("=" * 40)                         # garis pembatas

    print("Mengubah gaji pokok Budi dengan nilai tidak valid (-1000)...")  # keterangan di layar
    tetap.gaji_pokok = -1000                # memanggil SETTER dengan -1000 -> muncul peringatan, gaji tetap 7 juta

    print("\nMengubah gaji pokok Budi dengan nilai valid (8.000.000)...")   # \n = pindah baris dulu agar ada jarak
    tetap.gaji_pokok = 8_000_000            # memanggil SETTER dengan 8 juta -> valid, gaji pokok berubah

    print("\nData setelah perubahan:")     # keterangan di layar
    tetap.tampilkan_info()                  # tampilkan ulang: gaji pokok 8 juta, total gaji jadi 9,5 juta (dihitung ulang)