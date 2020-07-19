def counter(word):
    dictionary = {}
    for letter in word:
        dictionary[letter] = word.count(letter)
    print(dictionary)

if __name__ == "__main__":
    word = input("Enter a Word : ")
    counter(word)
    


