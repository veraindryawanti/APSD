def hitung_deret_genap(n):
    deret_genap = [i for i in range(2, n*2+1, 2)]
    return deret_genap

def main():
    deret_genap = hitung_deret_genap(10)
    total = sum(deret_genap)
    
    deret_str = ' + '.join(map(str, deret_genap))
    print(f"{deret_str} = {total}")

if __name__ == "__main__":
    main()