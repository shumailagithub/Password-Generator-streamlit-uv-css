import streamlit as st                  # Import streamlit Library for creating the Web app
import random                           # Import the random Library for generating random characters
import string                           # Import String Library for using characters

# Function to generate a password based on the user's preferences
def generator_password(length, use_digits, use_special):
    characters = string.ascii_letters    # Include all Letters (a-z, A-Z)
    
    if use_digits:
        characters += string.digits       # Add numbers (0-9) if selected
    
    if use_special:
        characters += string.punctuation    # Add special characters (!, @, #, $, %, ^, &, *)
    
    # Generates a random password of the specified length using the characters defiined obove
    return ''.join(random.choice(characters) for _ in range(length))

# Setting page title and header
st.set_page_config(page_title="Password Generator", layout="centered")

# Header/title
st.title("Password Generator")

# Slider for selecting password length
length = st.slider("Select Password Length", min_value=6,    max_value=32,   value=12)
                                         #  minimam value,  maximum value,   default valu  
                                          
# Checkboxes for including digits and special characters
use_digits = st.checkbox("Include Digits")
use_special = st.checkbox("Include Special Characters")

# Button to generate password
if st.button("Generate Password"):
    password = generator_password(length, use_digits, use_special)
    st.success(f"Generated Password: `{password}`")

# Footer with attribution
st.markdown("---")
st.markdown("Built with ❤️ by [Shumaila Gulfam](https://github.com/shumailagithub)")






# #-------------Password Generator-----------------
# #A simple password generator using python, uv, and streamlit


#---------------------------------------------------------------------------------



# Custom CSS example
st.markdown(
    """
    <style>
    .stButton button {
        background-color: navy;
        color: white;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
