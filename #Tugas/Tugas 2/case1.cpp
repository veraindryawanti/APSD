def main():
    print("PROGRAM HITUNG NILAI RATA-RATA")
    
    nim_siswa = input("Nim Siswa: ")
    nama_siswa = input("Nama Siswa: ")
    nilai_tugas1 = float(input("Nilai Tugas I: "))
    nilai_tugas2 = float(input("Nilai Tugas II: "))
    nilai_tugas3 = float(input("Nilai Tugas III: "))
    
    rata_rata = hitung_rata_rata(nilai_tugas1, nilai_tugas2, nilai_tugas3)
    
    print(f"Nim {nim_siswa} Siswa yang bernama {nama_siswa}")
    print(f"Memperoleh nilai rata-rata {rata_rata:.2f} dari hasil tugas yang diikutinya.")

if __name__ == "__main__":
    main()
