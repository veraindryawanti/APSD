def hitung_rata_rata(nilai1, nilai2, nilai3):
    return (nilai1 + nilai2 + nilai3) / 3

def tentukan_juara(rata_rata):
    if rata_rata > 80:
        return "I"
    elif rata_rata > 75:
        return "II"
    elif rata_rata > 65:
        return "III"
    else:
        return "tidak juara"

def main():
    print("PROGRAM HITUNG NILAI RATA-RATA")
    
    nama_siswa = input("Nama Siswa: ")
    nilai_pertandingan1 = float(input("Nilai Pertandingan I: "))
    nilai_pertandingan2 = float(input("Nilai Pertandingan II: "))
    nilai_pertandingan3 = float(input("Nilai Pertandingan III: "))
    
    rata_rata = hitung_rata_rata(nilai_pertandingan1, nilai_pertandingan2, nilai_pertandingan3)
    juara = tentukan_juara(rata_rata)
    
    print(f"\nSiswa yang bernama {nama_siswa}")
    print(f"Memperoleh nilai rata-rata {rata_rata:.2f} dan menjadi juara ke-{juara} dari hasil perlombaan yang diikutinya.")

 
if __name__ == "__main__":
    main()
