def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    words_count = count_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{words_count} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    lowered_text = text.lower()
    letters_dict = {}
    for letter in lowered_text:
        if letter not in letters_dict:
            letters_dict[letter] = 0
        letters_dict[letter] += 1
    return letters_dict

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_letters = []
    for ch in num_chars_dict:
        sorted_letters.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_letters.sort(reverse=True, key=sort_on)
    return sorted_letters


main()


