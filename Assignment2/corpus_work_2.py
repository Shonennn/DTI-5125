# -*- coding: utf-8 -*-
"""corpus_Work_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16co7bPDX_hBAQ_s8fHjp7FzDLiWdbYab
"""

import nltk
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
from nltk.corpus import stopwords

#nltk.download('gutenberg')
text = nltk.corpus.gutenberg.raw('chesterton-thursday.txt')

#nltk.download('punkt')
tokenized_sents=nltk.sent_tokenize(text)
#print(tokenized_sents)
tokenized_word=nltk.word_tokenize(text)
fdist = FreqDist(tokenized_word)
print(fdist)
print(fdist.most_common(2))

fdist.plot(30,cumulative=False)
plt.show()

nltk.download('stopwords')
stop_words=set(stopwords.words("english"))
print(stop_words)

filtered_sents=[]
for w in tokenized_sents:#is this wrong and should be tokenized_word?
    if w not in stop_words:
        filtered_sents.append(w)
#print("Tokenized Sentence:",tokenized_sents)
#print("Filterd Sentence:",filtered_sents)

fdist = FreqDist(filtered_sents)
print(fdist)
print(fdist.most_common(2))

fdist.plot(30,cumulative=False)
plt.show()

