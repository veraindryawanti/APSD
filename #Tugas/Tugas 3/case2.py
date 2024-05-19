def hitung_nilai_murni(keaktifan, tugas, ujian):
    nilai_murni_keaktifan = keaktifan * 0.20
    nilai_murni_tugas = tugas * 0.30
    nilai_murni_ujian = ujian * 0.50
    return nilai_murni_keaktifan, nilai_murni_tugas, nilai_murni_ujian

def hitung_nilai_akhir(nilai_murni_keaktifan, nilai_murni_tugas, nilai_murni_ujian):
    return nilai_murni_keaktifan + nilai_murni_tugas + nilai_murni_ujian

def tentukan_grade(nilai_akhir):
    if nilai_akhir > 80:
        return "A"
    elif nilai_akhir > 70:
        return "B"
    elif nilai_akhir > 56:
        return "C"
    elif nilai_akhir > 46:
        return "D"
    else:
        return "E"

def main():
    print("PROGRAM HITUNG NILAI AKHIR")
    
    nama_siswa = input("Nama Siswa: ")
    nilai_keaktifan = float(input("Nilai Keaktifan: "))
    nilai_tugas = float(input("Nilai Tugas: "))
    nilai_ujian = float(input("Nilai Ujian: "))
    
    nilai_murni_keaktifan, nilai_murni_tugas, nilai_murni_ujian = hitung_nilai_murni(nilai_keaktifan, nilai_tugas, nilai_ujian)
    nilai_akhir = hitung_nilai_akhir(nilai_murni_keaktifan, nilai_murni_tugas, nilai_murni_ujian)
    grade = tentukan_grade(nilai_akhir)
    
    print(f"\nSiswa yang bernama {nama_siswa}")
    print("Dengan Nilai Persentasi Yang dihasilkan:")
    print(f"Nilai Keaktifan : {nilai_murni_keaktifan:.2f}")
    print(f"Nilai Tugas     : {nilai_murni_tugas:.2f}")
    print(f"Nilai Ujian     : {nilai_murni_ujian:.2f}")
    print(f"Jadi Siswa yang bernama {nama_siswa} memperoleh nilai akhir sebesar {nilai_akhir:.2f} dengan grade {grade}.")
    

if __name__ == "__main__":
    main()
