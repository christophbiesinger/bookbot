def number_of_words(book):
    words = book.split()


    return len(words)

def count_characters(book):
    lowered = book.lower()
    result = {}

    for char in lowered:
        if char.isalpha():
            if char not in result:
                result[char] = 1
            else:
                result[char] += 1

    return dict(sorted(result.items(), key=lambda item: item[1], reverse=True))

# def sort_on(dict):
#     return dict["num"]



def main():
    path = "books/frankenstein.txt"
    with open(path) as f:
        file_contents = f.read()
        number = number_of_words(file_contents)

        chars = count_characters(file_contents)
        converted_list = []

        for i in chars:
            converted_list.append({i:chars[i]})

        print(f"--- Begin report of {path} ---")
        print(f"{number} words found in the document")
        print("")

        for word in converted_list:
            for k, v in word.items():
                print(f"The '{k}' character was found {v} times")
        
        print("--- End report ---")

main()
