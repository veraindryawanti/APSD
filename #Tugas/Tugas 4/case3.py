def hitung_deret_genap_segitiga(n):
    deret_genap = [2 * i for i in range(1, n + 1)]
    return deret_genap

def main():
    jumlah_baris = 5
    
    for i in range(1, jumlah_baris + 1):
        deret_genap = hitung_deret_genap_segitiga(i)
        total = sum(deret_genap)
        
        deret_str = ' + '.join(map(str, deret_genap))
        print(f"{deret_str} = {total}")

if __name__ == "__main__":
    main()
