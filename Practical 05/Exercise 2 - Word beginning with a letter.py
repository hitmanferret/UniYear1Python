sample_text = (" As Pythons creato I d like to say a few words about its "+
              "origins adding a bit of personal philosophy "+
              "Over six years ago in December I was looking for a "+
              "hobby programming project that would keep me occupied "+
              "during the week around Christmas My office "+
              "a government run research lab in Amsterdam would be closed "+
              "but I had a home computer and not much else on my hands "+
              " I decided to write an interpreter for the new scripting "+
              "language  I had been thinking about lately a descendant of ABC "+
              "that would appeal to UnixC hackers I chose Python as a "+
              "working title for   the project being in a slightly irreverent "+
              "mood and a big fan of Monty Pythons Flying Circus")

def get_words_starting_with(text, letter):
    letter = letter
    word_list = text.lower().split()
    same_words = []
    duplicates = 0
    duplicate_list = []
##    print(word_list)

    for i in word_list:
        if i[0] == letter.upper() or i[0] == letter.lower() and not i in same_words:
            same_words.append(i)
        elif i[0] == letter.upper() or i[0] == letter.lower() and i in same_words:
            for j in word_list:
                if j == i and not i in duplicate_list:
                    duplicate_list.append(i)
                        
    for k in duplicate_list:
        for i in word_list:
            if k == i:
                duplicates += 1
        print("There are", duplicates, " duplicates of the word", k)
        duplicates = 0
    
    print(duplicate_list)
    print(same_words)


get_words_starting_with(sample_text,"p")

