#!/usr/bin/env python
# coding: utf-8
import array as arr
# In[12]:


import math
from textblob import TextBlob as tb
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


# In[13]:


def tf(word, blob):
    return blob.words.count(word) / len(blob.words)


# In[14]:


def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob.words)


# In[15]:


def idf(word, bloblist):
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))


# In[16]:


def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)


# In[17]:


with open('C:/Users/Pratik/Desktop/CV Analysis/CV Analysis/cv.txt', 'r') as file:
    data = file.read().replace('\n', ' ')
# txtdata = pd.read_table('C:/Users/Pratik/Desktop/CV Analysis/CV Analysis/cv.txt')
# document1 = tb("Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of python program maintenance. Python supports modules and packages, which python encourages program modularity and code reuse.")


# In[18]:


document2 = tb("")
print(data)


# In[19]:


lematized_data_token = word_tokenize(data)
tokens_without_sw = [word for word in lematized_data_token if not word in stopwords.words()]
# print(tokens_without_sw)
filtered_sentence = (" ").join(tokens_without_sw)
filtered_sentence = filtered_sentence.upper()
# print(filtered_sentence.upper())
doc2 = tb('"'+filtered_sentence+'"')
print(doc2)
# docs2 = doc2.upper()


# In[20]:


document3 = tb("")


# In[21]:


bloblist = [doc2, document2, document3]


# In[22]:

lst = []
nlst = []
for i, blob in enumerate(bloblist):
    print("Top words in document" .format(i + 1))
    scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
    sorted_words = sorted(scores.items(), key = lambda x: x[1], reverse = True)
    for word, score in sorted_words[:3]:
        print("\tWord: {}, TF-IDF: {}" .format(word, round(score, 5)))
#         lst.append(word)
#         nlst.append(score)
#         # lst = sorted_words[:3]
# print(nlst)
# # print(lst[0])
# s1 = lst[0]
# s2 = lst[1]
# s3 = lst[2]


# sv1 = nlst[0]
# sv2 = nlst[1]
# sv3 = nlst[2]



       



# print(sorted_words[0])             


# print(list[0])
# list = ["python", "java", "c"]
# for a in range(len(list)):
#     print(list[a]) 



# In[ ]:





# In[ ]:




