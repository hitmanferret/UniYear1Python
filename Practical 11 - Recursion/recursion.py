# def is_power(a,b):
#     if b == 0 and a != 0:
#         return False
#     if b == 1 and a != b:
#         return False
#     if a == 0 and b == 0:
#         return True
#     division = a/b
#     if division == b or a == 1 or a == b or division == a:
#         return True
#     elif division < b:
#         return False
#     else:
#         a = division
#         return is_power(a,b)

# print(is_power(4,1))


# def sun_digits(nunber):
#     total = 0
#     nunber = str(abs(nunber))
#     def sun(nunber,total):
#         if nunber == "":
#             return total
#         else:
#             integer = int(nunber[0])
#             total += integer
#             return sun(nunber[1::],total)
#     result = sun(nunber,total)
#     return result

# print(sun_digits(1234))


# def rec_sun(nunbers):
#     if nunbers == []:
#         return 0
#     total = 0
#     def sun(nunbers,total):
#         if nunbers == []:
#             return total
#         else:
#             total += nunbers[0]
#             return sun(nunbers[1::],total)
#     return sun(nunbers,total)

# print(rec_sun([1,2,3,4]))


# def iselfish(word):
#     n = 0
#     e = False
#     l = False
#     f = False
#     def _elfish(word, n, e, l, f):

#         if e == True and l == True and f == True:
#             elfish = True
#             return elfish
#         else:
#             elfish = False

#         if n >= len(word):
#             return elfish

#         if word[n] == " " or word[n] == "":
#             return elfish

#         if word[n] == 'e':
#             e = True
#         elif word[n] == 'l':
#             l = True
#         elif word[n] == 'f':
#             f = True

#         n += 1
#         return _elfish(word, n, e, l, f)
#     true_elfish = _elfish(word, n, e, l, f)
#     return true_elfish

# print(iselfish("waffles"))


# def something_ish(pattern, word):
#     pattern = pattern
#     n = 0
#     word_list = []
#     def word_to_list(word, word_list, n):
#         if n >= len(word):
#             return word_list
#         else:
#             word_list.append(word[n])
#             n += 1
#             return word_to_list(word, word_list, n)
    
#     somethingish = False
#     count = 0
#     def pattern_in_word(word_list, pattern, n, count, somethingish):
#         if n >= len(pattern):
#             return somethingish

#         if pattern[n] in word_list:
#             count += 1
        
#         if count == len(pattern):
#             return True
#         else:
#             n += 1
#             return pattern_in_word(word_list, pattern, n, count, somethingish)

#     word_list = word_to_list(word, word_list, n)
#     # print(word_list)
#     pattern_word = pattern_in_word(word_list, pattern, n, count, somethingish)
#     print(pattern_word)
        
# print(something_ish("elf", "whiteleaf"))


# def flatten(mlist):
#     if mlist == []: #catches empty lists in mlist
#         return mlist
#     if isinstance(mlist[0], list):  #checks to see if mlist[0] is a list
#         return flatten(mlist[0]) + flatten(mlist[1:])   #recurses through everything beyond mlist[0]
#     return mlist[:1] + flatten(mlist[1:])   #returns flattened list

# print(flatten([1,[2,[3,[4]]],[]]))


def merge(sorted_listA, sorted_listB):
    