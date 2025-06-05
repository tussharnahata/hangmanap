# streamlit_app.py
import streamlit as st
import random

# Word list
word_list = ['python', 'java', 'kotlin', 'javascript', 'hangman', 'challenge', 'notebook']

def get_word():
    return random.choice(word_list).upper()

def display_word(word, guesses):
    return " ".join([letter if letter in guesses else "_" for letter in word])

# Session State Setup
if "word" not in st.session_state:
    st.session_state.word = get_word()
    st.session_state.guesses = []
    st.session_state.tries = 6
    st.session_state.game_over = False

st.title("🎯 Hangman Game")

st.write(f"Tries left: {st.session_state.tries}")
st.write(display_word(st.session_state.word, st.session_state.guesses))

if not st.session_state.game_over:
    guess = st.text_input("Enter a letter or the full word:").upper()
    
    if st.button("Guess"):
        if guess:
            if len(guess) == 1 and guess.isalpha():
                if guess in st.session_state.guesses:
                    st.warning("You already guessed that letter.")
                elif guess not in st.session_state.word:
                    st.session_state.tries -= 1
                    st.session_state.guesses.append(guess)
                    st.error(f"{guess} is not in the word.")
                else:
                    st.session_state.guesses.append(guess)
                    st.success(f"Good job! {guess} is in the word.")
            elif len(guess) == len(st.session_state.word) and guess.isalpha():
                if guess == st.session_state.word:
                    st.success(f"You guessed the word! 🎉 It's {st.session_state.word}")
                    st.session_state.game_over = True
                else:
                    st.session_state.tries -= 1
                    st.error("Wrong guess.")
            else:
                st.warning("Invalid guess.")
            
            if all(letter in st.session_state.guesses for letter in st.session_state.word):
                st.success(f"You guessed all letters! 🎉 It's {st.session_state.word}")
                st.session_state.game_over = True

            if st.session_state.tries == 0:
                st.error(f"You lost. The word was {st.session_state.word}")
                st.session_state.game_over = True

if st.session_state.game_over:
    if st.button("Play Again"):
        st.session_state.word = get_word()
        st.session_state.guesses = []
        st.session_state.tries = 6
        st.session_state.game_over = False
