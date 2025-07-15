
sample_text = """The quick brown fox jumps over the lazy dog.
The dog was not amused. The fox was quick and clever."""

with open("sample.txt", "w") as file:
    file.write(sample_text)

print("✅ 'sample.txt' file has been created.\n")

def count_words_in_file(filename):
    word_count = {}

    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.lower().strip()
                words = line.split()
                
                for word in words:
                    word = ''.join(char for char in word if char.isalnum())
                    if word:
                        word_count[word] = word_count.get(word, 0) + 1

        print("📊 Word Count (Alphabetical Order):")
        for word in sorted(word_count):
            print(f"{word}: {word_count[word]}")

    except FileNotFoundError:
        print(f"❌ File '{filename}' not found.")


count_words_in_file("sample.txt")
