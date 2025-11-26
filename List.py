# --- Program List ---

print(" Daftar Perintah (Menggunakan List)")
print("-" * 45)

# List berisi beberapa perintah dasar Linux
# Data dalam kurung siku bisa diubah
perintah_linux = ["ls", "cd", "pwd", "rm"]

print(f"Daftar Perintah Awal: {perintah_linux}")
print(f"Jumlah Perintah: {len(perintah_linux)}")

# Menambahkan item ke List (List itu Mutable/dapat Diubah)
perintah_linux.append("mkdir")
print(f"Setelah ditambah 'mkdir': {perintah_linux}")

# Mengubah item dalam List (List itu Mutable/dapat Diubah)
# Mengubah perintah 'rm' (index 3) menjadi 'cp'
perintah_linux[3] = "cp"
print(f"Setelah diubah index 3: {perintah_linux}")

# 3. Menghapus item dari List
perintah_linux.remove("ls")
print(f"sesudah dihapus 'ls': {perintah_linux}")

print("\nsesudah List (Data fleksibel, dapat diubah)")
