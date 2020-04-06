

def change_words_starting_with_a(list_of_words):
    new_list = [word + "hello" if word[0] == "a" else word for word in list_of_words]
    for i in new_list:
        print(i)

list = ["apple", "banana", "apricot", "potato"]
change_words_starting_with_a(list)

