import nltk
from nltk.corpus import gutenberg
from nltk.tokenize import word_tokenize
import random
import pandas as pd
import re

# download multiple books from Project Gutenberg
book_ids = ['melville-moby_dick.txt', 'austen-emma.txt', 'shakespeare-hamlet.txt']
# found these id from document
samples_list = []

for idx, book_id in enumerate(book_ids):
    # download the text of the books and tokenize them into words.
    text = nltk.corpus.gutenberg.raw(book_id)
    words = nltk.word_tokenize(text)
    # create random samples of 100 words each
    num_samples = 200
    sample_size = 100
    #
    start_indices = random.sample(range(len(words) - sample_size), num_samples)
    samples = [words[i:i + sample_size] for i in start_indices]
    label = chr(ord('a') + idx)
    samples_list.append(pd.DataFrame({'text': samples, 'label': label}))

df = pd.concat(samples_list)

# create a new column to store the matches
df['matches'] = df['text'].apply(lambda x: re.findall(r'pattern', ' '.join(x)))

# save dataframe to csv
df.to_csv('book_samples.csv')
