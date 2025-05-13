import streamlit as st
import random

# ✅ 반드시 가장 위에 위치해야 함!
st.set_page_config(page_title="MBTI 직업 추천기 🎯", page_icon="🌈", layout="wide")

# 💖 페이지 꾸미기
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(to right, #fbc2eb, #a6c1ee);
    }
    .stApp {
        background-color: #fff0f5;
    }
    h1 {
        color: #8a2be2;
        font-size: 3em;
        text-align: center;
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }
    .emoji {
        font-size: 1.5em;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 나머지 코드 계속 유지
st.markdown("# 🌟 나의 MBTI로 찾는 ✨꿈의 직업✨")
# ... 이하 동일 ...
