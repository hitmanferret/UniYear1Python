sentences = "hello my name is Freddie"

def save_list2file(sentences, filename):
    sentences.split()
    file = open(filename,'w')
    for word in sentences:
        file.write(word)
    file.close()

save_list2file(sentences, 'sentences.txt')
