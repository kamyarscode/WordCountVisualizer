import re
import urllib.request
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

def get_word_list(url):
    words = sorted(list(re.findall(r'[^\d\W_]+', site))) #try not to rely too much on RegEx as it is exponential time.
    return words                                         #probably not worth loss of efficieny

newlist = []
with open('htmltags.txt','r') as file:
    text = file.read()


link = ''
site = urllib.request.urlopen(link).read().decode('utf-8')

words = get_word_list(site)
for word in words:
    if len(word) >= 2 and word not in text:
        newlist.append(word)

file.close()

dictionary = Counter(newlist)
sorted_dic = sorted(((value, key) for (key,value) in dictionary.items()), reverse = True)
name = []
occ = []

for word in sorted_dic:
    name.append(word[1])
    occ.append(word[0])
    print (f'{word[1]} appears {word[0]} time(s)')


plt.xlabel('Occurrence')
plt.title('Frequency of words used in a website')
y = np.arange(len(name))
plt.barh(y, occ, align='center', alpha=0.5)
plt.yticks(y, name)

plt.show()

