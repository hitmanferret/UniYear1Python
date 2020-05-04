sentence = input("Enter a sentence without punctuation")

##sentence = sentence.replace(" ", "")


##sentence = sentence.title().replace(" ", "")

import re
sentence = re.findall('[A-Z][^A-Z]*', sentence)

print(sentence)

