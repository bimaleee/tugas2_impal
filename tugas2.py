def konversi_nilai(nilai):
    if nilai == 'A':
        return 4.0
    elif nilai == 'B':
        return 3.0
    elif nilai == 'C':
        return 2.0
    elif nilai == 'D':
        return 1.0
    elif nilai == 'E':
        return 0.0
    else:
        return 0.0

jumlah_mata_kuliah = int(input("Masukkan jumlah mata kuliah: "))

total_sks = 0
total_nilai_sks = 0

for i in range(jumlah_mata_kuliah):
    nama_mata_kuliah = input(f"Masukkan nama mata kuliah ke-{i+1}: ")
    nilai = input(f"Masukkan nilai mata kuliah {nama_mata_kuliah} (A/B/C/D/E): ").upper()
    sks = int(input(f"Masukkan SKS untuk mata kuliah {nama_mata_kuliah}: "))
    
    nilai_angka = konversi_nilai(nilai)
    nilai_sks = nilai_angka * sks
    total_nilai_sks += nilai_sks
    total_sks += sks

if total_sks > 0:
    IPK = total_nilai_sks / total_sks
    print(f"IPK Anda adalah: {IPK:.2f}")
else:
    print("Jumlah SKS tidak valid.")