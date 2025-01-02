class Kuliah:
    def __init__(self, nama_mahasiswa):
        self.nama_mahasiswa = nama_mahasiswa
        self.status_spp = False
        self.status_krs = False
        self.status_perkuliahan = False
        self.nilai_tugas = []
        self.nilai_uts = 0
        self.nilai_uas = 0
        self.nilai_akhir = 0

    def bayar_spp(self):
        self.status_spp = True
        print(f"{self.nama_mahasiswa} telah membayar SPP.")

    def isi_krs(self):
        if self.status_spp:
            self.status_krs = True
            print(f"{self.nama_mahasiswa} telah mengisi KRS.")
        else:
            print("SPP belum dibayar! Harap bayar SPP terlebih dahulu.")

    def mulai_perkuliahan(self):
        if self.status_krs:
            self.status_perkuliahan = True
            print(f"{self.nama_mahasiswa} mulai mengikuti perkuliahan.")
        else:
            print("KRS belum diisi! Harap isi KRS terlebih dahulu.")

    def kumpulkan_tugas(self, nilai):
        if self.status_perkuliahan:
            self.nilai_tugas.append(nilai)
            print(f"Tugas dikumpulkan dengan nilai {nilai}.")
        else:
            print("Belum mengikuti perkuliahan! Harap mulai perkuliahan terlebih dahulu.")

    def ikut_uts(self, nilai):
        if self.status_perkuliahan:
            self.nilai_uts = nilai
            print(f"Nilai UTS: {nilai}")
        else:
            print("Belum mengikuti perkuliahan! Harap mulai perkuliahan terlebih dahulu.")

    def ikut_uas(self, nilai):
        if self.status_perkuliahan:
            self.nilai_uas = nilai
            print(f"Nilai UAS: {nilai}")
        else:
            print("Belum mengikuti perkuliahan! Harap mulai perkuliahan terlebih dahulu.")

    def hitung_nilai_akhir(self):
        if self.nilai_tugas and self.nilai_uts and self.nilai_uas:
            rata_tugas = sum(self.nilai_tugas) / len(self.nilai_tugas)
            self.nilai_akhir = (rata_tugas * 0.4) + (self.nilai_uts * 0.3) + (self.nilai_uas * 0.3)
            print(f"Nilai akhir {self.nama_mahasiswa}: {self.nilai_akhir:.2f}")
        else:
            print("Belum lengkap semua nilai. Pastikan tugas, UTS, dan UAS telah diikuti.")

# Simulasi proses
mahasiswa1 = Kuliah("Budi Santoso")
mahasiswa1.bayar_spp()
mahasiswa1.isi_krs()
mahasiswa1.mulai_perkuliahan()
mahasiswa1.kumpulkan_tugas(85)
mahasiswa1.kumpulkan_tugas(90)
mahasiswa1.ikut_uts(80)
mahasiswa1.ikut_uas(88)
mahasiswa1.hitung_nilai_akhir()
