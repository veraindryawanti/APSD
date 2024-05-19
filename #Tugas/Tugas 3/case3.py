def hitung_tunjangan_jabatan(golongan):
    if golongan == 1:
        return 300000 * 0.05
    elif golongan == 2:
        return 300000 * 0.10
    elif golongan == 3:
        return 300000 * 0.15
    else:
        return 0

def hitung_tunjangan_pendidikan(pendidikan):
    if pendidikan.lower() == "sma":
        return 300000 * 0.025
    elif pendidikan.lower() == "d1":
        return 300000 * 0.05
    elif pendidikan.lower() == "d3":
        return 300000 * 0.20
    elif pendidikan.lower() == "s1":
        return 300000 * 0.30
    else:
        return 0

def hitung_honor_lembur(jam_kerja):
    if jam_kerja > 8:
        return (jam_kerja - 8) * 3500
    else:
        return 0

def main():
    print("PROGRAM HITUNG NILAI AKHIR")
    
    nama_karyawan = input("Nama Karyawan: ")
    golongan_jabatan = int(input("Golongan Jabatan (1/2/3): "))
    pendidikan = input("Pendidikan (SMA/D1/D3/S1): ")
    jam_kerja = int(input("Jumlah jam kerja: "))
    
    tunjangan_jabatan = hitung_tunjangan_jabatan(golongan_jabatan)
    tunjangan_pendidikan = hitung_tunjangan_pendidikan(pendidikan)
    honor_lembur = hitung_honor_lembur(jam_kerja)
    
    total_gaji = 300000 + tunjangan_jabatan + tunjangan_pendidikan + honor_lembur
    
    print(f"\nKaryawan yang bernama {nama_karyawan}")
    print(f"Tunjangan Jabatan Rp {tunjangan_jabatan:.2f}")
    print(f"Tunjangan Pendidikan Rp {tunjangan_pendidikan:.2f}")
    print(f"Honor Lembur Rp {honor_lembur:.2f}")
    print(f"Total Gaji yang diterima Rp {total_gaji:.2f}")
    
 
if __name__ == "__main__":
    main()
