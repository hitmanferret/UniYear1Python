from practical_6 import sample_text

seperators = [',', '.', "'", " "]

def split_text(sample_text, seperators):
    text = []
    word = ""
    sample_text = sample_text.lower()
    for i in sample_text:
        if i not in seperators:
            word += i
        else:
            if word != "":
                text.append(word)
                word = ""
##    print(text)

    dup_list = []

    for word in text:
        duplicate = False
    
        for index in range(len(dup_list)):
            if dup_list[index][0] == word:
                dup_list[index][1] += 1
                duplicate = True

        if not duplicate:
            dup_list.append([word, 1])

    print(dup_list)


split_text(sample_text, seperators)


"""
append word to new list, first checking if it is already in the new list
check how many times this word is in the original text
print how many times the duplicate words appear
"""
