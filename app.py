import streamlit as st
import suggestions as suggest_logic

def main():
    st.title('WordWise Assist')
    st.write("""
    This application suggests words based on the input keyword. 
    It uses the Jaccard similarity to find similar words and ranks them based on their similarity and frequency in the text.
    """)

    keyword = st.text_input('Enter a word:')
    if st.button('Get Suggestions'):
        if keyword:
            suggestions = suggest_logic.suggest(keyword.lower())
            if suggestions:
                st.write(suggestions)
            else:
                st.write('No suggestions found')
        else:
            st.write('Please enter a word')

if __name__ == "__main__":
    main()