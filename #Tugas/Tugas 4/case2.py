def hitung_deret_ganjil(n):
    deret_ganjil = [i for i in range(1, n*2, 2)]
    return deret_ganjil

def main():
    deret_ganjil = hitung_deret_ganjil(10)
    total = sum(deret_ganjil)
    
    deret_str = ' + '.join(map(str, deret_ganjil))
    print(f"{deret_str} = {total}")

if __name__ == "__main__":
    main()
