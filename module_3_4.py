def single_root_words(root_word, *other_words):
    same_words = []
    for words in other_words:
        if (words.find(root_word) == -1):
            k = 1
        else:
            same_words.append(words)



    for words in other_words:
        root_word_lower = root_word.lower()
        words_lower = words.lower()
        if (root_word_lower.find(words_lower) == -1):
            k = 1
        else:
            same_words.append(words)
    return (same_words)


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
