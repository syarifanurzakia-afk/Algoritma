# --- Program Tuple ---

##Tugas Algoritma ##
## NAMA : SY NUR ZAKIA TAU ##
## KELAS A SISTEM INFORMASI ##
##NIM : D0425330##

print("Data Dasar Linux (Menggunakan Tuple)")
print("-" * 45)

# Tiga Tuple yang dibuat secara terpisah
# Data dalam kurung biasa bisa diubah dan juga bisa tidak setelah dibuatkan
info_debian = ("Debian", "Kernel Linux", "APT")
info_fedora = ("Fedora", "Kernel Linux", "DNF/RPM")
info_arch = ("Arch Linux", "Kernel Linux", "Pacman")

# Mengakses data dari Tuple (data tidak bisa diubah)
print(f"Data Tuple Debian: {info_debian}")
print(f"Nama Distro di Index 0: {info_debian[0]}")
print(f"Manajer Paket di Index 2: {info_fedora[2]}")

# Coba mengubah Tuple (akan ERROR)
# info_debian[0] = "Debian Baru" # <- Coba hapus tanda '#' ini, pasti error!
print("\nSelesai Tuple (Data aman, tidak bisa diubah)")
