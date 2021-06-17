#9
import os
lines_num, words_num, chars_num = 0,0,0
with open('demotext.txt', 'r') as file:
    for line in file:
        lines_num += 1
        words_num += len(line.split())
        chars_num += sum([len(x) for x in line.split()])
print('No of Lines: %d\nNo of Words: %d\nNo of Characters: %d' % (lines_num, words_num, chars_num))