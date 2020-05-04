letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q" ,"r", "s", "t", "u", "v", "w", "x", "y", "z"]
text = "bpm owwl vmea ijwcb kwuxcbmza qa bpib bpmg lw epib gwc bmtt bpmu bw lw. bpm jil vmea qa bpib bpmg lw epib gwc bmtt bpmu bw lw."

##def caesar_encrypt(text, shift):
##    shift = int(shift)
##    text = text.lower().split()
##    print(text)
##    new_text = ""
##    
##    for i in text:
##        for j in i:
##            for k in letters:
##                if k == j:
##                    index = ((letters.index(k)) + shift)%26
##                    l = letters[index]
##                    new_text += l
##        new_text += " "
##    print(new_text)
##
##caesar_encrypt(text, 1)


"""
c = (p + a)mod 26
c = new character index
p = original character index
a = shift
"""

##def caesar_decrypt(text, shift):
##    shift = int(shift)
##    text = text.lower().split()
##    print(text)
##    new_text = ""
##    
##    for i in text:
##        for j in i:
##            for k in letters:
##                if k == j:
##                    index = ((letters.index(k)) - shift)%26
##                    l = letters[index]
##                    new_text += l
##        new_text += " "
##    print(new_text)
##
##caesar_decrypt(text, 1)


def caesar_decryption(text):
    shift = 1
    text = text.lower().split()
##    print(text)
    new_text = ""
    good = ""
    
    while good != 1:
        new_text = ""
        for i in text:
            for j in i:
                for k in letters:
                    if k == j:
                        index = ((letters.index(k)) - shift)%26
                        l = letters[index]
                        new_text += l
            new_text += " "
        print(new_text)
        good = int(input("Is the sentence decrypted? Enter 0 for no. Enter 1 for yes."))
        shift += 1
        
    


caesar_decryption(text)
