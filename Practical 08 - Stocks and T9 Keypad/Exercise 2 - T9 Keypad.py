t9_keypad = {'2':['a','b','c'], '3':['d','e','f'],
             '4':['g','h','i'], '5':['j','k','l'],
             '6':['m','n','o'], '7':['p','q','r','s'],
             '8':['t','u','v'], '9':['w','x','y','z']}

##user_dict = {'4663':[['home',5],['good',8],['hood',1]], '2':[['a',50]]}

vocabulary = ['home', 'good', 'hood', 'bye', 'hello', 'hello', 'good', 'good']

def extract_textonyms(vocabulary, keypad):
    user_dict = dict()
    for element in vocabulary:
        digits = ""
        for letter in element:
            for key,val in t9_keypad.items():
                if letter in val:
                    digits += key
        print(digits, ":", element)

    big_list = []
    sub_list=[]
    for element in vocabulary:
        count = vocabulary.count(element)
        sub_list = [element, count]
        if sub_list not in big_list:
            big_list.append(sub_list)
    print(big_list)

    
            
        


extract_textonyms(vocabulary, t9_keypad)
                
            
