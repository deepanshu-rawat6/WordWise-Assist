import textdistance
import pandas as pd
import re
from collections import Counter

word_list = []

with open('datasource.txt', 'r', encoding='utf-8') as f:
    data = f.read().lower()
    words = re.findall('\\w+', data)
    word_list += words

V = set(word_list)
words_freq_dict = Counter(word_list)
Total = sum(words_freq_dict.values())
probs = {}

for k in words_freq_dict.keys():
    probs[k] = words_freq_dict[k] / Total

def suggest(keyword):
    if keyword:
        jac = textdistance.Jaccard(qval=2)
        similarities = [1 - jac.distance(v, keyword) for v in words_freq_dict.keys()]
        df = pd.DataFrame.from_dict(probs, orient='index').reset_index()
        df.columns = ['Word', 'Prob']
        df['Similarity'] = similarities
        suggestions = df.sort_values(['Similarity', 'Prob'], ascending=False)[['Word', 'Similarity']]
        suggestions_list = suggestions.to_dict('records')
        return suggestions_list