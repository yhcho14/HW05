import sys
import re
import operator

file_name = sys.argv[1]
num = int(sys.argv[2])

file = open(file_name, 'r')
file_str = file.readlines()
file.close()
file_words = []
count_words = dict()

for i in range(len(file_str)):
    file_sentence = re.sub(r"[^a-zA-Z0-9 ]", "", file_str[i])
    file_sentence = file_sentence.split()
    for i in range(len(file_sentence)):
        file_words.append(file_sentence[i])



for i in range(len(file_words)):
    temp = file_words.count(file_words[i])
    count_words[file_words[i]] = temp

count_words = sorted(count_words.items(), key=operator.itemgetter(1), reverse=True)

for i in range(num):
    print(count_words[i][0].ljust(10) + str(count_words[i][1]).rjust(5))

