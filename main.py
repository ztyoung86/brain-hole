# -*- coding: utf-8 -*-
import jieba
import operator

jieba.enable_parallel(4)
words = {}
novel = open('lingyu.txt')
for line in novel.readlines():
    for word in jieba.cut(line):
        if words.has_key(word):
            words[word] = words[word] + 1
        else:
            words[word] = 1
novel.close()

# sort words
sorted_words = sorted(words.items(), key=operator.itemgetter(1),reverse=True)
words = dict(sorted_words)

output = open('dict.txt','w')
out_str = ""
for word in sorted_words:
    out_str = word[0]+" "+str(word[1])+"\n"
    # print out_str,
    output.write(out_str.encode("utf-8"))
output.close()
