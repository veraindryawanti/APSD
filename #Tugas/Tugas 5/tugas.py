def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def main():
    panjang_array = int(input("Masukkan panjang array: "))
    array = list(map(int, input("Masukkan elemen-elemen array: ").split()))

    print("\nArray sebelum diurutkan:", ' '.join(map(str, array)))

    bubble_sort(array)

    print("Array setelah diurutkan:", ' '.join(map(str, array)))

if __name__ == "__main__":
    main()
