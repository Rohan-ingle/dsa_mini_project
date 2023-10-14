import streamlit as st
import subprocess

# Function to call your C program and get suggestions
def get_suggestions(word):
    try:
        # Call your C program and pass the input word as an argument
        result = subprocess.run(["C:\\Users\\NotAPro\\Desktop\\dsa_github\\autocomplete.exe", word], capture_output=True, text=True, check=True)
        suggestions = result.stdout
        return suggestions
    except Exception as e:
        return str(e)

# Streamlit UI
st.title("C Code Suggestions App")

word = st.text_input("Enter a word to complete", "")

if st.button("Get Suggestions"):
    if word:
        suggestions = get_suggestions(word)
        st.write("Suggestions:")
        st.write(suggestions)
    else:
        st.write("Please enter a word to get suggestions.")
