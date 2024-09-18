def main():
    book_path = "books/frankenstein.txt"                #path to book.
    text = get_book_text(book_path)                     #getting content of book.
    num_words = counting_words(text)                    #returns number of words in text.
    character_count = counting_characters(text)         #returns number of characters.
    aggregated_report = report(character_count)         #returns how many times each letter is counted with sort().
    print("\n(-------------Report begins------------)\n")
    print(f"Number of words in this book: {num_words}\n")
    print(f"{aggregated_report}\n(-------------- Report ends -------------)\n ")
    

def report(character_count):
    sorted_list = list(character_count.items())
    sorted_list.sort(key=lambda x: x[1], reverse=True)
    empty_string = ""
    for character, count in sorted_list:
        empty_string += (f"For the letter {character}, it was found {count} times.\n")
    return empty_string


def counting_characters(text):
    text_lower = text.lower()
    empty_dictionary = {}
    for i in text_lower:
        if i.isalpha():
            if i in empty_dictionary:
                empty_dictionary[i] += 1
            else:
                empty_dictionary[i] = 1
    return empty_dictionary


def counting_words(text):
    words = text.split()
    return len(words)



def get_book_text(path):
    with open(path) as x:
        return x.read()

main()