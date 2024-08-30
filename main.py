from collections import defaultdict

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    freq_count = frequency_counter(file_contents)

    freq_count_list = []
    for i in range(97, 123):
        alphabet = chr(i)
        freq_count_list.append((freq_count[alphabet], alphabet))

    print("--- Begin report of books/frankenstein.txt ---")
    print(num_words(file_contents), "words found in the document\n")
    freq_count_list = sorted(freq_count_list, reverse=True)
    for count, character in freq_count_list:
        print("The '" + character + "' character was found " + str(count) + " times") 
    print("--- End report ---")
    
    return

def num_words(text):
    words = text.split()
    word_count = len(words)

    return word_count

def frequency_counter(text):
    words = text.split()
    freq_count = defaultdict(int)

    for word in words:
        word = word.lower()
        for c in word:
            if c.isalpha():
                freq_count[c] += 1

    return freq_count

main()

