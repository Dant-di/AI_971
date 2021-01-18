# Task 4
""" !!!!Module 'translate' is required!!!!"""

from translate import Translator
trans = Translator(to_lang="ru")
f_trgt = open('my_file_4_trans.txt', 'a', encoding='UTF8')

with open('my_file_4.txt', 'r', encoding='UTF8') as f_src:
    for line in f_src:
        line = line.split()
        line.insert(0, trans.translate(line.pop(0)))
        f_trgt.writelines(' '.join(line) + '\n')

f_trgt.close()
