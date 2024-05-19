class Mahasiswa:
    def __init__(self, nim, nama, nilai_uts, nilai_uas):
        self.nim = nim
        self.nama = nama
        self.nilai_uts = nilai_uts
        self.nilai_uas = nilai_uas
        self.nilai_hasil = 0
        self.nilai_huruf = ''

    def hitung_nilai(self):
        self.nilai_hasil = (self.nilai_uas * 0.4) + (self.nilai_uts * 0.6)
        if self.nilai_hasil >= 80:
            self.nilai_huruf = 'A'
        elif self.nilai_hasil >= 70:
            self.nilai_huruf = 'B'
        elif self.nilai_hasil >= 56:
            self.nilai_huruf = 'C'
        elif self.nilai_hasil >= 47:
            self.nilai_huruf = 'D'
        else:
            self.nilai_huruf = 'E'

def main():
    n = int(input("Masukkan banyak data mahasiswa: "))
    data_mahasiswa = []

    for i in range(n):
        print(f"\nData Mahasiswa ke-{i+1}:")
        nim = input("Masukkan NIM: ")
        nama = input("Masukkan Nama: ")
        nilai_uts = float(input("Masukkan Nilai UTS: "))
        nilai_uas = float(input("Masukkan Nilai UAS: "))

        mahasiswa = Mahasiswa(nim, nama, nilai_uts, nilai_uas)
        mahasiswa.hitung_nilai()
        data_mahasiswa.append(mahasiswa)

    print("\nTabel Nilai Mahasiswa:")
    print("| No | Nama Mahasiswa  | Nilai UTS | Nilai UAS | Nilai Akhir | Nilai Huruf |")
    print("|----|-----------------|-----------|-----------|-------------|-------------|")
    for i, mhs in enumerate(data_mahasiswa, 1):
        print(f"| {i:2} | {mhs.nama:15} | {mhs.nilai_uts:9} | {mhs.nilai_uas:9} | "
              f"{mhs.nilai_hasil:11.1f} | {mhs.nilai_huruf:11} |")
    print("|----|-----------------|-----------|-----------|-------------|-------------|")

if __name__ == "__main__":
    main()
