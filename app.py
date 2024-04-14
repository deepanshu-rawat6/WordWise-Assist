import streamlit as st
import pandas as pd
import textdistance
import re
from collections import Counter

words = []

with open('datasource.txt', 'r', encoding='utf-8') as f:
    data = f.read().lower()
    words = re.findall('\\w+', data)
    words += words

V = set(words)
words_freq_dict = Counter(words)
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
        suggestions_list = suggestions.to_dict('records')  # Convert DataFrame to list of dictionaries
        return suggestions_list

st.title('AutoSuggest System')
st.write("""
This application suggests words based on the input keyword. 
It uses the Jaccard similarity to find similar words and ranks them based on their similarity and frequency in the text.
""")

keyword = st.text_input('Enter a word:')
if st.button('Get Suggestions'):
    if keyword:
        suggestions = suggest(keyword.lower())
        if suggestions:
            st.write(suggestions)