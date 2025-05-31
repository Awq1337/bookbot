def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()
    char_counts = {}

    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts

def sort_characters(char_dict):
    sorted_chars = []

    for char, count in char_dict.items():
        if char.isalpha():  # pomijamy znaki nie-alfabetyczne
            sorted_chars.append({"char": char, "num": count})

    # Sortujemy malejąco po liczbie wystąpień
    sorted_chars.sort(key=lambda x: x["num"], reverse=True)

    return sorted_chars
