def word_count(file_path):
    word_counts = {}

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                word = word.lower()
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1

    return word_counts


file_path = 'P1_data.txt'
print(word_count(file_path))
