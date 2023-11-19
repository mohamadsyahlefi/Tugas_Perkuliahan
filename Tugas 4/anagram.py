def generate_anagrams(word):
    if len(word) <= 1:
        return [word]

    anagrams = []
    for i, letter in enumerate(word):
        prefix = word[:i]
        suffix = word[i+1:]
        for sub_anagram in generate_anagrams(prefix + suffix):
            anagrams.append(letter + sub_anagram)

    return anagrams

def remove_original_word(word, anagrams):
    return [anagram for anagram in anagrams if anagram != word]

# Input kata atau kalimat awal dari pengguna
input_word = input("Masukkan kata atau kalimat: ")

# Menghapus spasi dan mengubah huruf menjadi huruf kecil
input_word = input_word.replace(" ", "").lower()

# Memanggil fungsi untuk menghasilkan anagram
hasil_anagram = generate_anagrams(input_word)

# Menghapus kata awal dari daftar anagram
hasil_anagram = remove_original_word(input_word, hasil_anagram)

# Menghapus duplikasi anagram yang sama
hasil_anagram = list(set(hasil_anagram))

# Mencetak hasil anagram
if hasil_anagram:
    print("\nAnagram yang mungkin:")
    for anagram in hasil_anagram:
        print(anagram)
else:
    print("Tidak ada anagram yang mungkin dari kata tersebut.")
