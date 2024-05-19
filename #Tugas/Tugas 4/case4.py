def hitung_deret_ganjil_segitiga(n):
    deret_ganjil = [2 * i + 1 for i in range(n)]
    return deret_ganjil

def hitung_perkalian_deret_ganjil(deret_ganjil):
    hasil_perkalian = 1
    for bilangan in deret_ganjil:
        hasil_perkalian *= bilangan
    return hasil_perkalian

def main():
    jumlah_baris = 5
    
    for i in range(1, jumlah_baris + 1):
        deret_ganjil = hitung_deret_ganjil_segitiga(i)
        hasil_perkalian = hitung_perkalian_deret_ganjil(deret_ganjil)
        
        deret_str = ' * '.join(map(str, deret_ganjil))
        print(f"{deret_str} = {hasil_perkalian}")

if __name__ == "__main__":
    main()
