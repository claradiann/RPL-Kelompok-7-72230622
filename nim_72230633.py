def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return "Error: Pembagian dengan nol tidak diperbolehkan"
    return a / b

while True:
    print("\n=== KALKULATOR SEDERHANA ===")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == '5':
        print("Terima kasih, program selesai.")
        break

    if pilihan in ['1', '2', '3', '4']:
        try:
            a = float(input("Masukkan bilangan pertama: "))
            b = float(input("Masukkan bilangan kedua: "))
        except ValueError:
            print("Input tidak valid, masukkan angka.")
            continue

        if pilihan == '1':
            print(f"Hasil: {a} + {b} = {tambah(a, b)}")
        elif pilihan == '2':
            print(f"Hasil: {a} - {b} = {kurang(a, b)}")
        elif pilihan == '3':
            print(f"Hasil: {a} * {b} = {kali(a, b)}")
        elif pilihan == '4':
            print(f"Hasil: {a} / {b} = {bagi(a, b)}")
    else:
        print("Pilihan tidak tersedia, coba lagi.")
