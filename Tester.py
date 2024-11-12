import tkinter as tk  # Mengimpor pustaka Tkinter untuk membuat GUI
from tkinter import messagebox  # Mengimpor messagebox untuk menampilkan pesan peringatan

# Fungsi untuk menampilkan hasil prediksi
def hasil_prediksi():
    # Mengecek apakah ada input yang kosong
    for entry in entries:  # Melakukan iterasi pada setiap entry di list entries
        if entry.get() == "":  # Jika nilai pada entry kosong
            messagebox.showwarning("Peringatan", "NILAI NYA HARAP DI ISI !")  # Menampilkan peringatan
            return  # Keluar dari fungsi jika ada input kosong

    # Jika semua input terisi, tampilkan hasil prediksi
    label_hasil.config(text="Prediksi Prodi: Teknologi Informasi")  # Menampilkan hasil prediksi pada label_hasil

# Membuat jendela utama
root = tk.Tk()  # Membuat instance dari Tk untuk membuat jendela utama
root.title("Aplikasi Prediksi Prodi Pilihan")  # Mengatur judul jendela
root.geometry("400x500")  # Menentukan ukuran jendela utama

# Label judul
label_judul = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16))  # Membuat label untuk judul aplikasi
label_judul.pack(pady=10)  # Menempatkan label di jendela utama dengan jarak padding vertikal 10

# Membuat frame untuk menampung input nilai
frame_input = tk.Frame(root)  # Membuat frame untuk mengelompokkan input nilai
frame_input.pack(pady=20)  # Menempatkan frame di jendela utama dengan padding vertikal 20

# Membuat 10 input nilai mata pelajaran
entries = []  # Membuat list untuk menyimpan setiap entry nilai mata pelajaran
for i in range(10):  # Loop untuk membuat 10 input nilai
    label = tk.Label(frame_input, text=f"Nilai Mata Pelajaran {i+1}")  # Membuat label untuk setiap mata pelajaran
    label.grid(row=i, column=0, padx=5, pady=5)  # Menempatkan label pada baris i, kolom 0 di dalam frame

    entry = tk.Entry(frame_input)  # Membuat entry untuk memasukkan nilai mata pelajaran
    entry.grid(row=i, column=1, padx=5, pady=5)  # Menempatkan entry pada baris i, kolom 1 di dalam frame
    entries.append(entry)  # Menambahkan entry ke dalam list entries

# Button untuk menampilkan hasil prediksi
btn_prediksi = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi)  # Membuat tombol dengan teks "Hasil Prediksi"
btn_prediksi.pack(pady=10)  # Menempatkan tombol di jendela utama dengan padding vertikal 10

# Label untuk menampilkan hasil prediksi
label_hasil = tk.Label(root, text="", font=("Arial", 12))  # Membuat label untuk menampilkan hasil prediksi
label_hasil.pack(pady=10)  # Menempatkan label di jendela utama dengan padding vertikal 10

# Menjalankan aplikasi
root.mainloop()  # Memulai loop utama untuk menjalankan aplikasi Tkinter
