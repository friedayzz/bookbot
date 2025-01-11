def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    words = count_words(file_contents)
    char_list = sort_list(count_chars(file_contents))

    make_report(words, char_list)

def count_words(text):
    words = text.split()
    count = 0
    for word in words:
        count += 1

    return count

def count_chars(txt):
    txt_lowercase = txt.lower()
    new_dict = {}

    for c in txt_lowercase:
        if c not in new_dict:
            new_dict[c] = 0
        if c in new_dict:
            new_dict[c] += 1

    return new_dict

def sort_list(char_dict):
    new_list = []
    for char, count in char_dict.items():
        new_list.append({"char": char, "count": count})

    new_list.sort(reverse=True, key=sort_on)

    return new_list

def sort_on(dict):
    return dict["count"]

def make_report(word_count, characters):
    print("--- This is a report of books/frankenstein.txt ---")
    print(f"{word_count} words was found in the document")
    for i in characters:
        if i["char"].isalpha():
            print(f"The '{i["char"]}' character was found {i["count"]} times.")

    print("--- End of report ---")

main()