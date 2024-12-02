import tkinter as tk

# Kelas induk Animal
class Animal:
    def make_sound(self):
        return "Some sound"
    
# Kelas turunan Bird
class Bird (Animal):
    def make_sound(self):
        return "Tweet tweet"
    
# Kelas turunan Dog
class Dog(Animal):
    def make_sound(self):
        return "Woof woof"

# Kelas turunan Tiger
class Tiger(Animal):
    def make_sound(self):
        return "huaa!!"

# Kelas turunan Snake
class Snake(Animal):
    def make_sound(self):
        return "sisstt"

# Fungsi untuk menampilkan suara berdasarkan jenis hewan yang dipilih
def show_sound(animal):
    label_result.config(text=animal.make_sound())

# Membangun jendela utama menggunakan Tkinter
root = tk.Tk()
root.title("Polimorfisme di Tkinter")

# Label untuk menampilkan hasil suara
label_result = tk.Label(root, text="Klik salah satu tombol untuk mendengar suara hewan.", font=("Arial", 14))
label_result.pack(pady=20)

# Tombol untuk memilih Burung
button_bird = tk.Button(root, text="Burung", font=("Arial", 12), command=lambda: show_sound(Bird()))
button_bird.pack(pady=10)

# Tombol untuk memilih Anjing
button_dog = tk.Button(root, text="Anjing", font=("Arial", 12), command=lambda: show_sound(Dog()))
button_dog.pack(pady=10)

# Tombol untuk memilih Harimau
button_tiger = tk.Button(root, text="Harimau", font=("Arial", 12), command=lambda: show_sound(Tiger()))
button_tiger.pack(pady=10)

# Tombol untuk memilih Ular
button_snake = tk.Button(root, text="Ular", font=("Arial", 12), command=lambda: show_sound(Snake()))
button_snake.pack(pady=10)

# Tombol untuk memilih Hewan Umum
button_animal = tk.Button(root, text="Hewan Umum", font=("Arial", 12), command=lambda: show_sound(Animal()))
button_animal.pack(pady=10)

# Menjalankan aplikasi Tkinter
root.mainloop()